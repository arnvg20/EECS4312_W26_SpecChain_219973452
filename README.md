# EECS4312_W26_SpecChain

Application: Wysa

Data Collection Method:
- Reviews were collected from the Google Play Store using `python src/01_collect_or_import.py`
- Reviews were cleaned using `python src/02_clean.py`
- Cleaning included duplicate removal, punctuation and special character removal, stop-word removal, lowercase conversion, and lemmatization

Dataset:
- reviews_raw.jsonl contains the collected reviews.
- reviews_clean.jsonl contains the cleaned dataset.
- The original dataset contains 5000 reviews.
- The cleaned dataset contains 3927 reviews.

Repository Structure:
- data/ contains datasets and review groups
- personas/ contains persona files
- spec/ contains specifications
- tests/ contains validation tests
- metrics/ contains all metric files
- prompts/ contains the saved automated prompt
- src/ contains executable Python scripts
- reflection/ contains the final reflection

How to Run:
1. python src/00_validate_repo.py
2. python src/02_clean.py
3. python src/run_all.py
4. python src/08_metrics.py
5. python src/08_metrics.py hybrid
6. Open metrics/metrics_summary.json for comparison results
