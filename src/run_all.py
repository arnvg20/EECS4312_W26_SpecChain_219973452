"""runs the full pipeline end-to-end"""

import subprocess
import sys


def run_step(script_name, description):
    print(f"\nRunning: {description}")
    result = subprocess.run(
        [sys.executable, f"src/{script_name}"],
        check=True
    )
    print(f"Completed: {script_name}")


def main():
    print("Starting full automated pipeline...")

    # Step 1: collect/import reviews
    run_step("01_collect_or_import.py", "Collecting raw reviews")

    # Step 2: clean dataset
    run_step("02_clean.py", "Cleaning review dataset")

    # Step 3: automated review groups + personas
    run_step("05_personas_auto.py", "Generating automated review groups and personas")

    # Step 4: automated requirements specification
    run_step("06_spec_generate.py", "Generating automated specifications")

    # Step 5: automated validation tests
    run_step("07_tests_generate.py", "Generating automated tests")

    # Step 6: compute automated metrics
    run_step("08_metrics.py", "Computing automated metrics")

    print("\nFull automated pipeline completed successfully.")
    print("Files generated:")
    print("- data/review_groups_auto.json")
    print("- personas/personas_auto.json")
    print("- spec/spec_auto.md")
    print("- tests/tests_auto.json")
    print("- metrics/metrics_auto.json")


if __name__ == "__main__":
    main()
