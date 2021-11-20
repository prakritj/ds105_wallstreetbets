import praw as praw
import pandas as pd
import time
from datetime import datetime

reddit = praw.Reddit(
    client_id="0GFgVgByJ065sadDY62Q4g",
    client_secret="KfE32h3JMcZPLSF3UmYMJMsJbrXcaQ",
    password="ftu8uac9edb_TKM1yua",
    user_agent="testscript_for_WSB",
    username="ds105_WSB",
)

def wsb_function(start_date,end_date,month, posts_df):
    # start_date = datetime.date(2021,1,1)
    # end_date = datetime.date(2021,7,1) #because WSB is in US timezone but created.utc is in UTC.
    convert_start = datetime.strptime(start_date, '%d/%m/%Y')
    convert_end = datetime.strptime(end_date, '%d/%m/%Y')
    unix_start = time.mktime(convert_start.timetuple())
    unix_end = time.mktime(convert_end.timetuple())
    wsb = reddit.subreddit('wallstreetbets')
    for submission in wsb.search('Daily Discussion Thread for '+month, sort='new', time_filter='all', limit=1000):
        if 'Daily Discussion Thread for ' in submission.title and 'Unpinned' not in submission.title:
            if submission.created_utc >= unix_start and submission.created_utc <= unix_end: #need to check whether the post is within our two week window
                #I need title, id, comments, score, put into posts_df
                print('Posts: ' + submission.title)
                try:
                    submission.comments.replace_more(limit=3) #Need to change limit
                except:
                    print('Error: Unable to Replace More Comments')
                    pass
                # submission.comments.replace_more(limit=None)
                posts_df = posts_df.append({
                    'id':submission.id,
                    'title':submission.title,
                    'score':submission.score,
                    'top_level_comments': list(submission.comments),
                    'num_comments':submission.num_comments
                }, ignore_index=True)

posts=pd.DataFrame()
wsb_function('01/01/2021', '01/07/2021', 'January', posts)
wsb_function('01/01/2021', '01/07/2021', 'February', posts)
wsb_function('01/01/2021', '01/07/2021', 'March', posts)
wsb_function('01/01/2021', '01/07/2021', 'April', posts)
wsb_function('01/01/2021', '01/07/2021', 'May', posts)
wsb_function('01/01/2021', '01/07/2021', 'June', posts)
posts.to_pickle('WSB_Posts')
posts.to_csv(r'posts.csv', mode = 'w')

comments_df = pd.DataFrame()
for post in posts.itertuples():
    print('Comments: ' + post.title)
    for comment in post.top_level_comments:
        comments_df = comments_df.append({
            'id':comment.id,
            'post_id':comment.link_id,
            'body':comment.body,
            'score':comment.score
        }, ignore_index=True)
comments_df.to_pickle('WSB_Comments')
comments_df.to_csv(r'comments.csv', mode = 'w')
