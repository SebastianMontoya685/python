"""
PYTHON PRACTICE EXERCISE - Data Analysis & Processing Challenge

SCENARIO:
You work for an e-commerce company that wants to analyze product reviews. 
You've been given a text file containing product reviews, and your task is to 
write a Python program that processes and analyzes this data.

TASKS TO COMPLETE:
==================

1. Read the sample_reviews.txt file line by line

2. Parse each review (format: "Rating|Review_Text|Timestamp|Helpful_Votes")
   - Rating: integer 1-5
   - Review_Text: text description
   - Timestamp: YYYY-MM-DD format
   - Helpful_Votes: integer

3. Calculate and display:
   - Total number of reviews
   - Average rating
   - Most common rating
   - Reviews from the past 30 days (mock current date: 2024-12-15)
   - Top 5 most helpful reviews (by vote count)
   
4. Build a simple rating distribution visualization
   - Show count of each rating (1-5 stars)
   - Display as text-based bar chart

5. Extract insights:
   - Find reviews with "love", "hate", "terrible", or "amazing"
   - Count how many positive vs negative keywords appear
   - Store these in a structured format

BONUS CHALLENGES:
- Find the longest and shortest reviews
- Calculate the average review length (in words)
- Create a function that returns a summary report as a dictionary

RESTRICTIONS:
- Use only Python standard library (no external dependencies)
- Write clean, well-commented code
- Handle edge cases (empty reviews, missing data, etc.)
- Make your code reusable with functions

GOOD LUCK! 🐍
"""

import sys
from datetime import datetime, timedelta
from collections import Counter


def parse_review_line(line):
    """
    Parse a single review line into its components.
    Returns a tuple: (rating, review_text, timestamp, helpful_votes)
    """
    # TODO: Implement this function
    # Hint: Use line.split('|')
    rating, review_text, timestamp, helpful_votes = line.split('|')

    return int(rating), review_text, timestamp, int(helpful_votes)



# 3. Calculate and display:
#    - Total number of reviews
#    - Average rating
#    - Most common rating
#    - Reviews from the past 30 days (mock current date: 2024-12-15)
#    - Top 5 most helpful reviews (by vote count)
def calculate_statistics(reviews):
    """
    Calculate statistics from the reviews list.
    Returns a dictionary with various stats.
    """
    # TODO: Implement statistics calculation
    # Calculating the total number of reviews:
    total_reviews = len(reviews)
    # Calculating the average rating:
    for rating in reviews:
        
    pass


def create_rating_distribution(reviews):
    """
    Create a text-based bar chart for rating distribution.
    Print it out nicely formatted.
    """
    # TODO: Implement rating distribution visualization
    pass


def analyze_sentiment(reviews):
    """
    Analyze positive/negative keywords in reviews.
    Returns a dictionary with counts.
    """
    # TODO: Implement sentiment keyword analysis
    pass


def generate_report(reviews):
    """
    Generate a comprehensive report.
    Returns a dictionary with all analysis results.
    """
    # TODO: Implement comprehensive report generation
    pass


def main():
    """
    Main function to run the review analysis.
    """
    # TODO: Implement main logic
    
    # 1. Read the sample_reviews.txt file
    # 2. Parse all reviews
    # 3. Calculate statistics
    # 4. Display results
    # 5. Generate final report
    
    pass


if __name__ == "__main__":
    # ========================================
    # TESTING AREA - Uncomment to test as you go
    # ========================================
    
    # Test parse_review_line
    # test_line = "5|Absolutely amazing product! I love it and it works perfectly.|2024-12-10|28"
    # result = parse_review_line(test_line)
    # print("Test result:", result)
    # print(f"Rating type: {type(result[0])}, Votes type: {type(result[3])}")
    
    # Test reading and parsing all reviews
    # with open("sample_reviews.txt", "r") as f:
    #     lines = f.readlines()
    # reviews = [parse_review_line(line) for line in lines if line.strip()]
    # print(f"Parsed {len(reviews)} reviews")
    # print(f"First review: {reviews[0]}")
    
    # ========================================
    # Run the main program
    # ========================================
    main()

