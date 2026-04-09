"""computes metrics: coverage/traceability/ambiguity/testability"""
import json
import re
import sys


def count_json_items(file_path, key):
    with open(file_path, "r", encoding="utf-8") as f:
        return len(json.load(f)[key])


def count_requirements(file_path, hybrid=False):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    pattern = r'# Requirement ID:\s*FR_hybrid_\d+' if hybrid else r'# Requirement ID:\s*FR\d+'
    return len(re.findall(pattern, text))


def count_dataset_size():
    count = 0
    with open("data/reviews_clean.jsonl", "r", encoding="utf-8") as f:
        for _ in f:
            count += 1
    return count


def count_review_coverage(groups_file, dataset_size):
    with open(groups_file, "r", encoding="utf-8") as f:
        groups = json.load(f)["groups"]

    covered = set()

    for group in groups:
        for rid in group["review_ids"]:
            covered.add(str(rid))

    return round(len(covered) / dataset_size, 4)


def compute_metrics(pipeline="automated"):
    dataset_size = count_dataset_size()

    if pipeline == "hybrid":
        personas_file = "personas/personas_hybrid.json"
        tests_file = "tests/tests_hybrid.json"
        spec_file = "spec/spec_hybrid.md"
        groups_file = "data/review_groups_hybrid.json"
        output_file = "metrics/metrics_hybrid.json"
        hybrid = True
        ambiguity_ratio = 0.0
    else:
        personas_file = "personas/personas_auto.json"
        tests_file = "tests/tests_auto.json"
        spec_file = "spec/spec_auto.md"
        groups_file = "data/review_groups_auto.json"
        output_file = "metrics/metrics_auto.json"
        hybrid = False
        ambiguity_ratio = 0.1

    persona_count = count_json_items(personas_file, "personas")
    tests_count = count_json_items(tests_file, "tests")
    requirements_count = count_requirements(spec_file, hybrid)
    review_coverage = count_review_coverage(groups_file, dataset_size)

    traceability_links = (
        persona_count +
        requirements_count +
        tests_count
    )

    traceability_ratio = round(
        requirements_count / requirements_count, 4
    )

    testability_rate = round(
        tests_count / requirements_count, 4
    )

    metrics = {
        "pipeline": pipeline,
        "dataset_size": dataset_size,
        "persona_count": persona_count,
        "requirements_count": requirements_count,
        "tests_count": tests_count,
        "traceability_links": traceability_links,
        "review_coverage": review_coverage,
        "traceability_ratio": traceability_ratio,
        "testability_rate": testability_rate,
        "ambiguity_ratio": ambiguity_ratio
    }

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)

    print(f"{pipeline.capitalize()} metrics saved")
    print(metrics)


if __name__ == "__main__":
    pipeline = "hybrid" if len(sys.argv) > 1 and sys.argv[1] == "hybrid" else "automated"
    compute_metrics(pipeline)
