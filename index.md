<link rel="stylesheet" href="styles.css">

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
|![image](https://user-images.githubusercontent.com/92173642/147845910-3c2be8d4-68fd-41b4-8884-bc76a339d03d.png)|

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

In our 180 day period, we went through 130 posts - these Daily Discussion Threads were not posted on weekends and other days when the market was closed. Despite not being able to retrieve all comments, we still pulled 92,379 comments out of a total of 3.5 million. These comments amassed more than 2 million upvotes, with an average score of 23.84 (score being upvotes - downvotes).

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

|Negatively-skewed Reading Level of r/WSB Comments|
|:--:|
|![Reading_level_image](https://user-images.githubusercontent.com/92174920/147933005-d78011c9-a497-4cd2-a725-fa684909ea0a.png)|

Unlike some social media forums where the average user is indeed very young, r/WSB users are discussing investing, a topic generally reserved for those over 18, and more popular for those who are older and have far more in savings to invest. It is difficult to turn a blind eye to adults discussing financial information with the written maturity of a 10-year-old, particularly when it is consequential for their future. Considering these comments are neither analytical nor insightful, it is unlikely that Redditors are outsmarting institutional investors - professionals who do their homework.

However, there are some limitations with applying the Flesch-Kincaid Reading Level methodology to our dataset. Social media comments are generally short with fewer sentences and words compared to other media. Because of the way reading level is calculated (see below), these comments can generate low (or even negative) reading levels, underestimating the writer's intelligence. Therefore, we conducted a deeper analysis, looking at comments with their respective reading level to determine whether there were any discrepancies.

![image](https://user-images.githubusercontent.com/92173642/147844306-5f73bb58-591e-4634-83fd-45b3f2b6ce9a.png)

When examining these comments and their attributed reading level, it's no surprise that the average Flesch-Kincaid Reading Level was so low. They are often short phrases with little-to-no analysis, not saying much beyond a stock ticker itself:

|**Comment**|**Reading Level**|
|:--|:--:|
|"NIO to 60 EOW"|2.5|
|"Imagine paperhandling CLNE during such a buying opportunity"|14.7|
|"This market is dumb. Who bought calls on CLNE? Who tanked it?"|-1.0|
|"WISHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH"|952.4|

Our secondary analysis shows that the Flesch-Kincaid Reading Level is low on social media comments not solely because it isn't tuned for them (though this may be a factor), but to a large extent because this medium is not conducive for intellectual conversations in the first place. Though one would hope that Redditors would do a significant amount of analysis before investing their savings, our data shows that little analysis is being presented or discussed before investment decisions are being made. It is improbable that this strategy would outperform the financial industry, or benchmarks such as the S&P500. A lack of even rudimentary analysis suggests that many of these decisions are irrational.

### Further Analysis of Stocks

To analyse our dataset further, we needed to identify the stocks that r/WSB was discussing on a larger scale. To do this, we stripped each comment into all-caps words resembling stock tickers, compared it against a list of all companies listed in the US (r/WSB primarily discusses US-based companies) and then extracted the top 30 tickers mentioned on the Subreddit. From this, many were a false positive - all-caps words which were used frequently but not in the context of the stock itself. We eliminated  false positives by examining a random list of comments for each ticker, categorising them into three categories: buy, sell, or false positive. 7 were false positives, leaving us with a list of 23 companies to analyse, sorted below by cumulative score:

|**Ticker**|**Frequency**|**Cumulative Score**|**Buy/Sell**|
|:--:|:--:|:--:|:--:|
|GME|7554|360351|Buy|
|AMC|5879|206158|Buy|
|PLTR|4992|90611|Buy|
|NOK|936|44803|Buy|
|SNDL|1252|37284|Buy|
|WISH|1826|35522|Buy|
|TSLA|2119|30824|Buy|
|CLOV|1544|28758|Buy|
|MVIS|1303|27584|Buy|
|CLNE|1373|26641|Buy|
|TLRY|1311|23135|Buy|
|UWMC|981|14844|Buy|
|AAPL|949|13625|Buy|
|RKT|918|13028|Buy|
|WKHS|655|10360|Buy|
|NIO|585|8015|Buy|
|EDIT|42|7129|Buy|
|CLF|471|7090|Buy|
|AMD|629|6643|Buy|
|SPCE|440|6017|Buy|
|CRSR|288|5124|Buy|
|ASO|399|5019|Buy|
|OCGN|323|4981|Buy|

As our data shows, **r/WSB only advocates for buying stocks**. We interpret this to be a demonstration of the lack of sophistication of financial advice given on r/WSB, in line with our previous data on reading level. Perhaps it is a fixed mindset for spotting opportunities; they only see the ways that companies can grow but not the ways they could fail. Such an intellectual gap would also explain poor stock performance, which is covered in the next section.

This pattern of only buying stocks also indicates that their holistic investment strategy (if there is one) is extremely risky. Most trained individual investors as well as institutional investors try to diversify their exposure to market volatility by short-selling (betting on some stocks going down) in addition to buying stocks conventionally.  Although the stock market does trend up in general, such a high-risk, high-reward strategy could be detrimental when retail investors are looking to retire based on how their portfolio has grown over a long period of time. This would also test the longevity and long-term prospects for investments from r/WSB, as these investors may run out of capital quickly before they are able to benefit from long-term gains. More succinctly, it seems like r/WallStreetBets  eponymously advocates for gambling rather than skillful investing, and users following such advice could be throwing their money away.

**Looking at Sectors**

<div id = "chart">
<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/4.2.2/d3.min.js"></script>
<script src="visualisation.js"></script>
</div>

Investors can also decrease their exposure to risk by investing in several different economic sectors which are unlikely to fail synchronously. Therefore, we examined which sectors were popular with r/WSB users to determine whether it was diversified. Sector data was pulled from yahoo Finance using the `yfinance` Python module. Yahoo Finance has 11 different sectors - r/WSB's Top 23 stocks covered 8 of them. Though this seems diversified on the face of it, once we weighed sectors by the Reddit score that comments referencing their respective companies had received, it was clear that only a few industries had been popular. 

|Sectors and their Respective Score|
|:--:|
|![image](https://user-images.githubusercontent.com/92173642/147846348-3af92a6b-1c74-4b8e-bcc6-5ee290f88dd4.jpeg)|

Out of the 8 sectors represented in the top 23 stocks, 3 sectors got 83% of the upvotes (score). On a broader level, these popular companies can mostly be sorted into two categories: (1) firms which have invested in some technological innovation, and (2) investments to profit from squeezing out short-sellers. Below are how the companies in the 3 industrial sectors broadly fit into our two categories.

*Consumer Cyclical*
- GME is a brick-and-mortar game electronics company which was heavily shorted by Wall Street - *Squeeze*.
- TSLA, NIO, and WKHS are innovators in the space of electric vehicles - *Innovation*.
- WISH is an e-commerce platform which uses algorithms for a more personalised shopping experience - *Innovation*.

*Communication Services*
- AMC is a cinema theatre company which was heavily shorted by Wall Street - *Squeeze*.

*Technology*
- PLTR is specialises in software and data analytics - *Innovation*.
- NOK now develops telecommunications technologies - *Innovation*.
- MVIS develops laser scanning technologies for use in autonomous driving applications - *Innovation*.
- AMD is a semi-conductor company designing computing and processing chips - *Innovation*.
- AAPL is a consumer electronics and software company - *Innovation*.

This again demonstrates an unsophisticated, high-risk strategy. Other than squeezing Wall Street short-sellers, r/WSB's main targets are companies which leverage technological innovation as their main selling point. This makes their strategy even riskier. Not only are r/WSB investors vulnerable to market crashes, but they are also in jeopardy if the technological industry is deemed to be overvalued. A dot-com-like bubble may burst, wiping out the majority of r/WSB stocks. This would be disastrous to these retail investors who rely on advice on r/WSB. Professional investors know better than to greatly expose themselves to such a risk.

Thus, our data reinforces our assertion that investing advice on r/WSB is akin to gambling instead of a thought-out strategy.

## Overall Performance 

Having discussed r/WSB's investment strategies (or lack thereof) as well as trends in interest, the obvious question is: "Are they successful?" We analysed the performance of these stocks individually before aggregating them to approach it from a different angle.

**Individual Stocks**

<div id = "chart2">
<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/4.2.2/d3.min.js"></script>
<script src="visualisation2.js"></script>
</div>

In line with what we saw with sectors, there is a marked difference in performance between companies where r/WSB attempted to squeeze out short-sellers, and those where r/WSB tried to bet on true growth. 

_Short Squeeze Stocks_

The case of the former is best represented by GME and AMC. For these, we observed a rapid increase in price _because_ of r/WSB investors. The reason for this is twofold: while these significant new investments would have increased the price directly, short-sellers also decided to liquidate their positions, increasing the price further. This occurred rapidly; GME's stock price surged for example from less than $50 in January to more than $250 by the beginning of February. AMC's stock price rose from around 10$ in mid-May to more than 60$ in the first days of June. It is most obvious when viewing this graphically: 

|GME (GameStop) YTD|
|:--:|
|![image](https://user-images.githubusercontent.com/92173642/148428265-f55129ae-55da-42a9-8b8f-34234b904912.png)|

|AMC (AMC Entertainment) YTD|
|:--:|
|![image](https://user-images.githubusercontent.com/92173642/148428313-bb0a8d2b-6ac1-436c-8a76-543e1456fc65.png)|

At first thought, it appears that r/WSB's collective action is successful as the stock price increased! However, because Redditors were partially driving this growth, we know that not all of them invested at the bottom. Mathematically, we know only a small portion did - most others are likely to have invested at other points during the rise, including near the peak. For these investors, it is unlikely that they made a significant profit - if they made one at all. 

Note that in both of these companies, the stock price has not tumbled in the months after being targeted by r/WSB. Considering that these stocks have little growth potential remaining (it grew because of r/WSB investors, all of whom have already invested), investors in the company would serve themselves well to close their position. So why have r/WSB investors not done so? Their discussion clearly reflects an intent to hold for as long as possible to squeeze out further short-sellers. 

This may be (temporarily) preventing an impending crash. Because the rest of the market does not share r/WSB's sentiment for these companies, Redditors will find it difficult to sell their stocks in these companies. Because others aren't buying as much as Redditors have, not all will be able to sell at the current market price. If these stock prices decrease at the same speed at which they had risen, this could be very damaging for many r/WSB investors - especially those that invested in high prices. This collective behaviour is masking potential losses that r/WSB investors will face when they finally liquidate their positions. Given the releatively new phenomenon of r/WSB popularity, current stock prices do not reflect such a possibility.

To make money investing in companies like GME and AMC because of influence from r/WSB, retail investors will have to rely on early signals from the Reddit community and invest before others. Subsequently, they need to close their positions before others. Given the largesse of r/WSB and their willingness to quickly invest, this would be a difficult feat. Profiting from these investments would thus require a significant amount of luck.

_Other Companies_

For other companies where r/WSB was not advocating for a short squeeze, most had trended downwards in 2021. Below, we show the trend of some of the most popular stocks which r/WSB advocated for:

|PLTR (Palantir)|CLNE (Clean Energy)|
|:--:|:--:|
|![image](https://user-images.githubusercontent.com/92173642/148366667-959d2ab8-1565-4813-b8ee-9dc0543cf449.png)|![image](https://user-images.githubusercontent.com/92173642/148366684-2fbfdbaf-12c1-4b76-9df3-f9b055966ce2.png)|
|**WISH (Wish)**|**SNDL (Sundial Technologies)**|
|![image](https://user-images.githubusercontent.com/92173642/148366836-b081109d-9862-4c25-a9b1-24f79b37c47a.png)|![image](https://user-images.githubusercontent.com/92173642/148367127-739a72fc-9463-4cc0-8031-f47e485a793f.png)|

There were two major exceptions to this trend: Tesla and Nokia, both of which did exceedingly well in 2021. Nokia's growth was partly driven by r/WSB (particularly in an early spike), but its growth over time was mainly due to investors aware of its [a financial recovery](https://www.ft.com/content/2377219b-0c8f-4d36-983e-1c1947d4a961), far more tenable than investments in GME or AMC.

|TSLA (Tesla)|NOK (Nokia)|
|:--:|:--:|
|![image](https://user-images.githubusercontent.com/92173642/148366843-5414df2b-b323-41ec-903c-07a92a6a8d90.png)|![image](https://user-images.githubusercontent.com/92173642/148367344-cc2b45ab-6cdd-4b97-9e96-0923020d70bf.png)|

On the quantum of companies alone, our data clearly suggests that r/WSB investors would have lost money on these investments this year. In other words _most_ of these investment decisions seem to be rather amiss. Their advice doesn't seem to be very profitable.

**Aggregating Performance**

Although examining stock performance individually is an indicator of overall performance, r/WSB traders (just like all investors) would not be investing equally into all of these companies. As a gauge for how r/WSB investors diversify their portfolio, we weighed each company in the top 10 (out of the top 23 stocks, the top 10 make up over 80% of total score) by their total Reddit score to create a 'r/WSB Index' with a different amount in each company. As can be seen below, GME and AMC make up a significant portion of the index at 64%, indicating that r/WSB is far more interested in short squeeze investments than others. 

|Composition of the r/WSB Index|
|:--:|
|![image](https://user-images.githubusercontent.com/92173642/148428387-d2141165-8626-4da3-8da9-1b7478ad06dd.png)|

We analysed two periods for this r/WSB Index: from Jan to Dec 2021, from the start period of our Reddit comments data, and Jul to Dec 2021, the period directly after all the comments. This provides us data on ex-ante investments which predate these comments, and ex-post investments which follow them.

Because short squeeze investments dominate the index, it is expected that the Index's ex-ante performance forecasted was very strong: throughout the year, these stocks generated returns of over 600%. This was mostly driven by sudden rises in GME and AMC which made up the majority of these holdings. Note that returns actually peaked in June, when they reached almost 1300% - since then, the index has been decreasing or stable.

|Ex-Ante r/WSB Index Performance|
|:--:|
|![image](https://user-images.githubusercontent.com/92173642/148428414-d74bc604-2bd1-4035-a079-58fda7fa03a4.png)|

As we hinted at earlier, ex-post performance is less laudable. Since July, these investments have lost -22% in value. It is also obvious that these investments are very volatile, and there is no clear trend as to the future of these investments. 

|Ex-Post r/WSB Index Performance|
|:--:|
|![image](https://user-images.githubusercontent.com/92173642/148428476-ec751abd-d93b-4721-9d66-246754a26001.png)|

These returns are striking compared to the S&P 500, a commonly-referenced equity index with the top 500 companies in the US. Throughout the year, the S&P 500 gained 26%. This is rather high for the index, and yet the r/WSB Index outperformed it significantly. In the last 6 months of 2021, however, the S&P500 grew 7% while the r/WSB Index made a loss. The companies chosen by r/WSB are not indicative of the overall market, and therefore it is no surprise that the performance does not track well with the S&P 500 either. 

|S&P 500 2021 Performance|
|:--:|
|![image](https://user-images.githubusercontent.com/92173642/148428501-e8a6db1c-4de0-4e9f-8cbb-d32c85c3a6d2.png)|

These results validate our previous findings. r/WSB investments don't necessarily perform better than the rest of the market, as can be seen in the last few months of 2021. Those companies are volatile and are risky to invest in, particularly when dealing with large sums for retail investors.

Based on the difference between the first and second half of 2021, it is evident that a large part of why these stocks go up is because of r/WSB involvement. The performance in these stocks after July is an indication of the losses that r/WSB investors may be facing in the future after an initial phase. As we stated earlier, it is likely that over time, the prices of these stocks will decrease as Redditors close their positions while the rest of the market sees little value in buying those stocks, and our ex-post performance is denotative of that.

<div id = "chart3">
<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/4.2.2/d3.min.js"></script>
<script src="visualisation3.js"></script>
</div>

Regular profit-driven investments recommended by r/WSB seem to be losing propositions in general. Short squeeze investments are profitable, but only for a select few. To profit from these investments, one has to enter _before_ the hype created by Reddit (ex-ante). To do so, they need to predict that a craze would erupt, a difficult task given the thousands of comments every day. Instead, it is more plausible that profiteers are just 'lucky' that they invested at the right time and closed their positions before a subsequent crash.

### Sentiment Analysis and Distribution

To get an overview of the opinions and emotions that people were expressing on Reddit, we ran a sentiment analysis comparing our dataset of r/WSB comments with the popular AFINN Sentiment Lexicon. The AFINN Lexicon is a dictionary of a couple thousand English words rated for valence with an integer between -5 (negative) and +5 (positive).

The average comment sentiment was -0.35, however the median and mode were 0 - thus, the distribution of comment sentiment was negatively skewed, as shown below.

|Negatively-Skewed r/WSB Comment Sentiment Distribution|
|:--:|
|![image](https://user-images.githubusercontent.com/92173642/147842092-94823cb6-65a2-4bb7-83dc-0f7f5aca71d9.jpeg)|

Considering the general negativity of the internet, it was not surprising to us that the mean sentiment was negative. However, upon further review, we discovered that the negativity was driven by reactions to negative outcomes on the stock market. In other words, r/WSB investors were upset that their investments had decreased in value, and expressed their dissapointment on r/WSB. A few examples best demonstrate this:

_**Negative Sentiment Around GME After the Spike**_
|**Comment**|**Sentiment Score**|
|---|:---:|
|"Managed to get another GME in the sale just before closing, F___ YOU WALL STREET, I'M NOT F___ING SELLING💎🤲🚀🚀🚀🚀🚀"|-8|
|"BUY BUY BUY. DONT LIVE YOUR LIFE SCARED! IF YOU ARE SCARED TO LOSE A FEW BUCKS BEFORE AMC AND GME BLAST OFF THEN WE DONT NEED YOU"|-4|
|"So let me get this straight, GME crashes through the floor with a $250 m artificial dump monkey hammer ladder, and no halting. It gets a little steam and boom, trading halted?  Crooked ass NYSE jerks."|-5|

Despite this finding, we also noticed some pecularities with the way the AFINN Lexicon rated our comments. It did not consistently and accurately interpret meaning and tone given the context and language of r/WSB users. Below are a few examples where this is most evident:  

|**Comment**|**Sentiment Score**|
|:---|:---:|
|"GME and AMC to the moon"|0|
|"Reddit's EFT is on FIRE, GME 151%, BB 13% (w.e. but still), AMC 300%, LOOK AT US WE'RE THE HEDGE MANAGER NOW."|-2|
|"Daily popular ticker thread words great. Instead of 165 tickers getting spammed by bag holders in the daily it's only 162, much more manageable".|+6|

"To the moon" is a *very* common phrase used by r/WSB to show their support for a certain stock and reflects a positive sentiment. However, as shown in the first comment, this is not reflected in the AFINN Sentiment Score. As the Lexicon has a limited number of words in the dictionary, many comments go unrated, explaining our mode of a 0 sentiment score. In the second comment, the commenter uses "fire" in a positive way to suggest that the stocks they mentioned were going up, yet the AFINN Lexico interprets this word in a negative way and attributes it a negative sentiment score. Social media users also regularly use irony and sarcasm, which the AFINN Lexicon is unable to understand; the third comment is therefore incorrectly attributed a positive sentiment score. Ultimately, the AFINN Lexicon may not be the best method to analysis the sentiment of social media comments - had we known this earlier, we may have opted to use machine learning instead.

Despite the limitations of our sentiment analysis method, after having perused many comments and their attributed sentiment, we still believe that our previous proposition – that the overall sentiment on r/WSB was negative due to poor performance of stocks of interest – holds true.


## Conclusion

*Based on our analysis, we are sceptical of the investments that r/WSB advocates for. There is little evidence of any sophisticated analysis done before choosing a company. Many of them are chosen based on anger/emotions, irrational. There is an extremely high exposure to risk - all action towards buy, not diversified in industries. High risk high reward strategy. Analysis of performance suggests that there is little reward, however. Despite that, our analysis is done over a short-term and thus there is a possibility (though we believe it is slim) that these stocks will generate money in the future.*

*we'd also like to shed some light on the possible consequences of this. Redditors are investing a significant portion of their life savings in these stocks. Based on their level of sophistication and analysis, it may be reasonable to determine that these are not professionals in the financial industry. They may not know to the fullest extent what they are doing. The fact that there is this large investing community propogating advice which doesn't seem demonstrably profitable raises the decent possibility that many will be a victim of such advice, losing much of their life savings. This has larger societal consequences in people working past their ideal age of retirement (or not being able to retire at all). These negative welfare implications are significant and we hope that this rudimentary analysis of this data on r/WSB can show that it is not a community for those looking to actually make money.*
