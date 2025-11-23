#!/bin/bash
# S3 Backup Script
# Syncs source bucket to backup bucket with date stamp

# Check arguments
if [ -z "$1" ] || [ -z "$2" ]; then
    echo "Usage: $0 <source-bucket> <backup-bucket>"
    exit 1
fi

SOURCE_BUCKET=$1
BACKUP_BUCKET=$2
DATE=$(date +%Y%m%d-%H%M%S)
BACKUP_PATH="${BACKUP_BUCKET}/backup-${DATE}/"

echo "====================================="
echo "       S3 Backup Script              "
echo "====================================="
echo "Source: s3://${SOURCE_BUCKET}"
echo "Destination: s3://${BACKUP_PATH}"
echo "Started: $(date)"
echo ""

# Check if source bucket exists
if ! aws s3 ls "s3://${SOURCE_BUCKET}" &>/dev/null; then
    echo "Error: Source bucket '${SOURCE_BUCKET}' not found!"
    exit 1
fi

# Perform backup
echo "Starting backup..."
aws s3 sync \
    "s3://${SOURCE_BUCKET}/" \
    "s3://${BACKUP_PATH}" \
    --metadata-directive COPY \
    --storage-class STANDARD_IA \
    --delete \
    --exclude "*.tmp" \
    --exclude "*.log"

if [ $? -eq 0 ]; then
    echo ""
    echo "====================================="
    echo "Backup completed successfully!"
    echo "Completed: $(date)"
    echo "Backup location: s3://${BACKUP_PATH}"
    echo "====================================="
    
    # Get backup summary
    echo ""
    echo "Backup Summary:"
    aws s3 ls "s3://${BACKUP_PATH}" --recursive | \
        awk '{total+=$3} END {print "Total files:", NR, "\nTotal size:", total, "bytes"}'
else
    echo ""
    echo "Error: Backup failed!"
    exit 1
fi


