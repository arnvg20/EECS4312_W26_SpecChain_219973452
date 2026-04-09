"""generates structured specs from personas"""
import json
import os
from groq import Groq

MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def load_personas():
    with open("personas/personas_auto.json", "r", encoding="utf-8") as f:
        return json.load(f)["personas"]


def build_prompt(personas):
    persona_text = json.dumps(personas, indent=2)

    prompt = f"""
You are a software requirements engineering assistant.

Using the following personas, automatically generate EXACTLY 10 functional requirements.

Return ONLY markdown text in this exact format:

# Requirement ID: FR1

- Description: ...
- Source Persona: ...
- Traceability: Derived from review group ...
- Acceptance Criteria: ...

Generate FR1 to FR10.

Personas:
{persona_text}
"""
    return prompt


def generate_spec():
    personas = load_personas()
    prompt = build_prompt(personas)

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    result = response.choices[0].message.content.strip()

    with open("spec/spec_auto.md", "w", encoding="utf-8") as f:
        f.write(result)

    print("Auto specification saved")


if __name__ == "__main__":
    generate_spec()
