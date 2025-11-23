# Python Practice Exercise - Product Review Analyzer

## Overview
You've been given a complete setup for a data analysis exercise. Your goal is to implement the functions in `practice_exercise.py` to process and analyze product reviews.

## What You Have
- `practice_exercise.py` - Your main file to implement
- `sample_reviews.txt` - Sample data with 20 product reviews

## File Format
Each review line follows this format:
```
Rating|Review_Text|Timestamp|Helpful_Votes
```

Example:
```
5|Absolutely amazing product! I love it and it works perfectly.|2024-12-10|28
```

## Tasks Breakdown

### Task 1: Parse Reviews ✅
Implement `parse_review_line()` to split each line into components.

**Hint:**
```python
def parse_review_line(line):
    parts = line.strip().split('|')
    # parts[0] = rating (convert to int)
    # parts[1] = review_text
    # parts[2] = timestamp
    # parts[3] = helpful_votes (convert to int)
    return tuple of values
```

### Task 2: Calculate Statistics 📊
Implement `calculate_statistics()` to compute:
- Total number of reviews
- Average rating
- Most common rating
- Reviews from past 30 days
- Top 5 most helpful reviews

**Hints:**
- Use `Counter` from collections for most common rating
- For average: `sum(ratings) / len(ratings)`
- For date filtering: parse dates and compare with `datetime`
- For top helpful: sort by helpful_votes

### Task 3: Rating Distribution 📈
Create a text-based bar chart showing how many reviews got each rating (1-5).

**Example Output:**
```
Rating Distribution:
1 ⭐: ████ (2 reviews)
2 ⭐: ██ (2 reviews)
3 ⭐: ████ (4 reviews)
4 ⭐: █████ (5 reviews)
5 ⭐: ███████ (7 reviews)
```

### Task 4: Sentiment Analysis 💭
Find reviews containing sentiment keywords:
- Positive: "love", "amazing"
- Negative: "hate", "terrible"

Count occurrences and categorize.

### Task 5: Bonus Challenges 🎯
- Find longest/shortest review
- Calculate average review length in words
- Generate comprehensive report dictionary

## Running Your Solution

```bash
python3 practice_exercise.py
```

## How to Test Your Code 🧪

### Method 1: Use the Test Script
I've created a test script for you:

```bash
python3 test_exercise.py
```

This will test your `parse_review_line` function automatically!

### Method 2: Quick Inline Testing
Add test code directly in your `practice_exercise.py`:

```python
# At the bottom of the file, before main()
if __name__ == "__main__":
    # Quick test for parse_review_line
    test_line = "5|Great product!|2024-12-10|28"
    rating, text, date, votes = parse_review_line(test_line)
    print(f"Rating: {rating}, Votes: {votes}")  # Should print: Rating: 5, Votes: 28
    
    main()
```

### Method 3: Interactive Python Shell
Test individual functions in the Python shell:

```bash
python3
```

Then in the shell:
```python
from practice_exercise import parse_review_line

# Test with a single line
line = "5|Amazing!|2024-12-10|28"
result = parse_review_line(line)
print(result)  # Should output: (5, 'Amazing!', '2024-12-10', 28)
```

### Debugging Tips
1. **Print everything**: Use `print()` to see what your variables contain
2. **Test small**: Test one function at a time
3. **Check types**: `print(type(variable))` to verify data types
4. **Read errors**: Error messages tell you exactly what's wrong

## Expected Output Structure

When complete, your program should output something like:

```
=== PRODUCT REVIEW ANALYSIS ===

Total Reviews: 20
Average Rating: 3.5
Most Common Rating: 5

Reviews from Past 30 Days: 8

Top 5 Most Helpful Reviews:
1. 5 stars (67 helpful votes): Waste of money...
2. 5 stars (52 helpful votes): Amazing quality...
...

Rating Distribution:
1 ⭐: ████ (2 reviews)
...

Sentiment Analysis:
Positive keywords: 8 occurrences
Negative keywords: 4 occurrences
...

Longest Review: 45 words
Shortest Review: 3 words
Average Review Length: 18 words

=== ANALYSIS COMPLETE ===
```

## Learning Objectives

By completing this exercise, you'll practice:
- ✅ File I/O (reading text files)
- ✅ String manipulation and parsing
- ✅ Working with dates and times
- ✅ Data structures (lists, tuples, dictionaries)
- ✅ Collections (Counter)
- ✅ Sorting and filtering data
- ✅ Text analysis and keyword extraction
- ✅ Creating formatted output
- ✅ Function design and modularity

## Tips for Success

1. **Start Simple**: Implement one function at a time
2. **Test Each Function**: Make sure each piece works before moving on
3. **Handle Edge Cases**: Empty strings, missing data, etc.
4. **Read Error Messages**: They'll guide you to the solution
5. **Use print()**: Debug by printing intermediate results

## Need Help?

If you're stuck on a specific part:
1. Try solving just that one function
2. Use print() statements to see what your data looks like
3. Break the problem into smaller pieces
4. Google specific errors or concepts

## Ready to Begin?

Open `practice_exercise.py` and start implementing! Good luck! 🚀

