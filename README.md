# EECS4312_W26_SpecChain

## Application
**Wysa** – Mental Health Support App

This project analyzes user reviews collected from the Google Play Store for the Wysa application.  
The objective is to build and compare **manual**, **automated**, and **hybrid requirements engineering pipelines** for persona generation, software requirement specification, validation test generation, and metric comparison.

---

## Data Collection Method
- Reviews were collected from the Google Play Store using:

```bash
python src/01_collect_or_import.py
```

- Reviews were cleaned using:

```bash
python src/02_clean.py
```

Cleaning included:
- duplicate removal
- punctuation and special character removal
- stop-word removal
- lowercase conversion
- lemmatization

---

## Dataset
- `reviews_raw.jsonl` contains the collected raw reviews
- `reviews_clean.jsonl` contains the cleaned dataset
- Original dataset size: **5000 reviews**
- Final cleaned dataset size: **3927 reviews**

---

## Repository Structure
- `data/` → datasets and review groups
- `personas/` → persona files
- `spec/` → requirement specifications
- `tests/` → validation tests
- `metrics/` → all metric files
- `prompts/` → saved automated prompt
- `src/` → executable Python scripts
- `reflection/` → final reflection

---

## Groq API Key Setup
Before running the automated pipeline, set the Groq API key as an environment variable.

For **tcsh / csh**:

```tcsh
setenv GROQ_API_KEY "your_groq_api_key"
```

For **bash / zsh**:

```bash
export GROQ_API_KEY="your_groq_api_key"
```

---

## How to Run

### 1. Validate repository
```bash
python src/00_validate_repo.py
```

### 2. Create manual coding template (optional helper)
```bash
python src/03_manual_coding_template.py
```

This generates a starter manual coding template file for manual review grouping.

### 3. Clean dataset
```bash
python src/02_clean.py
```

### 4. Set the GROQ_API_KEY environment variable

### 5. Run full automated pipeline
```bash
python src/run_all.py
```

### 6. Generate automated metrics
```bash
python src/08_metrics.py
```

### 7. Generate hybrid metrics
```bash
python src/08_metrics.py hybrid
```

### 8. View comparison results
Open:

```text
metrics/metrics_summary.json
```
