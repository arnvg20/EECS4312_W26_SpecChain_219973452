"""imports or reads your raw dataset; if you scraped, include scraper here"""
from google_play_scraper import reviews_all
import json
import os

APP_ID = "bot.touchkin"

def collect_reviews():
    print("Collecting reviews from Google Play...")

    reviews = reviews_all(
        APP_ID,
        lang="en",
        country="ca"
    )[:5000]

    os.makedirs("data", exist_ok=True)

    with open("data/reviews_raw.jsonl", "w", encoding="utf-8") as f:
        for i, review in enumerate(reviews):
            item = {
                "id": i,
                "content": review["content"],
                "score": review["score"],
                "at": str(review["at"])
            }
            f.write(json.dumps(item) + "\n")

    print(f"Saved {len(reviews)} reviews")

if __name__ == "__main__":
    collect_reviews()
