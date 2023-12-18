import datetime
import praw
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

# Loading variables from env
env_client_id = os.getenv('client_id')
env_client_secret = os.getenv('client_secret')
env_user_agent = os.getenv('user_agent')

# Set up Reddit API credentials
reddit = praw.Reddit(client_id=env_client_id ,
                     client_secret= env_client_secret ,
                     user_agent= env_user_agent)

# Specify subreddit and time period
subreddits = ['emacs', 'vim']
start_date = datetime.datetime.utcnow() - datetime.timedelta(days=90)  # 3 months ago
end_date = datetime.datetime.utcnow()


# Function to get top posts and extract metrics
def get_top_posts(subreddit):
    posts = []
    for submission in reddit.subreddit(subreddit).top(time_filter='all', limit=None):
        if start_date <= datetime.datetime.utcfromtimestamp(submission.created_utc) <= end_date:
            post_metrics = {
                'post_id': submission.id,
                'title': submission.title,
                'score': submission.score,
                'num_comments': submission.num_comments,
                'created_utc': submission.created_utc,
                # Add more metrics as needed
            }
            posts.append(post_metrics)
    return posts

# Function to generate CSV file
def generate_csv(subreddit, posts):
    df = pd.DataFrame(posts)
    path="../data"
    df.to_csv(os.path.join(path, f'{subreddit}_posts.csv'), index=False)

# Get top posts for each subreddit
for subreddit in subreddits:
    posts = get_top_posts(subreddit)
    generate_csv(subreddit, posts)