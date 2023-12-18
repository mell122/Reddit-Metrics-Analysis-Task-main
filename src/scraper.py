import matplotlib.pyplot as plt
import seaborn as sns

# Load data from CSV files
dfs = {subreddit: pd.read_csv(f'{subreddit}_posts_data.csv') for subreddit in subreddits}

# Plotting
for metric in ['title_length', 'upvotes', 'num_comments']:
    plt.figure(figsize=(10, 6))
    for subreddit, df in dfs.items():
        sns.histplot(df[metric], kde=True, label=subreddit, alpha=0.5)
    
    plt.title(f'Distribution of {metric} across Subreddits')
    plt.xlabel(metric)
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()

# Additional analysis (e.g., comparing average post lengths)
average_title_length = {subreddit: df['title_length'].mean() for subreddit, df in dfs.items()}
print("Average Title Lengths:", average_title_length)
