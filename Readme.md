# Reddit Contributor Productivity Analysis

## Overview

This project focuses on understanding the productivity of contributors on reddit.org. The analysis involves scraping posts from specific subreddits, extracting key metrics, and performing an initial analysis on the subreddits "r/emacs" and "r/vim" within the time period from January 2023 to March 2023.

## Tasks

### 1. Scrape Reddit Posts

- **Subreddits:** "r/emacs" and "r/vim"
- **Time Period:** January 2023 to March 2023

### 2. Extract Metrics

For each post, five important metrics are extracted. The choice of metrics is determined based on the analysis goals.

### 3. Generate CSV File

A CSV file is generated with one line per post, containing an identifier and the values for the chosen metrics.

## Initial Analysis

1. **Generate Plots:**
   - Visualize differences in the distribution of the five metrics across "r/emacs" and "r/vim."

2. **Additional Analysis:**
   - Perform an additional type of analysis to better understand differences in contributor behavior between the two subreddits.

## Getting Started

### Prerequisites

- Python 3.x
- Required Python packages: `praw`, `pandas`, `matplotlib`, `seaborn`

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repo.git
    cd your-repo
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. **Obtain Reddit API Credentials:**
   - Create a Reddit App as described in the [Getting Reddit API Credentials](#getting-reddit-api-credentials) section.

2. **Update Credentials:**
   - Replace `'your_client_id'`, `'your_client_secret'`, and `'your_user_agent'` in the code with your actual Reddit API credentials.

3. **Run the Script:**

    ```bash
    python main.py
    ```

## Getting Reddit API Credentials

1. Create a Reddit account if you don't have one.

2. Go to your Reddit account settings and navigate to the "Developed Applications" section.

3. Create a new app and obtain the `client_id`, `client_secret`, and set the `user_agent`.

## Results

The analysis results, including CSV files and generated plots, can be found in the `data` directory.

## Contributing

Feel free to contribute to the project by submitting issues or pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
