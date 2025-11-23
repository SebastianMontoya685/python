# My Solution - Quick Start Guide

## Files Created For You

1. **`my_solution.py`** - This is where YOU write your code!
2. **`sample_data.py`** - This contains the sample data to work with
3. **`sample_reviews.txt`** - Alternative data source (optional, for file reading practice)

## How to Use

### Quick Start
```bash
python3 my_solution.py
```

### The Data Structure

The `REVIEWS` data in `sample_data.py` is a list of tuples:

```python
REVIEWS = [
    (rating, review_text, timestamp, helpful_votes),
    (5, "Amazing product!", "2024-12-10", 28),
    (3, "It's okay", "2024-11-25", 5),
    ...
]
```

Each tuple contains:
- **rating**: Integer 1-5 (star rating)
- **review_text**: String (customer review)
- **timestamp**: String in "YYYY-MM-DD" format
- **helpful_votes**: Integer (number of helpful votes)

### How to Access the Data

In `my_solution.py`:

```python
from sample_data import REVIEWS

# Method 1: Access by index
first_review = REVIEWS[0]
rating, text, date, votes = first_review
print(f"Rating: {rating}, Votes: {votes}")

# Method 2: Loop through all reviews
for rating, text, date, votes in REVIEWS:
    print(f"{rating} stars: {text}")

# Method 3: Just get one piece
all_ratings = [review[0] for review in REVIEWS]
all_votes = [review[3] for review in REVIEWS]
```

## Your Challenge

Implement functions to calculate:

1. **Total number of reviews**
2. **Average rating** (sum of all ratings / total reviews)
3. **Most common rating**
4. **Reviews from past 30 days** (assume current date is 2024-12-15)
5. **Top 5 most helpful reviews** (sort by helpful_votes)
6. **Rating distribution** (how many 1-star, 2-star, etc.)
7. **Sentiment analysis** (count positive/negative keywords)

## Tips

- Import the data: `from sample_data import REVIEWS`
- Write functions, not everything in main()
- Use `print()` to debug and see your progress
- Test incrementally as you build

## Example Starter Code

```python
from sample_data import REVIEWS

def calculate_stats():
    # Get total reviews
    total = len(REVIEWS)
    print(f"Total reviews: {total}")
    
    # Calculate average rating
    ratings = [review[0] for review in REVIEWS]
    avg_rating = sum(ratings) / len(ratings)
    print(f"Average rating: {avg_rating:.2f}")

if __name__ == "__main__":
    calculate_stats()
```

## Ready?

Just run `python3 my_solution.py` and start coding! Good luck! 🐍


