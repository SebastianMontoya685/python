# This is a python file that will perform different functions.
import sys
from collections import Counter


def parse_review_line(line):
    rating, review_text, timestamp, helpful_votes = line.split('|')
    return int(rating), review_text, timestamp, int(helpful_votes)

def main():
    for line in sys.stdin:
        review = parse_review_line(line.strip())
        print(review)


def calculate_statistics(reviews):
    total_reviews = len(reviews)

    # Calculating the average rating:
    all_ratings = [review[0] for review in reviews]
    total_rating = 0
    for review in reviews:
        rating = review[0]
        total_rating += rating

    average_rating = total_rating / total_reviews

    # Finding the most common rating:
    most_common_rating = Counter(all_ratings).most_common(1)[0][0]

    





if __name__ == "__main__":
    main()