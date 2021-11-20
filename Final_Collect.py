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
posts_df = pd.DataFrame()
start_date = '01/01/2021'
end_date = '01/07/2021' #because WSB is in US timezone but created.utc is in UTC.
convert_start = datetime.strptime(start_date, '%d/%m/%Y')
convert_end = datetime.strptime(end_date, '%d/%m/%Y')
unix_start = time.mktime(convert_start.timetuple())
unix_end = time.mktime(convert_end.timetuple())
wsb = reddit.subreddit('wallstreetbets')

#need to run multiple times, once for each month so can extract all the posts given the 250 search limit

# start with June
for submission in wsb.search('Daily Discussion Thread for '+ 'June', sort='new', time_filter='all', limit=1000):
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

#May
for submission in wsb.search('Daily Discussion Thread for '+ 'May', sort='new', time_filter='all', limit=1000):
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

#April
for submission in wsb.search('Daily Discussion Thread for '+ 'April', sort='new', time_filter='all', limit=1000):
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

#March
for submission in wsb.search('Daily Discussion Thread for '+ 'March', sort='new', time_filter='all', limit=1000):
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

#February
for submission in wsb.search('Daily Discussion Thread for '+ 'February', sort='new', time_filter='all', limit=1000):
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

#January
for submission in wsb.search('Daily Discussion Thread for '+ 'January', sort='new', time_filter='all', limit=1000):
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

posts_df.to_pickle('WSB_Posts')
posts_df.to_csv(r'posts.csv', mode = 'w')

comments_df = pd.DataFrame()
for post in posts_df.itertuples():
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