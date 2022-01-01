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

One limitation with Reddit's API (and, by extension, PRAW) is the way it retrieves comments from these posts. Rather than extracting them all at once, it only generates the top few by default. The rest are nested in `more_comments` instances, something similar to the 'load more comments' button you might see on the Reddit website. To replace these `more_comments` instances with actual comments, however, is extremely time intensive due to the sheer number of comments we were dealing with and the limitations on number of requests imposed by the API. As a result, our data doesn't include all comments during our time period, but only the top few which were automatically returned by the API. Since these comments were those which were most popular (and received more upvotes), we believe this has a limited impact on our analysis. 

## Analysing our Data

### Statistical Summary

In our 180 day period, we went through 130 posts - these Daily Discussion Threads were not posted on weekends. Despite not being able to retrieve all comments, we still pulled 92,379 comments out of a total of 3.5 million. These comments amassed more than 2 million upvotes, with an average score of 23.84 (score being upvotes - downvotes).

Noteworthy is the high activity on these forums. 27,670 comments per day were posted on these discussion threads alone. The 2+ million upvotes on comments during this period indicates a high level of engagement with these comments. There is a significant amount of content regularly submitted on r/WSB, even on working days when these threads are active.   

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

### Reading Level Analysis

Before analysing the stocks mentioned on r/WSB, we wanted to find out how intelligent these comments were in the first place. We can get a peek at the intelligence level of these conversations by doing a Flesch-Kincaid Reading Level Analysis - this analyses bodies of text to determine the level of reading at which it is written.

The reading level of these comments is astonishingly low - an average of Grade 3.93 (according to a US-style Education System), around the level of a 10-year-old.

__*William - add Reading Level Distribution here, elaborate a bit on it*__

Unlike some social media forums where the average user is indeed very young, r/WSB users are discussing investing, a topic generally reserved for those over 18, and more popular for those who are older and have far more in savings to invest. It is difficult to turn a blind eye to adults discussing financial information with the written maturity of a 10-year-old, particularly when it is consequential for their future.

When examining these comments and their attributed reading level, it's no surprise that the average reading level was so low. They are often short phrases with little-to-no analysis, not saying much beyond a stock ticker itself.

Considering these comments are not particularly analytical nor insightful, it is unlikely that Redditors are outsmarting institutional investors - professionals who do their homework. 

Limitation - this is not made for social media, scores take into account number of words/syllables/whatever, analysis might not be exactly correct. That said, it seems far off from the level of analysis that one should do before making investment decisions.*

Consider the high-stakes nature of investing large sums of money. these should be educated decisions made with a decent amount of analysis and thought. If indeed Redditors are somehow outsmarting institutional investors, then they must have done a significant amount of analysis to arrive at their conclusion regarding what stocks to pick! 

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

### Sentiment Analysis and Distribution

To get an overview of the opinions and emotions that people were expressing on Reddit, we ran a sentiment analysis comparing our dataset of r/WSB comments with the popular AFINN Sentiment Lexicon. The AFINN Lexicon is a dictionary of a couple thousand English words rated for valence with an integer between -5 (negative) and +5 (positive).

The average comment sentiment was -0.35, however the median and mode were 0 - thus, the distribution of comment sentiment was negatively skewed, as shown below.

|Negatively-Skewed r/WSB Comment Sentiment Distribution|
|:--:|
|![image](https://user-images.githubusercontent.com/92173642/147842092-94823cb6-65a2-4bb7-83dc-0f7f5aca71d9.jpeg)|

Considering the general negativity of the internet, it was not surprising to us that the mean sentiment was negative. However, upon further review, we discovered that the negativity was driven by reactions to negative outcomes on the stock market. In other words, r/WSB investors were upset that their investments had decreased in value, and expressed their dissapointment on r/WSB. A few examples best demonstrate this:

__*William: add comment examples based on the above*__

Despite this finding, we also noticed some pecularities with the way the AFINN Lexicon rated our comments. It did not consistently and accurately interpret meaning and tone given the context and language of r/WSB users. Below are a few examples where this is most evident:  

|**Comment**|**Sentiment Score**|
| --- | ---: |
| "GME and AMC to the moon" | 0 |
| "Reddit's EFT is on FIRE, GME 151%, BB 13% (w.e. but still), AMC 300%, LOOK AT US WE'RE THE HEDGE MANAGER NOW." | -2 |
| "Daily popular ticker thread words great. Instead of 165 tickers getting spammed by bag holders in the daily it's only 162, much more manageable". | +6 |

"To the moon" is a *very* common phrase used by r/WSB to show their support for a certain stock and reflects a positive sentiment. However, as shown in the first comment, this is not reflected in the AFINN Sentiment Score. As the Lexicon has a limited number of words in the dictionary, many comments go unrated, explaining our mode of a 0 sentiment score. In the second comment, the commenter uses "fire" in a positive way to suggest that the stocks they mentioned were going up, yet the AFINN Lexico interprets this word in a negative way and attributes it a negative sentiment score. Social media users also regularly use irony and sarcasm, which the AFINN Lexicon is unable to understand; the third comment is therefore incorrectly attributed a positive sentiment score. Ultimately, the AFINN Lexicon may not be the best method to analysis the sentiment of social media comments - had we known this earlier, we may have opted to use machine learning instead.

Despite the limitations of our sentiment analysis method, after having perused many comments and their attributed sentiment, we still believe that our previous proposition that the overall sentiment on r/WSB was negative due to poor performance of stocks of interest holds true.


## Conclusion

*Based on our analysis, we are sceptical of the investments that r/WSB advocates for. There is little evidence of any sophisticated analysis done before choosing a company. Many of them are chosen based on anger/emotions, irrational. There is an extremely high exposure to risk - all action towards buy, not diversified in industries. High risk high reward strategy. Analysis of performance suggests that there is little reward, however. Despite that, our analysis is done over a short-term and thus there is a possibility (though we believe it is slim) that these stocks will generate money in the future.*

*we'd also like to shed some light on the possible consequences of this. Redditors are investing a significant portion of their life savings in these stocks. Based on their level of sophistication and analysis, it may be reasonable to determine that these are not professionals in the financial industry. They may not know to the fullest extent what they are doing. The fact that there is this large investing community propogating advice which doesn't seem demonstrably profitable raises the decent possibility that many will be a victim of such advice, losing much of their life savings. This has larger societal consequences in people working past their ideal age of retirement (or not being able to retire at all). These negative welfare implications are significant and we hope that this rudimentary analysis of this data on r/WSB can show that it is not a community for those looking to actually make money.*
