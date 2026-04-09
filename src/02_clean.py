"""cleans raw data & make clean dataset"""
import json
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from num2words import num2words

INPUT_FILE = "data/reviews_raw.jsonl"
OUTPUT_FILE = "data/reviews_clean.jsonl"

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()


def numbers_to_text(text):
    return re.sub(
        r'\d+',
        lambda m: num2words(int(m.group())),
        text
    )


def clean_text(text):
    if not text or not text.strip():
        return None

    # lowercase
    text = text.lower()

    # convert numbers to words
    text = numbers_to_text(text)

    # remove punctuation + special chars + emojis
    text = re.sub(r'[^\w\s]', ' ', text)
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)

    # remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()

    # tokenize
    words = text.split()

    # remove stopwords
    words = [w for w in words if w not in stop_words]

    # lemmatize
    words = [lemmatizer.lemmatize(w) for w in words]

    # remove extremely short reviews
    if len(words) < 3:
        return None

    return " ".join(words)


def clean_reviews():
    seen = set()
    cleaned = []

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        for line in f:
            review = json.loads(line)

            cleaned_text = clean_text(review.get("content", ""))

            if not cleaned_text:
                continue

            # remove duplicates
            if cleaned_text in seen:
                continue

            seen.add(cleaned_text)

            cleaned.append({
                "id": review["id"],
                "content": cleaned_text,
                "score": review["score"]
            })

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for review in cleaned:
            f.write(json.dumps(review) + "\n")

    print(f"Saved cleaned dataset with {len(cleaned)} reviews")


if __name__ == "__main__":
    clean_reviews()
