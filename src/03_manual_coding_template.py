"""creates/updates coding table template + instructions"""

import json
import os


def get_manual_group_template():
    return {
        "groups": [
            {
                "group_id": "G1",
                "theme": "Example theme",
                "review_ids": [],
                "example_reviews": [],
                "notes": "Manually refined from raw review evidence"
            }
        ]
    }


def main():
    template = get_manual_group_template()

    os.makedirs("data", exist_ok=True)

    with open("data/manual_coding_template.json", "w", encoding="utf-8") as f:
        json.dump(template, f, indent=2)

    print("Manual coding template created successfully.")
    print("Saved to data/manual_coding_template.json")


if __name__ == "__main__":
    main()
