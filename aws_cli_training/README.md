# AWS CLI Training Materials

Welcome to your comprehensive AWS CLI training program! This collection is designed to help you master command-line operations that are essential for AWS Cloud Engineers.

## 📚 What's Included

### Core Documentation
- **AWS_CLI_PRACTICE_GUIDE.md** - Complete practice guide with 10 exercises covering:
  - EC2, S3, IAM, CloudWatch, Lambda, VPC
  - CloudFormation (Infrastructure as Code)
  - Automation & Scripting
  - JMESPath Queries
  - Troubleshooting & Debugging
  - Real-world scenarios
  - 3 comprehensive practice projects

- **quick_reference.md** - Quick reference card with:
  - Most common AWS CLI commands
  - JMESPath query examples
  - Useful one-liners
  - Debugging tips
  - Daily practice commands

- **exercise_checklist.md** - Track your progress through:
  - All 10 core exercises
  - 3 real-world scenarios
  - 3 practice projects
  - Certification prep milestones

### Automation Scripts
Ready-to-use shell scripts in the `scripts/` directory:
- `ec2_inventory.sh` - Comprehensive EC2 instance inventory
- `s3_backup.sh` - Automated S3 bucket backup
- `cost_check.sh` - AWS cost analysis and optimization suggestions

## 🚀 Getting Started

### Prerequisites
Before you begin, ensure you have:
- [ ] An AWS account (you already have this!)
- [ ] AWS CLI installed
- [ ] AWS credentials configured
- [ ] Basic command-line familiarity

### Installation

#### 1. Install AWS CLI
```bash
# macOS with Homebrew
brew install awscli

# Or download from:
# https://aws.amazon.com/cli/

# Verify installation
aws --version
```

#### 2. Configure AWS CLI
```bash
aws configure

# You'll be prompted for:
# - AWS Access Key ID
# - AWS Secret Access Key  
# - Default region name (e.g., us-east-1)
# - Default output format (recommend: json)
```

**Getting AWS Credentials:**
1. Log into AWS Console
2. Go to IAM → Users → Your User
3. Security credentials tab
4. Create access key (choose CLI, SDK, or API access)
5. Save the Access Key ID and Secret Access Key securely

#### 3. Verify Configuration
```bash
aws sts get-caller-identity

# Should show your account ID, user ARN, etc.
```

#### 4. Install Additional Tools (Recommended)
```bash
# jq - for JSON parsing
brew install jq

# Verify
jq --version
```

## 📖 How to Use This Training

### Suggested Learning Path

#### Week 1: Foundations
- [ ] Complete Exercise 0 (Configuration)
- [ ] Complete Exercise 1 (EC2)
- [ ] Complete Exercise 2 (S3)
- [ ] Run `ec2_inventory.sh` to see your resources

#### Week 2: Identity & Monitoring
- [ ] Complete Exercise 3 (IAM)
- [ ] Complete Exercise 4 (CloudWatch Logs)
- [ ] Run `cost_check.sh` to understand your spending

#### Week 3: Advanced Services
- [ ] Complete Exercise 5 (Lambda)
- [ ] Complete Exercise 6 (VPC)
- [ ] Try `s3_backup.sh` for data protection

#### Week 4: Automation & Advanced Topics
- [ ] Complete Exercise 7 (CloudFormation)
- [ ] Complete Exercise 8 (Automation & Scripting)
- [ ] Complete Exercise 9 (JMESPath Queries)
- [ ] Complete Exercise 10 (Troubleshooting)

#### Week 5: Real-World Practice
- [ ] Complete Scenario 1 (Disaster Recovery)
- [ ] Complete Scenario 2 (Cost Optimization)
- [ ] Complete Scenario 3 (Security Audit)

#### Week 6+: Practice Projects
- [ ] Project 1: Static Website Hosting
- [ ] Project 2: Multi-Tier Application
- [ ] Project 3: Automated Backup System

### Learning Tips

1. **Read First, Execute Second**
   - Read through each exercise before running commands
   - Understand what each command does

2. **Start Small**
   - Don't skip exercises
   - Master basics before moving to advanced topics

3. **Experiment**
   - Modify commands to see different outputs
   - Try combining commands
   - Break things (safely!)

4. **Clean Up**
   - Always delete resources when done
   - Monitor your AWS bill
   - Use tags to track training resources

5. **Document Your Learnings**
   - Take notes on commands you use frequently
   - Save your own examples
   - Build your own script library

## 🎯 Certification Path

While this training focuses on practical CLI skills, it aligns with AWS certifications:

### AWS Cloud Practitioner
- **Focus:** Understanding AWS services and billing
- **After Training:** You'll have practical experience with core services
- **Study Time:** 2-4 weeks after completing exercises
- **Cost:** ~$100 USD

### AWS Solutions Architect Associate
- **Focus:** Architecting and deploying applications on AWS
- **After Training:** You'll understand CLI operations for all major services
- **Study Time:** 4-8 weeks after completing all exercises and projects
- **Cost:** ~$150 USD

### Next Steps After Certification
- AWS Solutions Architect Professional
- AWS DevOps Engineer Professional
- AWS Specialty certifications (Security, Networking, etc.)

## 💰 Cost Management Tips

**Important:** Always monitor your AWS spending during training!

### Use AWS Free Tier
- EC2 t2/t3.micro instances (750 hours/month)
- S3 (5 GB standard storage)
- Lambda (1M requests/month)
- CloudWatch (10 custom metrics)
- See full list: https://aws.amazon.com/free/

### Cost Control
```bash
# Set up billing alerts
# Visit: https://console.aws.amazon.com/billing/home

# Check costs daily
./scripts/cost_check.sh

# Tag everything with "Purpose=Training"
aws ec2 create-tags --resources i-xxxxx --tags Key=Purpose,Value=Training

# Use cost allocation tags
aws organizations tag-resource --resource-id o-xxxxx --tags Key=Purpose,Value=Training
```

### Cleanup Script Example
```bash
#!/bin/bash
# Cleanup all training resources

echo "Terminating training EC2 instances..."
aws ec2 describe-instances \
  --filters "Name=tag:Purpose,Values=Training" \
  --query "Reservations[*].Instances[*].InstanceId" \
  --output text | xargs -I {} aws ec2 terminate-instances --instance-ids {}

echo "Deleting training S3 buckets..."
aws s3 ls | grep training | awk '{print $3}' | \
  xargs -I {} aws s3 rb s3://{} --force

echo "Cleanup complete!"
```

## 🛠️ Common Issues & Solutions

### Issue: "Unable to locate credentials"
```bash
# Solution: Configure AWS CLI
aws configure
```

### Issue: "Access Denied"
```bash
# Check your IAM permissions
aws iam list-attached-user-policies --user-name your-username
```

### Issue: "Command not found: aws"
```bash
# Reinstall AWS CLI
brew install awscli
# Or add to PATH in ~/.zshrc or ~/.bash_profile
```

### Issue: "Bucket already exists"
```bash
# S3 bucket names are globally unique
# Choose a different name or add random suffix
```

### Issue: "Rate exceeded"
```bash
# AWS has API rate limits
# Add delays between commands: sleep 1
# Use --max-items to limit results
```

## 📚 Additional Resources

### Official AWS Documentation
- AWS CLI User Guide: https://docs.aws.amazon.com/cli/latest/userguide/
- AWS CLI Command Reference: https://docs.aws.amazon.com/cli/latest/reference/
- AWS Well-Architected Framework: https://aws.amazon.com/architecture/well-architected/

### Hands-On Learning
- AWS Cloud Quest: https://aws.amazon.com/training/digital/aws-cloud-quest/
- AWS Workshops: https://workshops.aws/
- AWS Skill Builder: https://aws.amazon.com/training/skillbuilder/

### Communities & Forums
- r/aws on Reddit: https://reddit.com/r/aws
- AWS Forums: https://forums.aws.amazon.com/
- Stack Overflow (tag: aws-cli)
- AWS Community Builders: https://aws.amazon.com/developer/community/community-builders/

### YouTube Channels
- AWS official channel
- Adrian Cantrill (certification training)
- Stephane Maarek (course content)

## 🎓 Practice Recommendations

### Daily Practice (15-30 minutes)
```bash
# Morning routine
aws sts get-caller-identity
aws ec2 describe-instances --output table
./scripts/ec2_inventory.sh
```

### Weekly Projects (2-4 hours)
- Choose one scenario from the practice guide
- Implement it from scratch
- Document what you learned
- Clean up resources

### Monthly Review (1-2 hours)
- Revisit exercises you struggled with
- Try advanced challenges
- Review your notes
- Plan next learning phase

## 📝 Progress Tracking

Use `exercise_checklist.md` to track your progress. At minimum, you should:
- [ ] Complete all 10 core exercises
- [ ] Complete all 3 scenarios
- [ ] Finish at least 1 practice project
- [ ] Be comfortable with 90% of quick reference commands

## 🤝 Contributing

Found an error or have a suggestion?
- Update the relevant `.md` file
- Share feedback on exercises
- Add your own examples
- Improve the documentation

## ⚠️ Important Notes

1. **Never commit AWS credentials** to version control
2. **Always clean up** resources after practice
3. **Monitor your costs** closely
4. **Read AWS documentation** alongside exercises
5. **Practice regularly** - consistency is key

## 🎉 Success Criteria

You'll know you're ready for a cloud engineering role when you can:
- ✅ Navigate AWS services confidently via CLI
- ✅ Automate repetitive tasks with scripts
- ✅ Troubleshoot issues without the console
- ✅ Understand cost implications of your actions
- ✅ Follow AWS best practices
- ✅ Explain your implementations clearly

## 🚀 Next Steps After Completing Training

1. **Build a Portfolio Project**
   - Create a real application using AWS CLI
   - Document your process
   - Share on GitHub

2. **Get Certified**
   - AWS Cloud Practitioner
   - AWS Solutions Architect Associate

3. **Contribute to Open Source**
   - Find AWS-related projects on GitHub
   - Submit improvements
   - Help others learn

4. **Apply for Jobs**
   - Update your resume
   - Prepare for technical interviews
   - Practice whiteboard problems

5. **Continue Learning**
   - Explore advanced services
   - Learn Infrastructure as Code (Terraform, CDK)
   - Study system design
   - Learn Kubernetes

---

**Remember:** Cloud engineering is a journey, not a destination. Keep learning, keep practicing, and keep building!

Good luck! 🌟

---

**Questions?** Refer to the individual exercise files for detailed instructions and examples.

**Ready to start?** Begin with Exercise 0 in `AWS_CLI_PRACTICE_GUIDE.md`!

