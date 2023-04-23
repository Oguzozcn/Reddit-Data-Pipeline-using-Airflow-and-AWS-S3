from os import access
import praw
import pandas as pd 
import json
from datetime import datetime
import s3fs

#can be used to scrape different elements   (just implement under submission loop)        
# print(submission.title)
# print(submission.id)
# print(submission.author)
# print(submission.created_utc)
# print(submission.score)
# print(submission.upvote_ratio)
# print(submission.url)
           


def run_reddit_etl():

    user_agent = "Scrapper 1.0 by /u/YOUR_USERNAME"
    reddit = praw.Reddit(
        client_id= "YOUR CLIENT ID",
        client_secret = "YOUR CLIENT SECRET KEY",
        user_agent= user_agent
        )
    

    reddit_list = []
    for submission in reddit.subreddit('politics').hot(limit=20):
        submission_data = {"title": submission.title,
                       "id": submission.id,
                       "author": submission.author.name,
                       "created_utc": submission.created_utc,
                       "score": submission.score,
                       "upvote_ratio": submission.upvote_ratio,
                       "url": submission.url
                      }
        reddit_list.append(submission_data)
    return reddit_list

reddit_list = run_reddit_etl()
df = pd.DataFrame(reddit_list)
df.to_csv('reddit_data.csv') # local file test run with notebook or cmd to see the result
    
#df.to_csv('YOUR-S3-BUCKET/reddit_data.csv')