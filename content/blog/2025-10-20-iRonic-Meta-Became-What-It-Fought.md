---
title: "iRonic: Meta Became What It Fought"
date: 2025-10-19
description: "WhatsApp’s new Business API rules banning general-purpose AI assistants reveal Meta’s Apple-like turn. This blog post discusses the news, Meta's reasoning, recent history of platform controls, and how this affects early-stage startups."
type: "posts"
---
## The News

Meta [updated its WhatsApp Business Solution Terms](https://www.whatsapp.com/legal/business-solution-terms/) on October 15, 2025 to ban general-purpose AI assistants from using the Business API.
- This is immediately applicable for any users signing up on or after October 15, 2025.
- If already a user, it comes into effect on January 15, 2026.

{{< figure src="/images/2025-10-19-Journey-To-Zone/whatsapp-ai-provider-ban.png" alt="AI Assistants' ban in WhatsApp Business API Terms" caption="The new 'AI Providers' section in the [updated WhatsApp Business API Terms](https://www.whatsapp.com/legal/business-solution-terms/preview)" >}}

This will most likely affect all the AI assistant players in the market like **[ChatGPT](https://x.com/OpenAI/status/1980794846752436597), [Perplexity](https://x.com/AravSrinivas/status/1979571330535362641), [Poke](https://x.com/marvinvonhagen/status/1979691404415926764)**, etc., who already have a WhatsApp integration for their product.

## Meta's Reasoning
{{< figure src="/images/2025-10-19-Journey-To-Zone/rationale-tech-crunch.png" alt="Rationale from TechCrunch" caption="Why Meta says it's banning AI assistants from WhatsApp Business API (as per [the TechCrunch article](https://techcrunch.com/2025/10/18/whatssapp-changes-its-terms-to-bar-general-purpose-chatbots-from-its-platform/))" >}}

Meta's rationale that "new chatbot use cases placed a lot of burden on its system with increased message volume and required a different kind of support" is mostly a facade. Surely, there's at least some element of blocking Meta AI's competitors from the platform. It feels like a PR-vetted excuse to justify the decision.

It's also amusing that the presence of their very own Meta AI in WhatsApp kind of validates that their systems can handle such chatbot use cases.

I didn't really understand the "built the API for business-to-business use cases" part at first. What does that mean? Maybe they meant the ["trusted WhatsApp partner"](https://business.facebook.com/messaging/partner-showcase/?ref=WAB_PLATFORM_PRICING) thing. If so, what if someone builds a WhatsApp integration for their AI assistant using these partners?

It also raises an interesting question: if an AI assistant doesn't provide any physical goods, can it never be a "business" according to Meta's definition? What if:
- it provides a tailored service like tutoring students? 
- it is much better in providing personal assistance in particular languages and regions, by having better multilingual performance and/or regional integrations?
    - It's worth noting that Meta AI is still quite poor in many regional languages. I was surprised to see how bad it was in Hindi and Telugu (Indic languages I could personally test it out on), given that India is one of the largest markets for WhatsApp. 
    - Even basic audio message transcription doesn't currently support Indian languages.


It's sad that the creator of Llama, the first popular open-weights LLM, is now resorting to cold platform-locking tactics, cutting off billions of WhatsApp users from using alternatives to Meta AI that are often better for specific contexts and use cases.

This is especially impactful because there is a large segment of people in regions like India for whom smartphone use is synonymous with WhatsApp use for the most part. Companies were able to build products and unique experiences and meet users where they are using the WhatsApp Business API.

With this change, those users have no choice but to keep using Meta AI in WhatsApp or become comfortable with installing new apps to access an alternative AI assistant (maybe that's a good thing if a competitor can drive adoption by just being very good and easy to use). I hope Meta allows some discretion to products that showcase the value proposition beyond being a vanilla alternative to Meta AI.


## The Meta(pple)
Meta has long been known for taking up a fight against Apple for placing too many platform restrictions on its products and services. Zuckerberg hasn't been shy about being "the rebel" against Apple's platform restrictions. Of course, he might have eventually realized that there isn't much they could do about it (at least legally). It turns out what they realized was that they could do the same for the platforms they owned.

{{< figure src="/images/2025-10-19-Journey-To-Zone/Meta-vs-Apple.webp" alt="Meta vs. Apple rivalry" caption="Meta vs. Apple rivalry ([Source](https://appleworld.today/2024/12/apple-says-meta-platforms-wants-too-much-access-to-its-software-tools/))" >}}

Here's a brief timeline of the key events:
### 2010–2011: Apple sets the “no third‑party layers” doctrine
> "We know from painful experience that letting a third party layer of software come between the platform and the developer ultimately results in sub‑standard apps." - [Steve Jobs' open letter Thoughts on Flash (2010)](https://www.pomagalnik.com/wp-content/uploads/2021/01/Thoughts-on-Flash.pdf)

Although this isn't directly related to Meta, this tight curation lays the baseline for App Store controls and restrictions.
### 2018: Cambridge Analytica fallout turns into a public war of words
> “I wouldn’t be in this situation.” - [Tim Cook when asked what he’d do if he were Zuckerberg](https://www.vox.com/2018/4/6/17206532/transcript-interview-apple-tim-cook-msnbc-kara-swisher)

> "extremely glib and not at all aligned with the truth." - [Mark Zuckerberg shot back regarding Tim Cook's view](https://www.vox.com/technology/2018/4/2/17183708/mark-zuckerberg-facebook-tim-cook-apple)

### 2018–2019: Apple clamps down on Facebook’s data‑collection work‑arounds
[Apple forced Facebook to remove Onavo](https://www.wsj.com/articles/facebook-to-remove-data-security-app-from-apple-store-1534975340) from the App Store over data‑collection violations (2018), then revoked Facebook’s enterprise certificates after TechCrunch revealed the “Facebook Research” sideloaded app that paid users for deep device data (2019). Internal iOS apps at Facebook briefly stopped working.


### 2020: App Store fees collide with Facebook’s pandemic “Paid Online Events.”
> "We’re standing up to Apple for small businesses everywhere" — [Facebook’s newspaper ad (Dec 2020)](https://www.theverge.com/2020/12/16/22178068/facebook-apple-newspaper-ads-ios-privacy-changes)

[Facebook publicly asked Apple](https://about.fb.com/news/2020/08/paid-online-events) to waive its 30% cut or allow Facebook Pay; Apple initially refused, then granted a temporary waiver through year‑end 2020.

### 2020: Facebook Gaming meets iOS policy walls.
> "Apple has a unique stranglehold as a gatekeeper… blocks innovation… and charges monopoly rents." - [Mark Zuckerberg (Aug 2020, internal meeting)](https://9to5mac.com/2020/08/28/mark-zuckerberg-apple-monopoly/)

[Apple repeatedly rejected the Facebook Gaming app](https://www.theverge.com/2020/8/7/21358355/facebook-apple-app-store-policies-comments-facebook-gaming-ios) unless Facebook removed built‑in HTML5 games; the iOS app launched without games. Cloud gaming features were also blocked under Apple’s “no app stores within apps” rule.

### 2020–2021: App Tracking Transparency (ATT) is the big rupture.
> "Apple has every incentive to use their dominant platform position to interfere with how our apps work."  - [Mark Zuckerberg (Jan 2021 earnings call)](https://www.fool.com/earnings/call-transcripts/2021/01/28/facebook-fb-q4-2020-earnings-call-transcript/)
Apple’s iOS 14.5 tracking prompts limited cross‑app tracking (IDFA). Meta later estimated the impact at about $10B in 2022.

### 2022: Apple expands fees to "boosted posts."
[Apple clarified that “boosts” in social apps](https://www.theverge.com/2022/10/25/23423637/apple-app-store-tax-boosted-social-media-posts) are in‑app purchases subject to the 30% cut; Meta called the move Apple “undercutting others.” In 2024, Meta began passing the fee on to advertisers buying boosts in the iOS apps and steered users to the web to avoid it.

### 2023: Vision Pro & the “open vs. closed” narrative
> "It could be the vision of the future of computing, but… it’s not the one that I want." - [Mark Zuckerberg on Vision Pro (2023)](https://www.theverge.com/2023/6/8/23754239/mark-zuckerberg-meta-apple-vision-pro-headset) when speaking with Meta employees after Apple unveiled Vision Pro.

### 2024: EU DMA pressure on Apple’s App Store rules
[Spotify and others (often aligned with Meta’s policy posture) attacked Apple’s DMA “compliance”](https://techcrunch.com/2024/01/26/spotify-calls-apples-dma-compliance-plan-extortion-and-a-complete-and-total-farce) and new EU‑only “core technology fee” as anti‑competitive.

### 2025: Early DMA enforcement hits both companies.
[The European Commission fined](https://www.reuters.com/sustainability/boards-policy-regulation/apple-fined-570-million-meta-228-million-breaching-eu-law-2025-04-23) Apple €500m for anti‑steering in the App Store and fined Meta €200m over its “Consent or Pay” model, showing regulators see gatekeeping risks on both sides.


The latest WhatsApp Business API terms update seems like a classic case of "the bullied becomes the bully." Meta's claims of nurturing open ecosystems will surely invite "press X to doubt" feelings with this news, and the trend might only get worse from here.


## Platform Gates Be Closing

This isn’t just Apple vs. Meta. There have been at least two other recent cases of major platforms closing the gates.

### (Jan 2023) Twitter
[In 2023, Twitter banned](https://www.theverge.com/2023/1/19/23562947/twitter-third-party-client-tweetbot-twitterific-ban-rules) third-party clients and pushed developers to paid API tiers, explicitly forbidding apps that mimic its own.

### (June 2023) Reddit
[Reddit likewise moved to paid APIs](https://www.reddit.com/r/reddit/comments/145bram/addressing_the_community_about_changes_to_our_api) and watched beloved clients shut down after CEO Steve Huffman said the API “was never designed to support third-party apps” and that Reddit could no longer “subsidize” large-scale commercial use.

It’s the same playbook: rein in third-parties, put a meter on data, and privilege the first-party experience. As data has become the fossil fuel driving the LLM economy, this is not very surprising, given that these platforms have had enough time to reach maturity, where monetization priorities overtake growth channels.

## How this affects me as a founder

### The WhatsApp Pet Project
We built an AI assistant for WhatsApp as a weekend pet project in January 2023 and had it live on a "production-ish" server by March 2024, a few months before [Meta AI launched in India](https://about.fb.com/news/2024/06/meta-ai-arrives-in-india-leading-ai-assistant-now-at-your-fingertip). It supported eight Indian languages, where users could send audio messages in their native language and get responses in the same language. It was multimodal, supporting images, and could gather context from YouTube videos too.

{{< figure src="/images/2025-10-19-Journey-To-Zone/ladduu-meta-whatsapp-manager.png" alt="Ladduu AI's Meta Accounts" caption="Ladduu AI's WhatsApp accounts with dates (test account in Dec 2023 and the prod one in Mar 2024)" >}}

Given the novelty at that time, it received organic traction of thousands of users within the span of a few weeks.

#### Pet Project Origins
This pet project was born out of our passion for conversational AI as a way to help people overcome language and tech‑savviness barriers when using smartphone‑enabled services. It was mainly built for my father initially as he wanted to use his smartphone more in his daily life but couldn't due to a lack of tech‑savviness and some language barriers, so he often reached out to me for help placing orders on Amazon, taking care of utility bills, booking travel, etc. At this time, I was the Founding ML Engineer at SkyLink (YC W22). My experience with agent orchestration at SkyLink made me itch to solve this problem with a multilingual twist on WhatsApp for him.

My partner (Radha Jagarlamudi) and I are co-founders turned life partners. She started a rural-tech startup in India around the Covid times, where she wanted to build a rural version of TaskRabbit/UrbanClap as there was a severe shortage of skilled workers in rural areas. Through speaking with hundreds of rural families, she realized that although people had smartphones and purchasing capability, they were often not tech-savvy or comfortable enough with English to do more beyond **browsing YouTube and using WhatsApp**.


{{< figure src="/images/2025-10-19-Journey-To-Zone/ladduu-start-me-up-columbia.png" alt="Ladduu's Start Me Up Bootcamp at Columbia University (2022 Summer)" caption="Slide from Start Me Up Bootcamp at Columbia University (2022 Summer)" >}}

#### Betting on Conversational AI in 2021 before LLM Hype
As we started working together in mid-2021, we realized that just building a new service provider app wouldn't cut it. We had to solve the "last mile" problem of how to make people use the service. That's when our interest in conversational AI to solve this problem was born.

**We are proud to say that our interest was born of our drive to solve a problem we witnessed intimately rather than jumping on the LLM hype bandwagon that started when ChatGPT launched in 2022.**

I pursued research at Columbia University specializing in low‑resource Speech & NLP. During that time, we took part in the Start Me Up Bootcamp at Columbia University (2022) and pitched a conversational interface with agentic capabilities and multilingual support.

{{< figure src="/images/2025-10-19-Journey-To-Zone/ladduu-fast-pitch.png" alt="Slide from Ladduu's fast pitch entry (Nov 2022)" caption="Slide from Fast Pitch at Columbia University (Nov 2022)" >}}

While this may be super salesy (well, some of it is), I shared all this to highlight the context of why building on top of WhatsApp was important for us.


### Why WhatsApp?
Hope this has become obvious by now. But just to reiterate, through our roots in rural India, and having spoken with hundreds of rural families, we knew that WhatsApp is often the only medium to meet many users where they are without overwhelming them with a complex app. It provided the least friction.

We even tested an integration with redBus, a popular bus ticket booking platform in India, and it was a success.

### Why we didn't count on WhatsApp
While being able to reach many underserved users through WhatsApp was a huge win, there were still a lot of technical and business challenges.
The major ones:
- The need to use template messages when initiating outside the 24‑hour customer service window.
- The need to integrate with APIs/browser use at the backend, with limited on-device capabilities.
- No good official way to provide ambient intelligence using a background agent that listens to communication between two or more users. WhatsApp doesn't allow such business accounts to be added to groups.
- Last but not least, it didn't feel like a good long-term strategy to count on a platform that can change its terms at any time, given what Meta faced with Apple. iRonic indeed!

Therefore, overall, we decided to have WhatsApp as one of the modalities, but not the primary one.

*Full Disclosure:* The concern about WhatsApp pulling surprising changes was mainly raised by Radha. It was fun receiving the "told you so" moment when the recent news came out.


### What we did instead
Driven by concerns that WhatsApp is not a reliable platform to build on, we transitioned into building our own apps on Android (unreleased prototype) and iOS. 
Of course, the OS-level restrictions and limitations that apps are subject to are still a challenge to provide end-to-end assistive solutions, but it is a start.

#### Insights from the journey
This journey that began with building an AI assistant for senior citizens yielded many insights (often discovered the hard way) that made us converge on focusing on human-to-human interactions and using ambient intelligence to help get things done. Sharing some of the insights here:
- **Overwhelm for Seniors**: Even if a conversational AI agent is able to execute actions in users' native language, it is still overwhelming for a large number of senior users. We verified this with prototype apps on Android and iOS.
- **Love is all we need**: It's not only about getting things done. *What's of greater significance often is the feeling of connecting with a loved one.* My father doesn't text me just for the Amazon order. It's kind of his love language to be in touch with me too. Even if he learned to do it himself using an AI assistant, he might still prefer to get things done with help from me as it makes him feel cared for.
- **Cognitive Overload for Tech-Savvy Professionals**: While seniors face problems using tech-enabled services and may lack emotional support due to often living far away from their children, working professionals face problems of cognitive overload due to hectic professional lives, especially for parents with young children when both partners are working.
- **Context Challenges due to Platform Restrictions**: Both the mobile operating systems (like Android and iOS) and existing messaging platforms like WhatsApp and iMessage make it pretty much impossible to build a separate intelligent assistive layer.
- **AI Assistant Interaction Tax**: Building a separate AI assistant that the user has to interact with often demands a lot in terms of time spent interacting with the AI assistant and remembering when to interact with it to stay on top of things, adding to the cognitive overload. We saw this as a tax because existing systems like messaging, calendar, and email already contain enough context for an intelligent assistant to figure out most things without manual intervention. Only when the assistant is proactive are true convenience and cognitive-load relief viable.
- **Personal texts are where life happens**: Personal texts in WhatsApp/iMessage have the most context regarding our lives but are not accessible to third-party apps. There are some hacks one can use, but nothing official that can reach consumers at scale. While it's definitely an uphill task to drive adoption of a new platform, we found conviction in the user experience we could deliver long term.


#### Zone Text - Ambient Intelligence
All these insights led us to building [Zone Text](https://trymyzone.com/): it's a personal platform for communication, coordination, organization, and legacy. The [iOS app](https://apps.apple.com/us/app/zone-text/id6743241404) is already out. I will save the full story about this journey for my next post. Thanks for reading!
