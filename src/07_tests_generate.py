"""generates tests from specs"""
import json
import os
import re
from groq import Groq

MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def load_spec():
    with open("spec/spec_auto.md", "r", encoding="utf-8") as f:
        return f.read()


def extract_requirement_ids(spec_text):
    return re.findall(r'FR\d+', spec_text)


def build_prompt(spec_text):
    prompt = f"""
You are a software requirements engineering assistant.

Based on the following requirements specification, generate exactly one validation test
scenario for each requirement.

Return ONLY valid JSON in this exact format:

{{
  "tests": [
    {{
      "test_id": "T1",
      "requirement_id": "FR1",
      "scenario": "...",
      "steps": ["...", "..."],
      "expected_result": "..."
    }}
  ]
}}

Requirements:
{spec_text}
"""
    return prompt


def generate_tests():
    spec_text = load_spec()
    prompt = build_prompt(spec_text)

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    result = response.choices[0].message.content.strip()

    result = result.replace("```json", "").replace("```", "").strip()

    start = result.find("{")
    end = result.rfind("}") + 1
    json_text = result[start:end]

    parsed = json.loads(json_text)

    with open("tests/tests_auto.json", "w", encoding="utf-8") as f:
        json.dump(parsed, f, indent=2)

    print("Auto tests saved")


if __name__ == "__main__":
    generate_tests()
