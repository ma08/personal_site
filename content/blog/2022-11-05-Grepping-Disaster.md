---
title: "Grepping Disaster"
date: 2022-11-05
description: "TLDR; Recovered data from a disaster using grep."
type: "posts"
tags: ["programming", "unix", "data-recovery"]
slug: "grepping-disaster"
---

TLDR; Recovered data from a disaster using grep.

Few weeks back, I accidentally **destroyed** my main programming directory by running `"rm -rf *"` in the wrong directory as I forgot to `"cd"` after running `"mkdir"`. This was working on the last stage of organizing the code submission for a security conference.

I only heard legends about stuff like this happening (e.g: doing `"rm -rf ~"`) to unix folks on r/programming. Fortunately, I source version most of my code and dotfiles using git. BUT I didn't commit and push the code that I am working on for my MS thesis @ Columbia.

I knew I was doomed as I haven't setup a trash option or a safety alias for rm even though I read frequently about having that safety net when browsing stackexchange. As I sheepishly launched the inevitable googlefu, the sense of doom intensified as most answers talked about implementing the safety net than an attempt at recovering deleted data when there's none.

Finally, I found [this gem of an answer](https://askubuntu.com/questions/3883/how-to-recover-deleted-files/3912#3912) which suggested to use in the disk partition

```bash
grep "<a string I knew from the file that I am trying to bring back to life>"
```

![grep to the rescue!](/images/grep-save-rm-rf.jpeg) 

After a bit of trial and error, I was **able to recover ALL of my thesis code**. I probably lost some data which I might need sometime later yet insanely relieved that all of my crown jewels are safe. I am not exactly sure why it worked as of now; my best guess is text editors maintain temp files and grep was used to search and recover from them.

Feels silly yet somewhat proud to go through this right of passage. Make sure to backup periodically folks! And alias your commands!!
