<div id = "chart">
<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/4.2.2/d3.min.js"></script>
<script src="visualisation.js"></script>
</div>

*Need to add a TLDR; do so at the end*
# Exploring the Jungle of r/WSB

## Context

*talk about context - why is this important, general happenings over the last 12 months that make this important*

Over the last 12 months, there has been a seismic increase in followers of the Reddit community (known as a *subreddit*) [r/WallStreetBets](https://reddit.com/r/wallstreetbets). As a group of retail investors (but each operating on their own accord), these followers collectively invested in stocks on the US market, coordinating through Reddit forums. This subreddit has amassed over 11 million followers since its creationg on January 31st 2012, with the vast majority (9.5 million) of these followers arising from WSB's notorious short of the GameStop stock, GME, displaying unprecedented growth for a subreddit this year. With an average of 12000 comments and 500 posts per day, r/WallStreetBets continues to be one of the most active subreddits on the platform long after the GME debacle, and has seemingly been able to influence the stocks prices of [AMC Entertainment Holdings](https://finance.yahoo.com/quote/AMC),[Nokia](https://finance.yahoo.com/quote/NOK/) and [Sundial Growers](https://finance.yahoo.com/quote/SNDL/) to name a few.([Subreddit Stats, 2021](https://subredditstats.com/r/wallstreetbets)) 

*carry on about impact on the mainstream financial industry, subscriber growth, how active they are on Reddit, etc.) Cite some articles and data supporting this* Done? -William

*what motivated us* As observers of these trends, we wanted to further understand them for two reasons. Firstly, as a collective group of retail investors, r/WSB was able to rattle the financial industry despite competing against professionals with access to a vast amount of financial capital and real-time information to act upon. Secondly, we saw that many of these investors were pouring significant amounts, even their life savings ![200k_Loss](https://github.com/prakritj/ds105_wsb/blob/gh-pages/WSB_200k_loss.jpg?raw=true) into many companies advocated for on the platform. These investments are often unconventional, and financial professionals/ratings firms don't share many of the views of the community. The question then is: who's right? Are r/WSB investors throwing their money away or have they proved institutional investors wrong? To answer this, we needed to do a deeper analysis of the r/WSB community, what is being said on these forums, and understand the stocks that they are advocating for to identify patterns and performance trends. *need to expand a bit more on this, with some evidence, etc.*


*for the rest of this, I will be more brief and merely provide a basic template*
## Getting our Data

*Julio said that adding code can make it confusing so we should try to make this as simple as possible while covering enough bases*

### What Data do we Want?

As with any subreddit, there is a wide variety of posts and comments on r/WallStreetBets including images, gifs and videos. Combined with around 1000 posts per day (during the period that we would be looking at) and the even greater number of comments on those posts, it would be extremely difficult to analyse everything on r/WSB. In the end, we opted to only analyse comments from daily discussion threads, as this is typically the most popular and most active post accounting for the vast majority of comments everyday. Doing this made the process of parsing through and restructuring the data mmuch simpler, as it ensured that we only needed to look at one datatype (text). 

*talk about how there are so many posts and comments on r/WSB, it would be difficult to analyse a lot of them. Thus we opted to only analyse comments from daily threads to manage the data, ensure only one datatype (text) which is easy to parse and go through.* Done? -William

**Time Period**

Based on r/WSB's meteoric rise in the beginning of 2021, we thought it most appropriate to analyse comments from the first half of 2021 (Jan 1 to Jun 30). This ensures we cover comments from a time of peak popularity on the community, but also allows us to run a retrospective analysis on how well these companies have performed in the months after discussions had occurred.

### Obtaining Data

We opted to use Python to obtain and analyse data, and used [PRAW](https://praw.readthedocs.io/en/stable/), a wrapper for the reddit API, to get our data from Reddit. Being an API wrapper, it is very straightforward to use compared to dealing with the API mannually, featuring many quality-of-life features such as seeting a request limit of 60 per minute. Furthermore, the documentation is elaborate and well-written, and the wrapper stores post and comment data in objects with attributes. This made it very easy to store our data in Pandas Dataframes, a 2-D tabular data structure, to organise and iterate over them. This is far superior compared to just using the API raw where data is returned in a JSON format which is extremely messy and unncessarily difficult to deal with. 

*need to expand on this* Done? -William

*talk about issue regarding more comments here briefly*.

## Analysing our Data

### Overview

**Statistical Summary**
*how many comments collected, how many posts collected, total upvotes, average upvotes, etc.*

|  | **Count** |
| **Posts** | 130 |
| **Total Posts Score** | 178,323 |
| **Average Post Score** | 1372 |
| **Total Comments** | 3,597,073 |
| **Average Comments per Post** | 27,670 |
| **Comments Pulled** | 92,379 | 
| **Total Score of Comments Pulled** | 2,202,633 |
| **Average Score of Comments Pulled** | 23.84 |

**Sentiment Analysis and Distribution**

*It is no surprise that sentiment is skewed towards the left, with a mean of -0.35 - but it is still follows a relatively normal distribution. Generally the internet is quite a negative place after all*
*We ran this in comparison with an AFINN Dict - acknowledge limitations that it is not the most fitting for social media*

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
