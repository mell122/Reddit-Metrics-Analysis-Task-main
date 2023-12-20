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

# Reddit API Date Limitation


## Overview

This document provides information regarding a crucial limitation associated with the Reddit API, which has been in effect since 2018. Users are advised to take note of the restrictions imposed on querying data based on specific dates.

This document aims to inform you about a significant limitation associated with the Reddit API that has been in effect since 2018. Please be aware that precise dates are no longer supported when querying the Reddit API.



## Impact on Data Queries

This limitation may affect users accustomed to querying the API for data with precise date requirements. It is advisable to adjust any existing processes or applications that rely on specific date queries to align with the revised timeframe constraints imposed by the Reddit API.

## Recommended Approach

To obtain the required information, it is recommended to utilize date ranges within the last three months when interacting with the Reddit API.

## Support and Assistance

For any queries or concerns related to this limitation, please feel free to reach out to the Reddit API support team for further assistance.

Thank you for your attention to this matter, and we appreciate your understanding as we work within the constraints set by the Reddit API.

*Note: Last three months should be used to obtain the needed information.*



## Date Limitation Details

Since 2018, the Reddit API no longer supports the retrieval of data with precise dates. Instead, users can only query data within a time frame ranging from the last month to the last three months. This limitation means that it is not possible to obtain information based on an exact date beyond this specified window.

## Implications

Users who rely on the Reddit API for querying data with specific date requirements should be aware of this limitation. Any existing processes or applications that depend on exact date queries should be adjusted to align with the revised timeframe constraints.

## Contact

For any inquiries or concerns related to this limitation, please reach out to the Reddit API support team for further assistance.

## Acknowledgment

We appreciate your understanding as we navigate and work within the constraints set by the Reddit API.


# Next Step of the project 

## Dockerization and Containerization

This document outlines the steps to Dockerize and containerize the project for easier deployment and scalability.

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Building the Docker Image](#building-the-docker-image)
- [Running the Docker Container](#running-the-docker-container)
- [Customization](#customization)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Overview

Dockerizing the project involves encapsulating the application and its dependencies into a Docker container, making it portable and easily deployable across different environments. This step enhances scalability, reproducibility, and simplifies deployment processes.

## Test Descriptions

Test get_top_posts Function:

Mocks the PRAW Reddit instance to simulate Reddit API calls.
Calls the function with a mock subreddit and checks if the returned posts contain expected metrics.
Test generate_csv Function:

Creates a sample post for testing.
Calls the function with the sample post and checks if the CSV file is generated at the expected path.

