"""checks required files/folders exist"""

import os


REQUIRED_FILES = [
    # data
    "data/reviews_raw.jsonl",
    "data/reviews_clean.jsonl",
    "data/dataset_metadata.json",
    "data/review_groups_manual.json",
    "data/review_groups_auto.json",
    "data/review_groups_hybrid.json",

    # personas
    "personas/personas_manual.json",
    "personas/personas_auto.json",
    "personas/personas_hybrid.json",

    # specifications
    "spec/spec_manual.md",
    "spec/spec_auto.md",
    "spec/spec_hybrid.md",

    # tests
    "tests/tests_manual.json",
    "tests/tests_auto.json",
    "tests/tests_hybrid.json",

    # metrics
    "metrics/metrics_manual.json",
    "metrics/metrics_auto.json",
    "metrics/metrics_hybrid.json",
    "metrics/metrics_summary.json",

    # prompts
    "prompts/prompt_auto.json",

    # scripts
    "src/run_all.py",
    "src/00_validate_repo.py"
]


def validate_repo():
    print("Checking repository structure...")

    missing = []

    for file_path in REQUIRED_FILES:
        if os.path.exists(file_path):
            print(f"{file_path} found")
        else:
            print(f"{file_path} missing")
            missing.append(file_path)

    print("Repository validation complete")

    if missing:
        print("\nMissing files:")
        for item in missing:
            print("-", item)
    else:
        print("\nAll required files and folders exist.")


if __name__ == "__main__":
    validate_repo()
