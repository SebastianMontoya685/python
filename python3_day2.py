#!/usr/bin/env python3

def analyse_reviews(reviews):
    review_dictionary = {"positive": 0, "negative": 0, "neutral": 0}
    positive_keywords = ["good", "great", "excellent", "amazing", "fantastic", "love"]
    negative_keywords = ["bad", "poor", "terrible", "awful", "hate"]
    positive_count = 0
    negative_count = 0
    neutral_count = 0
    for review in reviews:
        review = review.lower()
        if any(keyword in review for keyword in positive_keywords) and any(keyword in review for keyword in negative_keywords):
            neutral_count += 1
        elif any(keyword in review for keyword in positive_keywords):
            positive_count += 1
        elif any(keyword in review for keyword in negative_keywords):
            negative_count += 1
        else:
            neutral_count += 1

    review_dictionary["positive"] = positive_count
    review_dictionary["negative"] = negative_count
    review_dictionary["neutral"] = neutral_count
    return review_dictionary


def main():
    reviews = [
    "I love this product, it is fantastic!",
    "The quality is terrible and I hate it.",
    "It's okay, does the job.",
    "Absolutely excellent service.",
    "Not bad, but could be better.",
    "Awful experience, very poor support.",
    "Amazing! Great value for the price.",
    "Nothing special, just average.",
    "Good, but not excellent.",
    "Terrible, would not recommend."
]

    review_dictionary = analyse_reviews(reviews)
    print(review_dictionary)

if __name__ == "__main__":
    main();