<div id = "chart">
<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/4.2.2/d3.min.js"></script>
<script src="visualisation.js"></script>
</div>

*Need to add a TLDR; do so at the end*
# Exploring the Jungle of r/WSB

## Context

Over the last 12 months, there has been a seismic increase in followers of the Reddit community (known as a *subreddit*) [r/WallStreetBets](https://reddit.com/r/wallstreetbets) (henceforth referred to as r/WSB). As a group of retail investors (but each operating on their own accord), these followers collectively invested in stocks on the US market, coordinating through Reddit forums. This subreddit has amassed over 11 million followers since its creation on January 31st 2012, with the vast majority (9.5 million) having joined in 2021. 

|Number of Followers (Members) to Reddit community r/wallstreetbets: A rapid increase since 2021|
|:--:| 
|![Image1](https://i.ibb.co/cx5jTqq/newplot.png)|

Since the recent surge in followers, r/WSB has taken interest in many high- and low-profile stocks. Initially (and most famously), they advocated for investments in [GameStop](https://finance.yahoo.com/quote/GME). As a brick-and-mortar retailer of gaming electronics and merchandise, the company seemed destined for failure. Institutional investors, primarily hedge funds, had heavily shorted the stock to profit off of declining sales and profits. Then, hundreds of thousands of enthusiastic comments and posts about GameStop were shared on r/WSB, causing retail investors fuelling a short-squeeze as hedge funds were forced to cover their losses. The stock price had increased by several multiples, and Wall Street suffered billions in losses. The Financial Times covered it in further detail [here](https://www.ft.com/content/47e3eaad-e087-4250-97fd-e428bac4b5e9).

The craze behind GameStop was not isolated. r/WSB had indulged in several other companies - [AMC Entertainment Holdings](https://finance.yahoo.com/quote/AMC), [Nokia](https://finance.yahoo.com/quote/NOK/) and [Sundial Growers](https://finance.yahoo.com/quote/SNDL/) to name a few. Observing these trends, we were intrigued as to how a collective group of retail investors was able to rattle the financial industry despite competing against financial professionals with access to a vast amount of information and capital. Additionally, we saw that many of these investors were pouring significant sums of money, including their life savings, into  companies advocated for on the platform. These investments are often unconventional and against the advice of financial professionals and ratings firms.

And thus we wanted to know: Who's right? Are r/WSB investors throwing their money away or have they proved institutional investors wrong? Are they sensible or irrational? To answer this, we needed to do a deeper analysis of the r/WSB community, to understand what is being said on these forums and the stocks that they are advocating for to identify patterns and performance trends.

|Redditors have invested vast sums based on advice from r/WSB|
|:--:| 
|![Image2](https://github.com/prakritj/ds105_wsb/blob/gh-pages/PNG%20image.png)|

## Getting our Data

To analyse data from r/WSB, the natural first step would be to retrieve this from Reddit. However, due to the nature of social media posts and comments, as well as the vastness of these forums, we had to carefully choose our set of data to analyse before we and our machines get overwhelmed.

### What Data do we Want?

As with any subreddit, there is a wide variety of posts and comments on r/WallStreetBets, including images, gifs and videos. Around 1000 submissions were posted per day on r/WSB in 2021, and each submission contained several thousand comments. The numbers add up quick. 

To limit our dataset to a manageable size while covering discussions during a decently lengthy period, we opted to only analyse comments from daily discussion threads. Since comments on Reddit were only text (at the time of our analysis), this made it much simpler to use commonly applicable text analysis techniques to our data. Additionally, these posts have a significant number of comments (~10,000) each day. We would still have plenty of data to work with.

**Time Period**

Based on r/WSB's meteoric rise in the beginning of 2021, we thought it most appropriate to analyse comments from the first half of 2021 (Jan 1 to Jun 30). This ensures we cover comments from a time of peak popularity on the community, but also allows us to run a retrospective analysis on how well these companies have performed in the months after discussions had occurred.

### Obtaining Data

We opted to use Python to obtain and analyse data, and used [PRAW](https://praw.readthedocs.io/en/stable/), a wrapper for the Reddit API, to get our data from Reddit. PRAW is extremely easy to use, automatically handling request limits while following all of Reddit's API rules (and thus not jeopardising our Reddit Dev account). The documentation is elaborate and well-written. Most conveniently, PRAW stores post and comment data in objects with attributes, allowing us to easily store and manipulate them later on without losing or cluttering our datasets. We then stored these objects in Pandas Dataframes so we could easily organise, filter, and iterate over them.

**Too Many Comments**

One limitation

## Analysing our Data

### Overview

**Statistical Summary**
*how many comments collected, how many posts collected, total upvotes, average upvotes, etc.*

|  | **Count** |
| --- | ---: |
| **Posts** | 130 |
| **Total Posts Score** | 178,323 |
| **Average Post Score** | 1,372 |
| **Total Comments** | 3,597,073 |
| **Average Comments per Post** | 27,670 |
| **Comments Pulled** | 92,379 | 
| **Total Score of Comments Pulled** | 2,202,633 |
| **Average Score of Comments Pulled** | 23.84 |


**Sentiment Analysis and Distribution**
To start off, we wanted to observe how r/WallStreetBets felt about their internet decisions overall, as people often make posts or comments describing their huge losses or gains. To do this, we used the AFINN sentiment lexicon, a list of English words manually rated for valence with an integer between -5 (negative) and +5 (positive). [Corpus Text, 2021](http://corpustext.com/reference/sentiment_afinn.html)

Applying this sentiment analysis, we have found that there is a slightly negative sentiment of -0.35 across comments on average and that the distribution of comment sentiment follows a relatively normal distribution, as shown below.

<p align="center">
  <img src="https://github.com/prakritj/ds105_wsb/blob/gh-pages/comment_sentiment.JPG?raw=true" height="400">
</p>

It is not surprising that the sentiment is skewed towards the left given the nature of r/WallStreetBets being filled with many posts and comments about losing money relative to posts and comments about making money. However, upon closer inspection of the  sentiment of specific comments picked randomly, we have noticed that the sentiment of comments may be getting measured incorrectly. A few examples are listed below:

- "GME and AMC to the moon" - Sentiment Score: 0
- "Reddit's EFT is on FIRE, GME 151%, BB 13% (w.e. but still), AMC 300%, LOOK AT US WE'RE THE HEDGE MANAGER NOW." - Sentiment Score: -2
- "Daily popular ticker thread words great. Instead of 165 tickers getting spammed by bag holders in the daily it's only 162, much more manageable". - Sentiment Score: 6

In the first comment, "to the moon" is a common phrase used by r/WallStreetBets redditors to show their support for a certain stock and reflects a positive sentiment, which isn't captured by the AFINN dictionary. In the second comment, the commenter is very positive about the gains in GME, BB and AMC, yet AFINN sentiment analysis believes that it has negative sentiment.
Lastly, in the third comment sarcasm is used so the AFINN dictionary is mislead into deeming that comment has positive sentiment.

This shows that there are limitations to using the AFINN lexicon to accurately measure the sentiment of r/WallStreetBets comments. This is in part to due the dictionary of words not being tailored to the words or phrases used on social media. Another limitation comes from using sentiment analysis based on words alone rather than phrases or entire sentences.

On a longer timescale, we may have been able to produce our own custom dictionary for words use on r/WallStreetBets to more accurately capture sentiment. Furthermore, there may be the potential to use machine learning to better capture the sentiment of whole phrases and sentiments by using services such as the [Natural Langauge Understanding AI](https://www.ibm.com/uk-en/cloud/watson-natural-language-understanding) by IBM.

*It is no surprise that sentiment is skewed towards the left, with a mean of -0.35 - but it is still follows a relatively normal distribution. Generally the internet is quite a negative place after all* 
*We ran this in comparison with an AFINN Dict - acknowledge limitations that it is not the most fitting for social media* -Done? William

**Reading Level Analysis**

Consider the high-stakes nature of investing large sums of money. these should be educated decisions made with a decent amount of analysis and thought. If indeed Redditors are somehow outsmarting institutional investors, then they must have done a significant amount of analysis to arrive at their conclusion regarding what stocks to pick! We can get a peek at the intelligence level of these conversations by doing a Flesch-Kincaid Reading Level Analysis - this analyses bodies of text to determine the level of reading at which it is written. 

*we saw xx level of reading, = to 10 year old. Note that these Redditors are engaging in investing - very likely that they are over 18 years old, most likely older since they have a significant level of savings/investment*

*based off of this, it is unlikely that redditors are thinking on a different level than institutional investors who do their homework. Limitation - this is not made for social media, scores take into account number of words/syllables/whatever, analysis might not be exactly correct. That said, it seems far off from the level of analysis that one should do before making investment decisions.*

### Further Analysis of Stocks

*here, talk about how we took each comment apart by word, compared it to a list of all US equities (based on our reading of the forum, their focus is on US Stocks). Then we extracted the top 30 - many are false positives. Eliminated the false positives by generating a random list of comments which have each ticker, determine whether it is buy, sell, or false positive. Then say we got the top XX stocks as a result, sorted based on total upvotes*

*need to connect this back to our argument. A lot of institutional and sophisticated investors try to diversify their exposure to market volatility by betting on some stocks going down, some going up - buy and put. In this case, r/WSB is only buying. Clearly they are not risk averse in this regard. It also demonstrates a lack of sophistication to only bet on stocks going up. we will see with regards to exposure to different industries, and it is also possible that they prefer higher risk trades.*

**Looking at our list of stocks**

*before delving into further analysis, briefly run through the stocks that made it to the top 23. In particular discuss a few that have probably gained some attention - GME, AMC, WISH, TSLA, etc. Focus on why they invested in GME and and AMC - to get back at financial industry. At this point, we will post our data viz JS component.*

**Looking at Sectors**

*Zoom back out to look at our overall data. Explain briefly process of getting industry data from Yahoo Finance using yfinance. Total of 8 industries within the top 23 stocks - yfinance has total of 11. But looking through, most are consumer cyclical, technology, healthcare.*

*weighted each sector by upvotes, examined it as a share. 3 big sectors in consumer cyclical, technology, communication services = 83% of upvotes. look at slide for why, separate behaviour when trying to bet on company growth vs acting out of spite.*
*one takeaway here is again, super high risk. A lot of positions are concentrated on very few industries. These may be high growth, but without a lot of diversification with regards to industries. And it may also be volatile. Another takeaway is that a LOT of upvotes are dedicated to just acting out of spite. Again, indicates a lack of sense when making financial decisions. (maybe can put this point somewhere else).*

## Overall Performance 

**Individual Stocks**
*How did stocks do since Jul 1 and before then?*

**Aggregating Performance**
*talk about the WSB index. Focus on other components than just overall performance, see volatility. Compare ex-ante vs ex-post. See composition of stocks.
*takeaway = these practices are not profitable in the short term. perhaps there is a long term play but ultimately it's an unpredictable market and these stocks are volatile. Also, since these investments are not completely geared towards pure profitability (there is some anger involved), not a must that these must go up!*


## Conclusion

*Based on our analysis, we are sceptical of the investments that r/WSB advocates for. There is little evidence of any sophisticated analysis done before choosing a company. Many of them are chosen based on anger/emotions, irrational. There is an extremely high exposure to risk - all action towards buy, not diversified in industries. High risk high reward strategy. Analysis of performance suggests that there is little reward, however. Despite that, our analysis is done over a short-term and thus there is a possibility (though we believe it is slim) that these stocks will generate money in the future.*

*we'd also like to shed some light on the possible consequences of this. Redditors are investing a significant portion of their life savings in these stocks. Based on their level of sophistication and analysis, it may be reasonable to determine that these are not professionals in the financial industry. They may not know to the fullest extent what they are doing. The fact that there is this large investing community propogating advice which doesn't seem demonstrably profitable raises the decent possibility that many will be a victim of such advice, losing much of their life savings. This has larger societal consequences in people working past their ideal age of retirement (or not being able to retire at all). These negative welfare implications are significant and we hope that this rudimentary analysis of this data on r/WSB can show that it is not a community for those looking to actually make money.*
