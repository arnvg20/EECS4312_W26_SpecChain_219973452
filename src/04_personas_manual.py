"""creates manual persona template"""

import json
import os


def get_persona_template():
    return {
        "personas": [
            {
                "id": "P1",
                "name": "Example Persona",
                "description": "Example user persona derived from manual review groups.",
                "derived_from_group": "G1",
                "goals": [],
                "pain_points": [],
                "context": [],
                "constraints": [],
                "evidence_reviews": []
            }
        ]
    }


def main():
    template = get_persona_template()

    os.makedirs("personas", exist_ok=True)

    with open("personas/personas_manual_template.json", "w", encoding="utf-8") as f:
        json.dump(template, f, indent=2)

    print("Manual persona template created successfully.")
    print("Saved to personas/personas_manual_template.json")


if __name__ == "__main__":
    main()
