"""automated persona generation pipeline"""
import os
import json
from groq import Groq

MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"

client = Groq(api_key="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")


def load_reviews(limit=100):
    reviews = []
    with open("data/reviews_clean.jsonl", "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            if i >= limit:
                break
            item = json.loads(line)
            reviews.append({
                "id": item["id"],
                "content": item["content"]
            })
    return reviews


def build_prompt(reviews):
    review_text = "\n".join(
        [f'ID {r["id"]}: {r["content"]}' for r in reviews]
    )

    prompt = f"""
You are a software requirements engineering assistant.

Given the following cleaned app reviews for Wysa, automatically:
1. Group reviews into 5 meaningful themes
2. Generate 5 personas based on those themes

Return ONLY valid JSON in this exact format:

{{
  "groups": [...],
  "personas": [...]
}}

Each group must contain:
- group_id
- theme
- review_ids
- example_reviews

Each persona must contain:
- id
- name
- description
- derived_from_group
- goals
- pain_points
- context
- constraints
- evidence_reviews

Reviews:
{review_text}
"""
    return prompt


def save_prompt(prompt):
    os.makedirs("prompts", exist_ok=True)
    with open("prompts/prompt_auto.json", "w", encoding="utf-8") as f:
        json.dump({"prompt": prompt}, f, indent=2)


def generate():
    reviews = load_reviews()
    prompt = build_prompt(reviews)
    save_prompt(prompt)

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    result = response.choices[0].message.content

    parsed = json.loads(result)

    os.makedirs("data", exist_ok=True)
    os.makedirs("personas", exist_ok=True)
def generate():
    reviews = load_reviews()
    prompt = build_prompt(reviews)
    save_prompt(prompt)

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    # Get raw response
    result = response.choices[0].message.content.strip()

    print("RAW MODEL OUTPUT:")
    print(result)

    # Remove markdown code blocks if model returns them
    result = result.replace("```json", "").replace("```", "").strip()

    # Extract only JSON object
    start = result.find("{")
    end = result.rfind("}") + 1

    if start == -1 or end == 0:
        raise ValueError("No valid JSON object found in model response")

    json_text = result[start:end]

    # Parse cleaned JSON
    parsed = json.loads(json_text)

    os.makedirs("data", exist_ok=True)
    os.makedirs("personas", exist_ok=True)

    with open("data/review_groups_auto.json", "w", encoding="utf-8") as f:
        json.dump({"groups": parsed["groups"]}, f, indent=2)

    with open("personas/personas_auto.json", "w", encoding="utf-8") as f:
        json.dump({"personas": parsed["personas"]}, f, indent=2)

    print("Auto review groups saved")
    print("Auto personas saved")
    print("Prompt saved")


if __name__ == "__main__":
    generate()
