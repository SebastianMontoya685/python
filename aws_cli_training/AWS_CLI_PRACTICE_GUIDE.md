# AWS CLI Practice Guide for Cloud Engineers

## Overview
This guide contains practical command-line exercises tailored for aspiring AWS Cloud Engineers. These exercises are based on real-world scenarios and tasks you'll encounter in AWS cloud engineering roles.

**Prerequisites:**
- AWS Account (you have this!)
- AWS CLI installed and configured
- Basic command-line familiarity

---

## Setup & Configuration

### Exercise 0: Install and Configure AWS CLI

**Objective:** Set up your AWS CLI environment

**Commands:**
```bash
# Install AWS CLI (macOS with Homebrew)
brew install awscli

# Or download from: https://aws.amazon.com/cli/

# Configure AWS CLI with your credentials
aws configure

# This will prompt you for:
# - AWS Access Key ID
# - AWS Secret Access Key
# - Default region name (e.g., us-east-1)
# - Default output format (json, text, or table)

# Verify configuration
aws sts get-caller-identity

# View current configuration
aws configure list
```

**Expected Output:**
- Your AWS account ID, user ARN, and current configuration

**Learning Points:**
- Understanding AWS credentials (Access Keys, Secret Keys)
- Choosing appropriate regions for your workloads
- Different output formats and when to use each

---

## Core AWS Services

### Exercise 1: EC2 (Elastic Compute Cloud) - Launch and Manage Instances

**Objective:** Launch, monitor, and terminate EC2 instances

**Commands:**
```bash
# 1. Get available AMIs (Amazon Machine Images) for Linux
aws ec2 describe-images \
  --owners amazon \
  --filters "Name=name,Values=amzn2-ami-hvm-*" \
  --query "Images | sort_by(@, &CreationDate) | [-1].[ImageId,Name]" \
  --output table

# 2. List available instance types
aws ec2 describe-instance-type-offerings \
  --location-type availability-zone \
  --filters Name=instance-type,Values=t3.micro \
  --query "InstanceTypeOfferings | [0].[InstanceType]" \
  --output text

# 3. Create a key pair for SSH access
aws ec2 create-key-pair \
  --key-name my-training-key \
  --query 'KeyMaterial' \
  --output text > my-training-key.pem

chmod 400 my-training-key.pem

# 4. Create a security group
aws ec2 create-security-group \
  --group-name training-sg \
  --description "Security group for AWS CLI training"

# 5. Add SSH access to security group (get group-id from above output)
aws ec2 authorize-security-group-ingress \
  --group-id sg-xxxxx \
  --protocol tcp \
  --port 22 \
  --cidr 0.0.0.0/0

# 6. Launch an EC2 instance
aws ec2 run-instances \
  --image-id ami-xxxxx \
  --count 1 \
  --instance-type t3.micro \
  --key-name my-training-key \
  --security-group-ids sg-xxxxx \
  --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=Training-Instance}]'

# 7. List running instances
aws ec2 describe-instances \
  --filters "Name=instance-state-name,Values=running" \
  --query "Reservations[*].Instances[*].[InstanceId,InstanceType,PublicIpAddress,State.Name,Tags[?Key=='Name'].Value|[0]]" \
  --output table

# 8. Stop an instance
aws ec2 stop-instances --instance-ids i-xxxxx

# 9. Terminate an instance (cleanup)
aws ec2 terminate-instances --instance-ids i-xxxxx
```

**Learning Points:**
- Understanding AMIs, instance types, and pricing
- Security groups and network access control
- Tagging resources for organization
- Managing instance lifecycle

**Practice Challenge:**
- Launch 3 instances with different instance types
- Filter instances by tags
- Stop all instances with a specific tag

---

### Exercise 2: S3 (Simple Storage Service) - Bucket Management

**Objective:** Create buckets, upload/download files, and manage objects

**Commands:**
```bash
# 1. Create an S3 bucket (bucket names must be globally unique)
aws s3api create-bucket \
  --bucket your-unique-bucket-name-training \
  --region us-east-1

# 2. Enable versioning
aws s3api put-bucket-versioning \
  --bucket your-unique-bucket-name-training \
  --versioning-configuration Status=Enabled

# 3. Upload a file
echo "Hello AWS!" > test-file.txt
aws s3 cp test-file.txt s3://your-unique-bucket-name-training/

# 4. Upload with server-side encryption
aws s3 cp test-file.txt s3://your-unique-bucket-name-training/encrypted-file.txt \
  --server-side-encryption AES256

# 5. List objects in bucket
aws s3 ls s3://your-unique-bucket-name-training/

# 6. Download a file
aws s3 cp s3://your-unique-bucket-name-training/test-file.txt downloaded-file.txt

# 7. Sync a directory to S3 (useful for website hosting)
mkdir local-site
echo "<html><body>Hello!</body></html>" > local-site/index.html
aws s3 sync local-site/ s3://your-unique-bucket-name-training/

# 8. Set bucket policy (make bucket publicly readable)
cat > bucket-policy.json << EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::your-unique-bucket-name-training/*"
    }
  ]
}
EOF

aws s3api put-bucket-policy \
  --bucket your-unique-bucket-name-training \
  --policy file://bucket-policy.json

# 9. Get bucket metadata
aws s3api list-objects-v2 \
  --bucket your-unique-bucket-name-training \
  --query "Contents[*].[Key,Size,LastModified]" \
  --output table

# 10. Delete objects (cleanup)
aws s3 rm s3://your-unique-bucket-name-training/ --recursive

# 11. Delete bucket
aws s3api delete-bucket --bucket your-unique-bucket-name-training
```

**Learning Points:**
- S3 naming conventions and global uniqueness
- Versioning and lifecycle management
- Encryption options
- S3 as static website hosting
- Bucket policies for access control

**Practice Challenge:**
- Create a lifecycle policy to transition old files to cheaper storage
- Set up cross-region replication
- Build a backup script using S3 sync

---

### Exercise 3: IAM (Identity and Access Management) - User & Permission Management

**Objective:** Manage users, groups, roles, and policies

**Commands:**
```bash
# 1. Create an IAM user
aws iam create-user --user-name training-user

# 2. Create an IAM group
aws iam create-group --group-name training-group

# 3. Add user to group
aws iam add-user-to-group \
  --user-name training-user \
  --group-name training-group

# 4. Attach managed policy to group
aws iam attach-group-policy \
  --group-name training-group \
  --policy-arn arn:aws:iam::aws:policy/ReadOnlyAccess

# 5. Create an inline policy
cat > inline-policy.json << EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::your-bucket/*",
        "arn:aws:s3:::your-bucket"
      ]
    }
  ]
}
EOF

aws iam put-user-policy \
  --user-name training-user \
  --policy-name S3ReadAccess \
  --policy-document file://inline-policy.json

# 6. Create access keys for the user
aws iam create-access-key --user-name training-user

# 7. List all users
aws iam list-users --query "Users[*].[UserName,CreateDate]" --output table

# 8. List policies attached to a user
aws iam list-attached-user-policies --user-name training-user

# 9. Create an IAM role (for EC2)
aws iam create-role \
  --role-name ec2-training-role \
  --assume-role-policy-document '{
    "Version": "2012-10-17",
    "Statement": [{
      "Effect": "Allow",
      "Principal": {"Service": "ec2.amazonaws.com"},
      "Action": "sts:AssumeRole"
    }]
  }'

# 10. Attach policy to role
aws iam attach-role-policy \
  --role-name ec2-training-role \
  --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess

# 11. List all roles
aws iam list-roles --query "Roles[*].[RoleName,Arn]" --output table

# Cleanup
aws iam delete-user --user-name training-user
aws iam delete-role --role-name ec2-training-role
```

**Learning Points:**
- IAM users vs roles vs groups
- Managed policies vs inline policies
- Principal of least privilege
- Service roles and trust policies
- IAM best practices

**Practice Challenge:**
- Create a policy that only allows S3 access during business hours
- Set up cross-account access using roles
- Enforce MFA requirement with a policy

---

### Exercise 4: CloudWatch Logs - Monitoring and Logging

**Objective:** Create log groups, streams, and query logs

**Commands:**
```bash
# 1. Create a log group
aws logs create-log-group --log-group-name /aws/training/app-logs

# 2. Create a log stream
aws logs create-log-stream \
  --log-group-name /aws/training/app-logs \
  --log-stream-name app-stream-1

# 3. Put log events
aws logs put-log-events \
  --log-group-name /aws/training/app-logs \
  --log-stream-name app-stream-1 \
  --log-events timestamp=$(date +%s)000,message="Application started"

# 4. Get log events
aws logs get-log-events \
  --log-group-name /aws/training/app-logs \
  --log-stream-name app-stream-1 \
  --start-time $(($(date +%s) - 3600))000

# 5. Filter log events
aws logs filter-log-events \
  --log-group-name /aws/training/app-logs \
  --filter-pattern "ERROR" \
  --start-time $(($(date +%s) - 86400))000

# 6. List all log groups
aws logs describe-log-groups \
  --query "logGroups[*].[logGroupName,storedBytes]" \
  --output table

# 7. Set retention policy
aws logs put-retention-policy \
  --log-group-name /aws/training/app-logs \
  --retention-in-days 7

# 8. Query logs using CloudWatch Logs Insights
aws logs start-query \
  --log-group-name /aws/training/app-logs \
  --start-time $(($(date +%s) - 3600))000 \
  --end-time $(date +%s)000 \
  --query-string 'fields @timestamp, @message | filter @message like /ERROR/'

# Cleanup
aws logs delete-log-group --log-group-name /aws/training/app-logs
```

**Learning Points:**
- Centralized logging best practices
- Log retention and cost management
- Querying logs for troubleshooting
- CloudWatch Logs Insights for analysis

**Practice Challenge:**
- Create a metric filter for specific errors
- Set up log-based alarms
- Export logs to S3

---

### Exercise 5: Lambda - Serverless Functions

**Objective:** Create and invoke AWS Lambda functions

**Commands:**
```bash
# 1. Create a simple Lambda function ZIP file
mkdir lambda-function
cat > lambda-function/index.js << EOF
exports.handler = async (event) => {
    const response = {
        statusCode: 200,
        body: JSON.stringify('Hello from Lambda!'),
    };
    return response;
};
EOF

cd lambda-function
zip function.zip index.js
cd ..

# 2. Create IAM role for Lambda
aws iam create-role \
  --role-name lambda-execution-role \
  --assume-role-policy-document '{
    "Version": "2012-10-17",
    "Statement": [{
      "Effect": "Allow",
      "Principal": {"Service": "lambda.amazonaws.com"},
      "Action": "sts:AssumeRole"
    }]
  }'

aws iam attach-role-policy \
  --role-name lambda-execution-role \
  --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole

# Wait a moment for IAM role propagation
sleep 5

# 3. Create Lambda function
aws lambda create-function \
  --function-name training-function \
  --runtime nodejs18.x \
  --role arn:aws:iam::ACCOUNT_ID:role/lambda-execution-role \
  --handler index.handler \
  --zip-file fileb://lambda-function/function.zip \
  --description "Training Lambda function"

# 4. List Lambda functions
aws lambda list-functions \
  --query "Functions[*].[FunctionName,Runtime,LastModified]" \
  --output table

# 5. Invoke function
aws lambda invoke \
  --function-name training-function \
  response.json

cat response.json

# 6. Update function code
echo 'exports.handler = async (event) => { return { statusCode: 200, body: JSON.stringify("Updated!") }; };' > lambda-function/index.js
cd lambda-function && zip function.zip index.js && cd ..

aws lambda update-function-code \
  --function-name training-function \
  --zip-file fileb://lambda-function/function.zip

# 7. Get function configuration
aws lambda get-function --function-name training-function

# 8. Create function URL (public access)
aws lambda create-function-url-config \
  --function-name training-function \
  --auth-type NONE \
  --cors AllowOrigins="*"

# Cleanup
aws lambda delete-function --function-name training-function
aws iam delete-role --role-name lambda-execution-role
```

**Learning Points:**
- Serverless architecture principles
- Lambda execution roles
- Function versioning and aliases
- Event-driven architecture
- Cost optimization for Lambda

**Practice Challenge:**
- Trigger Lambda from S3 upload
- Connect Lambda to CloudWatch Logs
- Use Lambda layers for shared code

---

### Exercise 6: VPC (Virtual Private Cloud) - Network Management

**Objective:** Create and configure VPCs, subnets, and security

**Commands:**
```bash
# 1. Create a VPC with CIDR block
aws ec2 create-vpc \
  --cidr-block 10.0.0.0/16 \
  --tag-specifications 'ResourceType=vpc,Tags=[{Key=Name,Value=Training-VPC}]'

# 2. Get VPC ID
VPC_ID=$(aws ec2 describe-vpcs \
  --filters "Name=tag:Name,Values=Training-VPC" \
  --query "Vpcs[0].VpcId" \
  --output text)

echo "VPC ID: $VPC_ID"

# 3. Create public subnet
aws ec2 create-subnet \
  --vpc-id $VPC_ID \
  --cidr-block 10.0.1.0/24 \
  --availability-zone us-east-1a \
  --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=Public-Subnet}]'

# 4. Create private subnet
aws ec2 create-subnet \
  --vpc-id $VPC_ID \
  --cidr-block 10.0.2.0/24 \
  --availability-zone us-east-1b \
  --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=Private-Subnet}]'

# 5. Create Internet Gateway
aws ec2 create-internet-gateway \
  --tag-specifications 'ResourceType=internet-gateway,Tags=[{Key=Name,Value=Training-IGW}]'

IGW_ID=$(aws ec2 describe-internet-gateways \
  --filters "Name=tag:Name,Values=Training-IGW" \
  --query "InternetGateways[0].InternetGatewayId" \
  --output text)

# 6. Attach Internet Gateway to VPC
aws ec2 attach-internet-gateway \
  --internet-gateway-id $IGW_ID \
  --vpc-id $VPC_ID

# 7. Create route table for public subnet
aws ec2 create-route-table \
  --vpc-id $VPC_ID \
  --tag-specifications 'ResourceType=route-table,Tags=[{Key=Name,Value=Public-Route-Table}]'

PUBLIC_RT_ID=$(aws ec2 describe-route-tables \
  --filters "Name=tag:Name,Values=Public-Route-Table" \
  --query "RouteTables[0].RouteTableId" \
  --output text)

# 8. Add route to Internet Gateway
aws ec2 create-route \
  --route-table-id $PUBLIC_RT_ID \
  --destination-cidr-block 0.0.0.0/0 \
  --gateway-id $IGW_ID

# 9. Associate subnet with route table
PUBLIC_SUBNET_ID=$(aws ec2 describe-subnets \
  --filters "Name=tag:Name,Values=Public-Subnet" \
  --query "Subnets[0].SubnetId" \
  --output text)

aws ec2 associate-route-table \
  --subnet-id $PUBLIC_SUBNET_ID \
  --route-table-id $PUBLIC_RT_ID

# 10. List VPCs
aws ec2 describe-vpcs \
  --query "Vpcs[*].[VpcId,CidrBlock,Tags[?Key=='Name'].Value|[0]]" \
  --output table

# Cleanup
aws ec2 detach-internet-gateway --internet-gateway-id $IGW_ID --vpc-id $VPC_ID
aws ec2 delete-internet-gateway --internet-gateway-id $IGW_ID
aws ec2 delete-vpc --vpc-id $VPC_ID
```

**Learning Points:**
- VPC CIDR blocks and subnetting
- Public vs private subnets
- Internet gateways and NAT gateways
- Route tables and routing
- Network architecture best practices

**Practice Challenge:**
- Set up NAT gateway for private subnet internet access
- Create VPC peering between two VPCs
- Configure VPC endpoints for S3

---

## Advanced Topics

### Exercise 7: CloudFormation - Infrastructure as Code

**Objective:** Deploy and manage AWS resources using CloudFormation

**Commands:**
```bash
# 1. Create a simple CloudFormation template
cat > simple-stack.yaml << EOF
AWSTemplateFormatVersion: '2010-09-09'
Description: 'Simple S3 bucket stack'

Resources:
  TrainingBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: training-bucket-12345
      VersioningConfiguration:
        Status: Enabled

Outputs:
  BucketName:
    Description: Name of the S3 bucket
    Value: !Ref TrainingBucket
EOF

# 2. Validate the template
aws cloudformation validate-template --template-body file://simple-stack.yaml

# 3. Create the stack
aws cloudformation create-stack \
  --stack-name training-stack \
  --template-body file://simple-stack.yaml \
  --capabilities CAPABILITY_IAM

# 4. Describe stack events
aws cloudformation describe-stack-events \
  --stack-name training-stack \
  --query "StackEvents[*].[Timestamp,ResourceStatus,ResourceType,LogicalResourceId]" \
  --output table

# 5. Wait for stack creation
aws cloudformation wait stack-create-complete --stack-name training-stack

# 6. Get stack outputs
aws cloudformation describe-stacks \
  --stack-name training-stack \
  --query "Stacks[0].Outputs" \
  --output table

# 7. Update the stack (modify template)
aws cloudformation update-stack \
  --stack-name training-stack \
  --template-body file://simple-stack.yaml

# 8. Delete the stack
aws cloudformation delete-stack --stack-name training-stack
```

**Learning Points:**
- Infrastructure as Code principles
- CloudFormation template structure
- Stack lifecycle management
- Template validation and debugging
- Best practices for production CloudFormation

**Practice Challenge:**
- Create a multi-tier web application with CloudFormation
- Use CloudFormation parameters and conditions
- Implement stack exports and imports

---

### Exercise 8: Automation and Scripting

**Objective:** Create shell scripts to automate AWS operations

**Commands:**
```bash
# 1. Create a backup script for S3
cat > s3_backup.sh << 'EOF'
#!/bin/bash
SOURCE_BUCKET=$1
BACKUP_BUCKET=$2
DATE=$(date +%Y%m%d)

if [ -z "$SOURCE_BUCKET" ] || [ -z "$BACKUP_BUCKET" ]; then
    echo "Usage: $0 <source-bucket> <backup-bucket>"
    exit 1
fi

echo "Starting backup from $SOURCE_BUCKET to ${BACKUP_BUCKET}/${DATE}..."

aws s3 sync \
    "s3://${SOURCE_BUCKET}/" \
    "s3://${BACKUP_BUCKET}/${DATE}/" \
    --metadata-directive COPY \
    --storage-class STANDARD_IA

if [ $? -eq 0 ]; then
    echo "Backup completed successfully!"
else
    echo "Backup failed!"
    exit 1
fi
EOF

chmod +x s3_backup.sh

# 2. Create EC2 inventory script
cat > ec2_inventory.sh << 'EOF'
#!/bin/bash
echo "===== EC2 Instance Inventory ====="
echo ""

aws ec2 describe-instances \
  --query "Reservations[*].Instances[*].[InstanceId,InstanceType,State.Name,PrivateIpAddress,PublicIpAddress,Tags[?Key=='Name'].Value|[0]]" \
  --output table

echo ""
echo "===== Security Group Summary ====="
aws ec2 describe-security-groups \
  --query "SecurityGroups[*].[GroupId,GroupName,Description]" \
  --output table
EOF

chmod +x ec2_inventory.sh

# 3. Create cost monitoring script
cat > cost_check.sh << 'EOF'
#!/bin/bash
START_DATE=$(date -d "1 day ago" +%Y-%m-%d)
END_DATE=$(date +%Y-%m-%d)

echo "Checking costs from $START_DATE to $END_DATE..."
aws ce get-cost-and-usage \
  --time-period Start=$START_DATE,End=$END_DATE \
  --granularity DAILY \
  --metrics "BlendedCost" "UnblendedCost" \
  --output json | jq '.ResultsByTime[] | {Date: .TimePeriod.Start, Cost: .Total.BlendedCost.Amount}'
EOF

chmod +x cost_check.sh

# Test the scripts
./ec2_inventory.sh
```

**Learning Points:**
- Shell scripting for AWS automation
- Error handling in scripts
- Using AWS CLI in bash scripts
- Parsing JSON output with jq
- Scheduling scripts with cron

**Practice Challenge:**
- Create a script that backs up EC2 snapshots older than 7 days
- Build a health check script for your resources
- Automate security group audits

---

### Exercise 9: JMESPath Queries - Advanced Data Filtering

**Objective:** Master JMESPath for extracting and filtering AWS CLI output

**Commands:**
```bash
# 1. Basic query examples
aws ec2 describe-instances \
  --query "Reservations[*].Instances[*].[InstanceId,InstanceType,State.Name]" \
  --output table

# 2. Filter running instances only
aws ec2 describe-instances \
  --query "Reservations[?Instances[0].State.Name=='running'].Instances[*].[InstanceId,InstanceType]" \
  --output table

# 3. Get unique instance types
aws ec2 describe-instances \
  --query "Reservations[*].Instances[*].InstanceType" \
  --output text | tr '\t' '\n' | sort -u

# 4. Extract specific fields from complex objects
aws s3api list-buckets \
  --query "Buckets[*].[Name,CreationDate]" \
  --output table

# 5. Count resources
aws ec2 describe-instances \
  --query "length(Reservations[*])" \
  --output text

# 6. Multi-level querying
aws ec2 describe-instances \
  --query "Reservations[*].Instances[*].{ID:InstanceId,Type:InstanceType,Name:Tags[?Key=='Name'].Value|[0]}" \
  --output table

# 7. Aggregations
aws s3api list-objects-v2 \
  --bucket your-bucket \
  --query "{TotalSize:sum(Contents[].Size),ObjectCount:length(Contents)}" \
  --output json

# 8. Conditional filtering
aws iam list-users \
  --query "Users[?CreateDate>='2024-01-01'].{UserName:UserName,Created:CreateDate}" \
  --output table

# 9. Custom output with JMESPath functions
aws ec2 describe-instances \
  --query "Reservations[*].Instances[*].{
    ID:InstanceId,
    Name:Tags[?Key=='Name'].Value|[0],
    Type:InstanceType,
    IP:PrivateIpAddress,
    Age:round((now()-LaunchTime)/86400)
  }" \
  --output table

# 10. Complex nested queries
aws ec2 describe-security-groups \
  --query "SecurityGroups[*].{
    GroupId:GroupId,
    InboundRules:length(IpPermissions),
    OutboundRules:length(IpPermissionsEgress)
  }" \
  --output table
```

**Learning Points:**
- JMESPath syntax and functions
- Filtering and sorting data
- Extracting nested values
- Aggregations and calculations
- Creating readable output

**Practice Challenge:**
- Create a comprehensive inventory query combining EC2, VPC, and security groups
- Calculate total storage used across all S3 buckets
- Find all unencrypted EBS volumes

---

### Exercise 10: Troubleshooting and Debugging

**Objective:** Diagnose and resolve common AWS issues via CLI

**Commands:**
```bash
# 1. Check AWS CLI version and configuration
aws --version
aws configure list
aws sts get-caller-identity

# 2. Enable debug mode
export AWS_CLI_LOG_LEVEL=DEBUG
aws ec2 describe-instances
unset AWS_CLI_LOG_LEVEL

# 3. Verify IAM permissions
aws iam simulate-principal-policy \
  --policy-source-arn arn:aws:iam::ACCOUNT_ID:user/user-name \
  --action-names "s3:GetObject" "s3:PutObject" \
  --resource-arns "arn:aws:s3:::my-bucket/*"

# 4. Check CloudWatch metrics for EC2
aws cloudwatch get-metric-statistics \
  --namespace AWS/EC2 \
  --metric-name CPUUtilization \
  --dimensions Name=InstanceId,Value=i-xxxxx \
  --start-time $(date -u -v-1H +%Y-%m-%dT%H:%M:%S) \
  --end-time $(date -u +%Y-%m-%dT%H:%M:%S) \
  --period 300 \
  --statistics Average

# 5. Troubleshoot Lambda function
aws lambda list-functions \
  --query "Functions[*].[FunctionName,LastUpdateStatus,CodeSize]" \
  --output table

aws lambda get-function --function-name my-function

# 6. Check recent API calls
aws cloudtrail lookup-events \
  --lookup-attributes AttributeKey=ResourceName,AttributeValue=my-instance \
  --max-results 50 \
  --query "Events[*].[EventTime,EventName,Username]" \
  --output table

# 7. Validate CloudFormation template
aws cloudformation validate-template \
  --template-body file://template.yaml

# 8. Check for orphaned resources
aws ec2 describe-snapshots \
  --owner-ids self \
  --query "Snapshots[?VolumeId==null].[SnapshotId,StartTime,VolumeSize]" \
  --output table

# 9. Monitor API rate limits
aws ec2 describe-instances \
  --query "ResponseMetadata.RetryAttempts"

# 10. Get detailed error messages
aws ec2 describe-instance-status \
  --instance-ids i-xxxxx \
  --include-all-instances \
  --output json | jq '.InstanceStatuses[] | {InstanceId, State, SystemStatus, InstanceStatus}'
```

**Learning Points:**
- Using debug modes
- Checking IAM permissions before operations
- Reading CloudWatch metrics and logs
- Tracing API calls with CloudTrail
- Validating templates and configurations
- Identifying orphaned resources

**Practice Challenge:**
- Set up a complete monitoring dashboard using AWS CLI
- Automate finding and cleaning up unused resources
- Create a troubleshooting runbook with CLI commands

---

## Real-World Scenarios

### Scenario 1: Disaster Recovery Setup

**Objective:** Create automated backups and recovery procedures

**Tasks:**
1. Create an EC2 instance with important data
2. Create automated EBS snapshots
3. Test restoring from snapshot
4. Document recovery procedures

**Key Commands:**
```bash
# Create snapshot schedule
aws ec2 create-snapshot \
  --volume-id vol-xxxxx \
  --description "Daily backup $(date +%Y-%m-%d)"

# List snapshots
aws ec2 describe-snapshots \
  --owner-ids self \
  --query "Snapshots[*].[SnapshotId,VolumeId,StartTime,State]" \
  --output table

# Delete old snapshots
aws ec2 delete-snapshot --snapshot-id snap-xxxxx
```

---

### Scenario 2: Cost Optimization

**Objective:** Identify and reduce AWS costs

**Tasks:**
1. Generate cost and usage reports
2. Identify underutilized resources
3. Find unattached EBS volumes
4. Identify idle EC2 instances

**Key Commands:**
```bash
# Get cost breakdown
aws ce get-cost-and-usage \
  --time-period Start=2024-01-01,End=2024-01-31 \
  --granularity MONTHLY \
  --metrics BlendedCost \
  --group-by Type=SERVICE

# Find unattached volumes
aws ec2 describe-volumes \
  --filters Name=status,Values=available \
  --query "Volumes[*].[VolumeId,Size,CreateTime]" \
  --output table

# Find low-utilization instances
aws cloudwatch get-metric-statistics \
  --namespace AWS/EC2 \
  --metric-name CPUUtilization \
  --dimensions Name=InstanceId,Value=i-xxxxx \
  --statistics Average \
  --period 3600 \
  --start-time $(date -u -v-7d +%Y-%m-%dT%H:%M:%S) \
  --end-time $(date -u +%Y-%m-%dT%H:%M:%S)
```

---

### Scenario 3: Security Audit

**Objective:** Audit AWS security settings and configurations

**Tasks:**
1. Review IAM users and access keys age
2. Check for overly permissive security groups
3. Identify publicly accessible resources
4. Review bucket policies

**Key Commands:**
```bash
# Find old access keys
aws iam list-access-keys --user-name user-name
aws iam get-access-key-last-used --access-key-id AKIAxxxxx

# Find publicly accessible security groups
aws ec2 describe-security-groups \
  --filters "Name=ip-permission.cidr,Values=0.0.0.0/0" \
  --query "SecurityGroups[*].[GroupId,GroupName,IpPermissions]" \
  --output json

# Find public S3 buckets
aws s3api list-buckets --query "Buckets[*].Name" --output text | \
  while read bucket; do
    aws s3api get-bucket-acl --bucket $bucket --query "Grants[?Grantee.URI=='http://acs.amazonaws.com/groups/global/AllUsers']" --output text
  done
```

---

## Practice Projects

### Project 1: Build a Static Website Hosting Solution

**Requirements:**
- Create S3 bucket for hosting
- Configure bucket policy for public access
- Set up CloudFront distribution
- Create automation script to sync files
- Implement CI/CD workflow

**Deliverables:**
- Working static website
- Deployment script
- Documentation

---

### Project 2: Create a Multi-Tier Application Infrastructure

**Requirements:**
- VPC with public and private subnets
- Application load balancer
- EC2 instances in target group
- RDS database in private subnet
- Auto Scaling configuration
- All deployed via CloudFormation

**Deliverables:**
- CloudFormation templates
- Deployment guide
- Architecture diagram

---

### Project 3: Implement Automated Backup System

**Requirements:**
- Lambda function to create EBS snapshots
- CloudWatch Events to trigger backups
- S3 bucket for snapshot metadata
- Cleanup script for old snapshots
- Alerting for failures

**Deliverables:**
- Lambda function code
- CloudFormation template
- Monitoring setup

---

## Additional Resources

### Official AWS Documentation
- **AWS CLI User Guide:** https://docs.aws.amazon.com/cli/latest/userguide/
- **AWS CLI Command Reference:** https://docs.aws.amazon.com/cli/latest/reference/
- **AWS Cloud Practitioner Essentials:** https://aws.amazon.com/training/path-cloudpractitioner/
- **AWS Solutions Architect Associate:** https://aws.amazon.com/certification/certified-solutions-architect-associate/

### Hands-On Labs
- **AWS Cloud Quest:** https://aws.amazon.com/training/digital/aws-cloud-quest/
- **AWS Workshops:** https://workshops.aws/
- **AWS Samples:** https://github.com/aws-samples

### Tools to Install
```bash
# AWS CLI
brew install awscli

# jq for JSON parsing
brew install jq

# Terraform (infrastructure as code)
brew install terraform

# AWS CDK
npm install -g aws-cdk

# AWS SAM CLI
brew install aws-sam-cli
```

### Practice Tips
1. **Always Clean Up:** Delete resources when done to avoid unexpected charges
2. **Use Tags:** Tag everything for better organization
3. **Read Documentation:** AWS CLI has excellent inline help: `aws s3 help`
4. **Start Small:** Begin with simple commands and build complexity
5. **Practice Daily:** Consistency is key to mastering the CLI
6. **Join Communities:** AWS user groups, Reddit r/aws, Stack Overflow
7. **Use AWS Free Tier:** Take advantage of AWS free tier limits
8. **Document Learnings:** Keep notes on common commands and patterns

---

## Getting Help

**AWS CLI Built-in Help:**
```bash
aws help
aws s3 help
aws ec2 help
aws ec2 run-instances help
```

**AWS Forums:**
- https://forums.aws.amazon.com/

**Stack Overflow:**
- Tag: aws-cli

**AWS Support:**
- https://console.aws.amazon.com/support/

---

## Next Steps

1. Complete all exercises in this guide
2. Implement the three practice projects
3. Obtain AWS Cloud Practitioner certification
4. Pursue AWS Solutions Architect Associate certification
5. Build a portfolio of AWS projects
6. Contribute to open-source AWS projects
7. Consider AWS Professional-level certifications

---

**Remember:** The key to becoming proficient with AWS CLI is consistent practice and hands-on experience. Start with the basics, gradually increase complexity, and always clean up your resources!

Good luck on your cloud engineering journey! 🚀


