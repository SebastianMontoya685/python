#!/bin/bash
# AWS Cost Check Script
# Shows daily costs for the past 7 days

echo "====================================="
echo "        AWS Cost Analysis           "
echo "====================================="
echo ""

# Calculate date range
END_DATE=$(date +%Y-%m-%d)
START_DATE=$(date -v-7d +%Y-%m-%d)

echo "Period: ${START_DATE} to ${END_DATE}"
echo ""

# Check if jq is installed
if ! command -v jq &> /dev/null; then
    echo "Note: Install 'jq' for better output formatting: brew install jq"
    echo ""
    # Get costs without jq
    aws ce get-cost-and-usage \
      --time-period Start=$START_DATE,End=$END_DATE \
      --granularity DAILY \
      --metrics "BlendedCost" "UnblendedCost" \
      --output table
else
    # Get costs with formatted output
    echo "Daily Costs:"
    aws ce get-cost-and-usage \
      --time-period Start=$START_DATE,End=$END_DATE \
      --granularity DAILY \
      --metrics "BlendedCost" "UnblendedCost" \
      --output json | jq -r '.ResultsByTime[] | "\(.TimePeriod.Start): \$\(.Total.BlendedCost.Amount)"'
    
    echo ""
    echo "By Service:"
    aws ce get-cost-and-usage \
      --time-period Start=$START_DATE,End=$END_DATE \
      --granularity DAILY \
      --metrics "BlendedCost" \
      --group-by Type=SERVICE \
      --output json | \
      jq -r '.ResultsByTime[] | select(.Groups != null) | .Groups[] | "\(.Keys[0]): \$\(.Metrics.BlendedCost.Amount)"' | \
      sort -k2 -rn | head -20
fi

echo ""
echo "====================================="
echo ""

# Additional checks
echo "Potential Cost Savings:"
echo ""

echo "Untagged Resources:"
UNTAGGED=$(aws ec2 describe-instances \
  --filters "Name=tag:Name,Values=" \
  --query "length(Reservations)" \
  --output text)
echo "  - Untagged EC2 instances: $UNTAGGED"
echo "  - Consider tagging all resources for better cost allocation"

echo ""
echo "Unattached EBS Volumes:"
UNATTACHED=$(aws ec2 describe-volumes \
  --filters Name=status,Values=available \
  --query "length(Volumes)" \
  --output text)
echo "  - Unattached volumes: $UNATTACHED"
if [ "$UNATTACHED" -gt 0 ]; then
    echo "  - WARNING: These are incurring costs!"
    aws ec2 describe-volumes \
      --filters Name=status,Values=available \
      --query "Volumes[*].[VolumeId,Size,CreateTime]" \
      --output table
fi

echo ""
echo "Old Snapshots:"
OLD_SNAPS=$(aws ec2 describe-snapshots \
  --owner-ids self \
  --query "length(Snapshots[?StartTime<='$(date -v-30d -u +%Y-%m-%dT%H:%M:%S)'])" \
  --output text)
echo "  - Snapshots older than 30 days: $OLD_SNAPS"
echo "  - Consider setting lifecycle policies"

echo ""
echo "Cost check complete!"


