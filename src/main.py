import praw
import pandas as pd

# Set up Reddit API credentials
reddit = praw.Reddit(client_id='_1puKAM7Cs6wEl8H1o-Oqg',
                     client_secret='_9xtMfzYdUuwTWJ0MqRA5SXj2PBxQQ',
                     user_agent='personal use script')

# Specify subreddit and time period
subreddits = ['emacs', 'vim']
time_period = ('01/2023', '03/2023')

# Function to scrape posts and extract metrics
def scrape_subreddit(subreddit_name):
    subreddit = reddit.subreddit(subreddit_name)
    posts_data = []
    
    for submission in subreddit.submissions(start=time_period[0], end=time_period[1]):
        # Choose 5 metrics to extract (e.g., title length, upvotes, comments count, etc.)
        post_metrics = {
            'id': submission.id,
            'title_length': len(submission.title),
            'upvotes': submission.score,
            'num_comments': submission.num_comments,
            'created_utc': submission.created_utc,
            'author': submission.author.name
            # Add more metrics as needed
        }
        
        posts_data.append(post_metrics)
    
    return posts_data

# Scrape data for each subreddit
subreddit_data = {}
for subreddit_name in subreddits:
    subreddit_data[subreddit_name] = scrape_subreddit(subreddit_name)

# Convert data to Pandas DataFrame
dfs = {subreddit: pd.DataFrame(data) for subreddit, data in subreddit_data.items()}

# Save data to CSV files
for subreddit, df in dfs.items():
    df.to_csv(f'{subreddit}_posts_data.csv', index=False)
