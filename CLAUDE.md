# Hugo Website Development Guide

## Build Commands
- Local development: `hugo server` (live reload at http://localhost:1313)
- Local draft preview: `hugo server -D` (includes draft content)
- Production build: `hugo` (outputs to /public directory)

## Content Creation
- Create new post: `hugo new posts/my-post.md`
- Create new page: `hugo new pages/page-name.md`

## Directory Structure
- `/content/` - All site content (posts, pages)
- `/themes/PaperMod/` - Theme files (don't modify directly)
- `/static/` - Static assets (images, downloads)
- `/assets/` - Custom CSS/JS/images (processed by Hugo)

## Style Guidelines
- Use YAML front matter with triple dashes
- Markdown content follows standard Hugo conventions
- File names should use kebab-case (lowercase with hyphens)
- Follow PaperMod theme's structure for custom templates
- Use relative image paths: `![alt](/images/filename.jpg)`

## Configuration
- Settings in `hugo.yaml` at project root
- Follow existing indentation pattern

## URL Redirects (S3-based)
For external URL redirects (e.g., `sourya.co/shortlink` → external site):

### Adding a New Redirect
1. Edit `/scripts/s3-redirect-rules.json`
2. Add a new rule to the `RoutingRules` array:
   ```json
   {
     "Condition": {
       "KeyPrefixEquals": "your-shortlink"
     },
     "Redirect": {
       "Protocol": "https",
       "HostName": "destination-domain.com",
       "ReplaceKeyWith": "path/to/page",
       "HttpRedirectCode": "301"
     }
   }
   ```
3. Run `/scripts/configure-s3-redirects.sh` to apply changes
4. Invalidate CloudFront cache if needed

### Notes
- Redirects are configured at the S3 bucket level
- Uses 301 (permanent redirect) status code for SEO
- Changes require running the configuration script
- CloudFront cache invalidation may be needed for immediate effect