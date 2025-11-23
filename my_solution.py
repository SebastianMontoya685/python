#!/usr/bin/env python3
"""
MY SOLUTION - Write your code here!
"""

from sample_data import REVIEWS


def main():
    """
    Your main function - implement your solution here.
    """
    # The REVIEWS data is already loaded for you!
    print(f"You have {len(REVIEWS)} reviews to analyze")
    
    # TODO: Your code goes here
    
    # EXAMPLE - How to access the data:
    # Each review is a tuple: (rating, review_text, timestamp, helpful_votes)
    # 
    # Example 1: Print the first review
    # first_review = REVIEWS[0]
    # rating, text, date, votes = first_review
    # print(f"Rating: {rating}, Text: {text}, Date: {date}, Votes: {votes}")
    #
    # Example 2: Loop through all reviews
    # for rating, text, date, votes in REVIEWS:
    #     print(f"{rating} stars: {text}")
    
    pass


if __name__ == "__main__":
    main()

