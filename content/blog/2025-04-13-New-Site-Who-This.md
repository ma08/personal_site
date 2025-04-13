---
title: "New site, Who this"
date: 2025-04-13
description: "Hello world"
type: "posts"
---
I'm Sourya and you can read more about me [here](/about). Welcome to the inaugural post of my revamped personal website! In this post, I'll share why I've decided to break my years-long writing hiatus, my struggle with perfectionism, and the technical details of how I built this site. If you've ever found yourself stuck in "posting-paralysis" or hesitant to ship your work, I hope my reflections might resonate with you.

## Posting-Paralysis
I've had posting-paralysis for years - my last blog post was in 2022, and before that, 2017. I've been scribbling in Google Docs, Notion, and tweeting occasionally. Visiting SF for ODF24 rekindled my hacker spirit to tinker and ship quickly.

ODF's weekly updates culture inspired my Daily Updates doc, helping me release the writing handbrake (as Arsene Wenger would say). I've realized writing+posting parallels building+shipping.

{{< figure src="/images/wenger-handbrake.jpg" alt="handbrake" width="50%" align="center" class="responsive-image">}}

While my zero-to-one experience at SkyLink (YC W22) was great, my shipping at Ladduu AI has been inconsistent since creating a multilingual WhatsApp assistant for Indic languages.

Although it's partly circumstantial as I was working weekends and part-time during my SkyLink transition, I also habitually want to perfect things too much before releasing them. Even ChatGPT recently called me out on this while testing its memory feature.
![roasted by ChatGPT!](/images/chatji-roast-overthink.png)

The creation of this personal website + blog is a deep commitment to myself to post more. I don't expect any magic to happen from this but I have seen enough that I can't ignore the power of putting my voice out there. Regular posts will help me have better chain-of-thought based thinking and will also help me connect with the community eventually.

While overcoming my posting-paralysis is a major goal, I've also been reflecting on my actual writing approach and how it connects to my shipping philosophy.

## Writing Style, Error-correction, Beginning of Infinity, Shipping
I realized that my writing style can be incredibly verbose with too much chain-of-thought/tree-of-thoughts journaling. While I appreciate the power of being concise, I have also started to embrace the verbosity in some contexts. LLMs make it way easy to compress a verbose blob of text into a concise one and add structure to it (often surprisingly well) but the opposite might not be true. There is an art to blabbering and I shall keep (f)arting it out until the next error-correction.

I am currently reading _The Beginning of Infinity_ book and the point about error-correction leading to universal intelligence is fascinating. I have taken inspiration from it to embrace being awkward in my writing so that I can correct it after posting (if needed) rather than never posting at all.

I can't stress it enough that the same can be said for building products. Shipping way too late is a standard startup cliche and has been incredibly hard to escape in spite of being fully aware of the cliche.

Now that I've shared my thoughts on writing and shipping, let me walk you through how I actually built this website and what I learned along the way.

## Tech Stack and Process
Jotting down some details of my process of creating this site.
### Framework
I consulted with the trifecta of ChatGPT, Grok, and Claude on how to create a personal website + blog. `hugo` was a top recommendation in all answers which I ended up picking along with the `papermod` theme. 

Other top recommendations:
- `astro`
- `next.js` + `tailwind css`
- `ghost`
- `jekyll`

Grok's recommendation and reasons were pretty convincing.

![grok hugo recommendation](/images/hugo-recommendation-grok.png)

I chose `hugo` because I am indeed a markdown purist and like minimalistic frameworks. The fact that it caters to researchers and AI/ML folks made it even more attractive. I also didn't want to suffer from paralysis through too much research so I went ahead with `hugo` to build something quickly as it ticked many boxes.

### Papermod Hiccup and Resolution
I had an issue with the first build failing due to a fresh `papermod` bug and was able to resolve it by making a [small change](https://github.com/adityatelange/hugo-PaperMod/commit/7153bb83f5bbe22e1746ec2d7f8e54d566e6ccfb) in the `papermod` theme thanks to [this comment](https://github.com/adityatelange/hugo-PaperMod/issues/1719#issuecomment-2797327929).

### Hosting
I am waiting for my application for Vercel for Startups to be processed (a perk through ODF). Therefore, I went ahead with AWS S3 + CloudFront as I had some AWS credits to spare (also thanks to ODF). Claude was terrific in helping me set up the AWS infrastructure and write [the bash script](https://github.com/ma08/personal_site/blob/main/scripts/deploy-to-s3.sh) for the `S3` bucket sync and `CloudFront` invalidation. It was a breeze to setup the infra when compared to the last time I had to do something like this before LLMs were a thing.

```bash
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
aws cloudfront create-invalidation --distribution-id $CLOUDFRONT_DISTRIBUTION_ID --paths "/*"```
```

### Source Code
I am [open-sourcing the source code](https://github.com/ma08/personal_site) for the website + blog for anyone who wants to use it as a starting point for their own thing. I have also included useful notes in the `README.md` and scripts that helped my flow in the `scripts` folder. Feel free to open an issue in the repo if you have any questions or feedback :)

### Tweets Along the Way
Posted some tweets along the way:
#### Snooping on Claude Code

{{< x user="curious_queue"  id="1910734595907322099">}}

#### Rickrolled by AI

{{< x user="curious_queue"  id="1910917670637097430">}}

With the v0 of the site now up and running, there are always improvements to be made.
## Some TODOs for the Website
- [ ] Add tags to the blog posts and create a tag view/page
- [ ] Add a search bar to the blog
- [ ] Add a daily/weekly updates section to the blog
- [ ] Create a Github workflow to automate the website build, sync, and invalidation after a commit to the `main` branch
- [ ] Improve the aesthetics a bit. I have a background style in mind but wasn't able to create the correct SVG images so far. Could be a good eval for LLMs lol.
- [ ] Add a comments section to the blog posts
- [ ] Update/improve the [about page](/about) page
- [ ] Add Google Analytics to the website
- [ ] Add `llms.txt` to the website
- [ ] Add newsletter pipeline (if there is enough demand)

## Fin & Goals for Posting
That's it for now. Wish me luck in improving my posting game. While anything's fair game, here's what I plan to post about:
- Ladduu AI startup journey and product updates/demos
- Tech learnings and reflections
- Regular weekly/daily updates 

Respect to you if you made it this far :) Thanks for reading!