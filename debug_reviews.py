#!/usr/bin/env python3
"""
Debug script to investigate review count issues
"""

import os
from dotenv import load_dotenv
from serpapi import GoogleSearch
import json

# Load environment variables
load_dotenv()

def debug_review_fetching():
    """Debug the review fetching process"""
    api_key = os.getenv('SERPAPI_KEY')
    if not api_key:
        print("❌ SERPAPI_KEY not found in environment variables")
        return
    
    app_id = "1113153706"  # American Express
    
    print(f"🔍 Debugging review fetch for American Express (ID: {app_id})")
    print("=" * 60)
    
    try:
        # Test with different review counts
        for num_reviews in [25, 50, 100]:
            print(f"\n📊 Requesting {num_reviews} reviews...")
            
            search = GoogleSearch({
                "engine": "apple_reviews",
                "product_id": app_id,
                "api_key": api_key,
                "num": num_reviews
            })
            
            results = search.get_dict()
            
            print(f"   Response keys: {list(results.keys())}")
            
            if "reviews" in results:
                reviews = results["reviews"]
                print(f"   ✅ Found {len(reviews)} reviews")
                
                # Check review content
                valid_reviews = 0
                empty_reviews = 0
                no_rating_reviews = 0
                
                for i, review in enumerate(reviews):
                    has_text = bool(review.get('text', '').strip())
                    has_rating = 'rating' in review and review['rating'] is not None
                    
                    if has_text and has_rating:
                        valid_reviews += 1
                    elif not has_text:
                        empty_reviews += 1
                    elif not has_rating:
                        no_rating_reviews += 1
                    
                    # Show first few reviews for debugging
                    if i < 3:
                        print(f"   Review {i+1}: Text: {'Yes' if has_text else 'No'}, Rating: {'Yes' if has_rating else 'No'}")
                        if has_text:
                            print(f"      Text: {review.get('text', '')[:100]}...")
                        if has_rating:
                            print(f"      Rating: {review.get('rating', 'N/A')}")
                
                print(f"   📈 Summary: {valid_reviews} valid, {empty_reviews} empty text, {no_rating_reviews} no rating")
                
            else:
                print(f"   ❌ No reviews found in response")
                if "error" in results:
                    print(f"   Error: {results['error']}")
                print(f"   Full response: {json.dumps(results, indent=2)[:300]}...")
                
    except Exception as e:
        print(f"❌ Error: {str(e)}")

def main():
    """Main debug function"""
    print("🐛 Review Count Debug Tool")
    print("=" * 60)
    
    debug_review_fetching()
    
    print("\n💡 Troubleshooting Tips:")
    print("1. Check your SerpAPI plan limits")
    print("2. Verify the app ID is correct")
    print("3. Some reviews might be filtered out automatically")
    print("4. Empty or invalid reviews might be excluded")

if __name__ == "__main__":
    main()
