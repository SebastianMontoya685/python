"""
Quick test script to test your parse_review_line function.
Run this to verify your implementation is working correctly.
"""

from practice_exercise import parse_review_line


def test_parse_review_line():
    """Test the parse_review_line function with sample data."""
    
    print("Testing parse_review_line function...")
    print("-" * 50)
    
    # Test with a sample line
    test_line = "5|Absolutely amazing product! I love it and it works perfectly.|2024-12-10|28"
    
    print(f"Input: {test_line}")
    
    try:
        rating, review_text, timestamp, helpful_votes = parse_review_line(test_line)
        
        print(f"\nParsed Results:")
        print(f"  Rating: {rating} (type: {type(rating).__name__})")
        print(f"  Review: {review_text}")
        print(f"  Timestamp: {timestamp}")
        print(f"  Helpful Votes: {helpful_votes} (type: {type(helpful_votes).__name__})")
        
        # Validate the results
        assert rating == 5, f"Expected rating 5, got {rating}"
        assert isinstance(rating, int), "Rating should be an integer"
        assert helpful_votes == 28, f"Expected 28 helpful votes, got {helpful_votes}"
        assert isinstance(helpful_votes, int), "Helpful votes should be an integer"
        assert timestamp == "2024-12-10", f"Expected timestamp 2024-12-10, got {timestamp}"
        
        print("\n✅ All tests passed!")
        return True
        
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_multiple_lines():
    """Test parsing multiple lines from the file."""
    
    print("\n\nTesting with multiple lines from sample_reviews.txt...")
    print("-" * 50)
    
    try:
        with open("sample_reviews.txt", "r") as f:
            lines = f.readlines()
        
        print(f"Parsing {len(lines)} reviews...")
        
        reviews = []
        for i, line in enumerate(lines, 1):
            if line.strip():  # Skip empty lines
                try:
                    parsed = parse_review_line(line)
                    reviews.append(parsed)
                    print(f"  ✅ Line {i}: Rating {parsed[0]}, Votes {parsed[3]}")
                except Exception as e:
                    print(f"  ❌ Line {i} failed: {e}")
        
        print(f"\nSuccessfully parsed {len(reviews)} reviews!")
        print(f"First review: Rating={reviews[0][0]}, Text='{reviews[0][1][:40]}...'")
        print(f"Last review: Rating={reviews[-1][0]}, Text='{reviews[-1][1][:40]}...'")
        
        return True
        
    except FileNotFoundError:
        print("❌ sample_reviews.txt not found!")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    print("=" * 60)
    print("PYTHON EXERCISE TESTING SCRIPT")
    print("=" * 60)
    
    # Run tests
    test1 = test_parse_review_line()
    test2 = test_multiple_lines()
    
    print("\n" + "=" * 60)
    if test1 and test2:
        print("🎉 ALL TESTS PASSED! Your function is working correctly!")
    else:
        print("⚠️  Some tests failed. Check the output above.")
    print("=" * 60)

