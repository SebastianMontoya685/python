# AWS CLI Quick Reference Card

## Most Common Commands

### Configuration
```bash
aws configure                                    # Configure AWS CLI
aws configure list                               # List current configuration
aws sts get-caller-identity                      # Get current identity
```

### EC2 Instances
```bash
aws ec2 describe-instances                       # List all instances
aws ec2 run-instances --image-id ami-xxx --instance-type t3.micro
aws ec2 stop-instances --instance-ids i-xxx      # Stop instance
aws ec2 start-instances --instance-ids i-xxx     # Start instance
aws ec2 terminate-instances --instance-ids i-xxx # Terminate instance
aws ec2 describe-instance-types                  # List instance types
```

### S3 Buckets
```bash
aws s3 ls                                        # List buckets
aws s3 mb s3://bucket-name                       # Create bucket
aws s3 rb s3://bucket-name                       # Delete bucket
aws s3 ls s3://bucket-name                       # List objects
aws s3 cp file.txt s3://bucket-name/             # Upload
aws s3 cp s3://bucket-name/file.txt .            # Download
aws s3 sync local-dir s3://bucket-name/          # Sync directory
aws s3 rm s3://bucket-name/file.txt              # Delete file
```

### IAM
```bash
aws iam list-users                               # List users
aws iam create-user --user-name username         # Create user
aws iam delete-user --user-name username         # Delete user
aws iam list-groups                              # List groups
aws iam attach-user-policy --user-name x --policy-arn y
aws iam list-roles                               # List roles
```

### Lambda
```bash
aws lambda list-functions                        # List functions
aws lambda get-function --function-name x        # Get function
aws lambda invoke --function-name x output.json  # Invoke function
aws lambda update-function-code --function-name x --zip-file fileb://x.zip
aws lambda delete-function --function-name x     # Delete function
```

### CloudWatch
```bash
aws logs describe-log-groups                     # List log groups
aws logs tail /aws/lambda/my-function --follow   # Tail logs
aws logs filter-log-events --log-group-name x --filter-pattern ERROR
aws cloudwatch get-metric-statistics --namespace AWS/EC2 --metric-name CPUUtilization
```

### VPC
```bash
aws ec2 describe-vpcs                            # List VPCs
aws ec2 describe-subnets                         # List subnets
aws ec2 describe-security-groups                 # List security groups
aws ec2 describe-route-tables                    # List route tables
```

### CloudFormation
```bash
aws cloudformation validate-template --template-body file://template.yaml
aws cloudformation create-stack --stack-name x --template-body file://template.yaml
aws cloudformation describe-stacks --stack-name x
aws cloudformation delete-stack --stack-name x
```

## Common Filters and Queries

### JMESPath Examples
```bash
# Filter running instances
aws ec2 describe-instances \
  --query "Reservations[*].Instances[?State.Name=='running'].[InstanceId,InstanceType]"

# Extract specific fields
aws s3api list-buckets --query "Buckets[*].[Name,CreationDate]"

# Count resources
aws ec2 describe-instances --query "length(Reservations)"

# Custom output
aws ec2 describe-instances \
  --query "Reservations[*].Instances[*].{ID:InstanceId,Type:InstanceType,IP:PrivateIpAddress}"
```

### Useful Filters
```bash
# By tags
aws ec2 describe-instances --filters "Name=tag:Name,Values=production"

# By state
aws ec2 describe-instances --filters "Name=instance-state-name,Values=running"

# By instance type
aws ec2 describe-instances --filters "Name=instance-type,Values=t3.micro"
```

## Output Formats
```bash
--output json      # JSON (default, machine-readable)
--output text      # Tab-delimited text
--output table     # Formatted table (human-readable)
--output yaml      # YAML format
```

## Common Flags
```bash
--region us-east-1                # Specify region
--profile myprofile               # Use specific profile
--query "..."                     # JMESPath query
--filters "..."                   # Resource filters
--output json|text|table          # Output format
--no-cli-pager                    # Disable pager
--dry-run                         # Test without changes
```

## Useful Pipe Commands
```bash
aws ec2 describe-instances | jq '.'                    # Pretty JSON
aws s3 ls | grep "my-bucket"                           # Filter results
aws ec2 describe-instances --output text | cut -f5     # Extract column
aws lambda list-functions --query "Functions[*].FunctionName" --output text | \
    xargs -I {} aws lambda get-function --function-name {}  # Batch operations
```

## Debugging
```bash
export AWS_CLI_LOG_LEVEL=DEBUG        # Enable debug logging
aws s3 ls 2>&1 | tee debug.log       # Save output to file
aws configure set cli_pager /bin/cat # Disable pager
```

## Cost Management
```bash
aws ce get-cost-and-usage --time-period Start=2024-01-01,End=2024-01-31 \
    --granularity MONTHLY --metrics BlendedCost

aws ec2 describe-volumes --filters Name=status,Values=available
```

## Security
```bash
aws iam list-access-keys --user-name username
aws ec2 describe-security-groups --filters "Name=ip-permission.cidr,Values=0.0.0.0/0"
aws s3api get-bucket-acl --bucket my-bucket
```

## Getting Help
```bash
aws help                           # General help
aws s3 help                        # Service help
aws s3 cp help                     # Command help
aws s3api list-objects-v2 help     # API help
```

## Common One-Liners

### List all EC2 instances (formatted)
```bash
aws ec2 describe-instances \
  --query "Reservations[*].Instances[*].[InstanceId,InstanceType,State.Name,PrivateIpAddress]" \
  --output table
```

### Show S3 bucket sizes
```bash
aws s3 ls --recursive --summarize --human-readable s3://my-bucket
```

### Find all public S3 buckets
```bash
aws s3api list-buckets --query "Buckets[*].Name" --output text | \
    xargs -I {} sh -c 'echo "Checking {}..." && \
    aws s3api get-bucket-acl --bucket {} | \
    grep -q "AllUsers" && echo "{} is PUBLIC!"'
```

### Start all stopped instances in a region
```bash
aws ec2 describe-instances --filters "Name=instance-state-name,Values=stopped" \
  --query "Reservations[*].Instances[*].InstanceId" --output text | \
  xargs -I {} aws ec2 start-instances --instance-ids {}
```

### Get Lambda function sizes
```bash
aws lambda list-functions \
  --query "Functions[*].[FunctionName,CodeSize]" \
  --output table | sort -k2 -nr
```

### Check your AWS account limits
```bash
aws service-quotas list-service-quotas --service-code ec2 | \
    jq '.Quotas[] | select(.UsageMetric != null) | {Name: .QuotaName, Value: .Value}'
```

## Tips
1. Use `--dry-run` to test commands without making changes
2. Combine commands with `&&` for sequential execution
3. Use `--region` to work with specific regions
4. Learn JMESPath for powerful data extraction
5. Always use `--output table` for human-readable results
6. Save complex commands as shell scripts
7. Use CloudShell for quick testing without local setup
8. Enable MFA on your AWS account

## Practice Commands for Daily Use
```bash
# Morning routine
aws sts get-caller-identity
aws ec2 describe-instances --query "length(Reservations)"

# Monitoring
aws cloudwatch get-metric-statistics ...
aws logs tail /aws/lambda/my-function --follow

# Cost check
aws ce get-cost-and-usage ...

# Inventory
aws ec2 describe-instances --output table
aws s3 ls
aws iam list-users
```

Save this file and reference it often as you practice! 🚀


