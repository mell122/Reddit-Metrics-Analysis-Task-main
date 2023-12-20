import datetime
import os
import unittest
from unittest.mock import patch
from scraper import get_top_posts, generate_csv

class TestRedditScraper(unittest.TestCase):
    
    @patch('scraper.praw.Reddit')
    def test_get_top_posts(self, mock_reddit):
        # Mock the praw Reddit instance
        mock_subreddit = mock_reddit.return_value.subreddit.return_value
        mock_submission = mock_subreddit.top.return_value.__iter__.return_value
        mock_submission.return_value.created_utc = datetime.datetime.utcnow().timestamp()

        # Call the function with a mock subreddit
        posts = get_top_posts('test_subreddit')

        # Make assertions about the results
        self.assertEqual(len(posts), 1)
        self.assertIn('post_id', posts[0])
        self.assertIn('title', posts[0])
        self.assertIn('score', posts[0])
        self.assertIn('num_comments', posts[0])
        self.assertIn('created_utc', posts[0])

    def test_generate_csv(self):
        # Create a sample post for testing
        sample_post = {
            'post_id': '123456',
            'title': 'Test Title',
            'score': 42,
            'num_comments': 5,
            'created_utc': datetime.datetime.utcnow().timestamp()
        }

        # Call the function with the sample post
        generate_csv('test_subreddit', [sample_post])

        # Check if the CSV file is created
        file_path = '../data/test_subreddit_posts.csv'
        self.assertTrue(os.path.exists(file_path))

        # You can add more assertions based on your specific requirements

if __name__ == '__main__':
    unittest.main()
