#!/bin/bash
# EC2 Inventory Script
# Lists all EC2 instances with key information

echo "====================================="
echo "       EC2 Instance Inventory        "
echo "====================================="
echo ""

# Get all instances
aws ec2 describe-instances \
  --query "Reservations[*].Instances[*].[InstanceId,InstanceType,State.Name,PrivateIpAddress,PublicIpAddress,Tags[?Key=='Name'].Value|[0]]" \
  --output table

echo ""
echo "====================================="
echo "      Instance Summary              "
echo "====================================="

TOTAL=$(aws ec2 describe-instances \
  --query "length(Reservations)" \
  --output text)

RUNNING=$(aws ec2 describe-instances \
  --filters "Name=instance-state-name,Values=running" \
  --query "length(Reservations)" \
  --output text)

STOPPED=$(aws ec2 describe-instances \
  --filters "Name=instance-state-name,Values=stopped" \
  --query "length(Reservations)" \
  --output text)

echo "Total Instances: $TOTAL"
echo "Running: $RUNNING"
echo "Stopped: $STOPPED"
echo ""

echo "====================================="
echo "      Security Groups               "
echo "====================================="
aws ec2 describe-security-groups \
  --query "SecurityGroups[*].[GroupId,GroupName,Description]" \
  --output table

echo ""
echo "====================================="
echo "      Untagged Instances            "
echo "====================================="
aws ec2 describe-instances \
  --filters "Name=tag:Name,Values=" \
  --query "Reservations[*].Instances[*].[InstanceId,InstanceType,State.Name]" \
  --output table

echo ""
echo "Inventory complete!"


