# AWS CLI Automation Scripts

This directory contains useful shell scripts for automating common AWS CLI tasks.

## Scripts

### ec2_inventory.sh
Comprehensive EC2 instance inventory showing:
- All instances with details (ID, type, state, IPs, name)
- Instance summary (total, running, stopped)
- Security groups
- Untagged instances

**Usage:**
```bash
chmod +x ec2_inventory.sh
./ec2_inventory.sh
```

### s3_backup.sh
Automated S3 bucket backup with:
- Date-stamped backup directory
- Progress reporting
- Summary statistics
- Error handling

**Usage:**
```bash
chmod +x s3_backup.sh
./s3_backup.sh source-bucket-name backup-bucket-name
```

### cost_check.sh
AWS cost analysis showing:
- Daily costs for past 7 days
- Costs by service
- Cost optimization suggestions
- Unattached resources
- Old snapshots

**Usage:**
```bash
chmod +x cost_check.sh
./cost_check.sh
```

**Note:** Install `jq` for better JSON formatting:
```bash
brew install jq
```

## Adding Your Own Scripts

Feel free to add more automation scripts here. When creating new scripts:

1. Include a shebang: `#!/bin/bash`
2. Add usage instructions at the top
3. Include error checking
4. Make scripts executable: `chmod +x script.sh`
5. Test thoroughly before production use

## Best Practices

- **Security:** Never commit AWS credentials to these scripts
- **Testing:** Always test scripts in a non-production environment first
- **Logging:** Add logging for debugging and audit trails
- **Error Handling:** Include proper error checking
- **Documentation:** Comment your code
- **Dry Run:** Use `--dry-run` flags when available

## Integration with Cron

These scripts can be scheduled with cron for automation:

```bash
# Edit crontab
crontab -e

# Examples:
# Run EC2 inventory every morning at 8 AM
0 8 * * * /path/to/ec2_inventory.sh >> /var/log/aws_scripts.log 2>&1

# Run S3 backup daily at 2 AM
0 2 * * * /path/to/s3_backup.sh production-bucket backup-bucket

# Run cost check weekly on Mondays
0 9 * * 1 /path/to/cost_check.sh >> /var/log/cost_check.log 2>&1
```

## Example: Create a Custom Script

Here's a template for creating your own script:

```bash
#!/bin/bash
# My Custom AWS Script
# Description of what this script does

set -e  # Exit on error

# Configuration
REGION="${AWS_REGION:-us-east-1}"

# Functions
log_info() {
    echo "[INFO] $1"
}

log_error() {
    echo "[ERROR] $1" >&2
}

# Main logic
main() {
    log_info "Starting script..."
    
    # Your commands here
    aws ec2 describe-instances --region $REGION
    
    log_info "Script completed successfully"
}

# Run main function
main "$@"
```

## Next Steps

1. Customize these scripts for your needs
2. Add error notifications (email, Slack, etc.)
3. Implement comprehensive logging
4. Add CloudWatch metrics for monitoring
5. Create CloudWatch Alarms for failures
6. Document your own scripts
7. Share with your team!

Happy automating! 🚀


