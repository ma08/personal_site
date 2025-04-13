#!/bin/bash
# This script is used to deploy the website to AWS S3 and invalidate the CloudFront distribution
# Relevant only if using the deploy-to-s3.sh script
# Read the .env.template file and create a .env file with the correct values

# Source the needed environment variables
# Assumes that the credentials for `aws` are cached already
source .env
# Build the website
hugo
# Sync the website to the S3 bucket
aws s3 sync public/ s3://$S3_BUCKET_NAME/
# Invalidate the CloudFront distribution
aws cloudfront create-invalidation --distribution-id $CLOUDFRONT_DISTRIBUTION_ID --paths "/*"