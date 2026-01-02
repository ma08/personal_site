#!/bin/bash
# This script configures S3 redirect rules for the static website
# Run this whenever you add new redirects to s3-redirect-rules.json

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# Source environment variables
if [ ! -f "$PROJECT_ROOT/.env" ]; then
    echo "Error: .env file not found at $PROJECT_ROOT/.env"
    echo "Please create one based on .env.template"
    exit 1
fi

source "$PROJECT_ROOT/.env"

# Check if S3_BUCKET_NAME is set
if [ -z "$S3_BUCKET_NAME" ]; then
    echo "Error: S3_BUCKET_NAME is not set in .env file"
    exit 1
fi

# Check if redirect rules file exists
REDIRECT_RULES_FILE="$SCRIPT_DIR/s3-redirect-rules.json"
if [ ! -f "$REDIRECT_RULES_FILE" ]; then
    echo "Error: Redirect rules file not found at $REDIRECT_RULES_FILE"
    exit 1
fi

echo "Configuring S3 redirect rules for bucket: $S3_BUCKET_NAME"
echo "Using redirect rules from: $REDIRECT_RULES_FILE"

# Apply the redirect rules to the S3 bucket
aws s3api put-bucket-website \
    --bucket "$S3_BUCKET_NAME" \
    --website-configuration "file://$REDIRECT_RULES_FILE"

if [ $? -eq 0 ]; then
    echo "✓ Successfully configured S3 redirect rules"
    echo ""
    echo "Note: If you're using CloudFront, you may need to invalidate the cache:"
    echo "  aws cloudfront create-invalidation --distribution-id \$CLOUDFRONT_DISTRIBUTION_ID --paths \"/*\""
else
    echo "✗ Failed to configure S3 redirect rules"
    echo "Make sure your AWS credentials are configured and you have permission to modify the S3 bucket"
    exit 1
fi
