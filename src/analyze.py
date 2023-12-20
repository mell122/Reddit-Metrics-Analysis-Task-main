import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# Load Emacs data from the parent directory/data
emacs_data = pd.read_csv('../data/emacs_posts.csv')

# Load Vim data from the parent directory/data
vim_data = pd.read_csv('../data/vim_posts.csv')


# Plotting metrics
sns.boxplot(x='subreddit', y='score', data=pd.concat([emacs_data.assign(subreddit='emacs'), vim_data.assign(subreddit='vim')]))
plt.title('Distribution of Scores')
plt.show()

# Add more plots for other metrics

# Additional analysis
# You may want to compare the average scores, comment counts, etc., between the two subreddits using statistical tests.
# Example:
from scipy.stats import ttest_ind

t_stat, p_value = ttest_ind(emacs_data['score'], vim_data['score'])
print(f'T-test for scores: t-statistic={t_stat}, p-value={p_value}')
