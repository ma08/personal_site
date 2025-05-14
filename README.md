# Sourya Kakarla - Personal Website

This repository contains the source code for my personal website: [sourya.co](https://sourya.co).

## Local Development

Best to refer to the [PaperMod documentation](https://github.com/adityatelange/hugo-PaperMod) for the most up-to-date instructions.

I use a fork of the PaperMod theme with some customizations (mainly to fix some bugs and custom features); you can find the fork [here](https://github.com/ma08/hugo-PaperMod). You can look at the [diff/commits](https://github.com/adityatelange/hugo-PaperMod/compare/master...ma08:hugo-PaperMod:master) to see the changes I made.


1. Start ngrok: `./scripts/run-ngrok.sh`
2. Start Hugo server: `./scripts/run-local.sh`


## Scratchpad for Useful Commands

### Remove public folder from version control and force push
```bash
echo "public/" >> .gitignore && git rm -r --cached public/ && git add .gitignore && git commit -m "Remove public folder from version control" && git push --force
```

### AWS S3 Bucket Creation
```bash
S3_BUCKET_NAME=<bucket-name>
AWS_REGION=<region>
aws s3 mb s3://$S3_BUCKET_NAME --region $AWS_REGION
aws s3 website s3://$S3_BUCKET_NAME --index-document index.html --error-document error.html
aws s3 sync public/ s3://$S3_BUCKET_NAME/ --acl public-read
aws s3api put-bucket-policy --bucket $S3_BUCKET_NAME --policy file://bucket-policy.json
aws s3 website s3://sourya.co --index-document index.html --error-document error.html
```