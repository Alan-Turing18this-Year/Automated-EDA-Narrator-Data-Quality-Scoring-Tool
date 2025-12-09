<img width="1920" height="1080" alt="1" src="https://github.com/user-attachments/assets/24f98fd5-f0c4-46ab-b243-3c65dcf2b622" />
<img width="1920" height="1080" alt="2" src="https://github.com/user-attachments/assets/bec9141f-2ea4-4c8c-9a79-cbfa335a58d7" />
<img width="1920" height="1080" alt="3" src="https://github.com/user-attachments/assets/2fc72025-7b48-4ef0-8899-1cd6b572b058" />
<img width="1920" height="1080" alt="4" src="https://github.com/user-attachments/assets/8aaa4d32-a7d3-4528-92e3-27dde9fa24fe" />
<img width="1920" height="1080" alt="5" src="https://github.com/user-attachments/assets/3cbe67a9-aaf3-4b51-aeec-e00280c16113" />
<img width="1920" height="1080" alt="6" src="https://github.com/user-attachments/assets/ee43d952-aff8-4c6a-90ad-3e72345b019d" />
<img width="1920" height="1080" alt="7" src="https://github.com/user-attachments/assets/4665c6f1-db98-4d84-a024-114e06437b84" />
<img width="1920" height="1080" alt="8" src="https://github.com/user-attachments/assets/4ccc88ac-0636-4544-a321-193f5826f671" />
<img width="1920" height="1080" alt="9" src="https://github.com/user-attachments/assets/ea671bbd-6a6e-4eda-af94-33f35daf2b2b" />
<img width="1920" height="1080" alt="10" src="https://github.com/user-attachments/assets/839655ed-b3bf-4cec-97ff-1f11f00787e7" />


# DatasetSense: Automated EDA Narrator + Data Quality Scoring Tool
## 1. Project Overview
DatasetSense is a Python tool that performs **automated exploratory data analysis (EDA)** and computes a **dataset quality score (0–100)**. It generates **human-readable insights** and produces a **markdown report** summarizing dataset characteristics and quality.  

The project demonstrates **object-oriented programming (OOP)** concepts including **encapsulation, inheritance, polymorphism, composition, and dunder methods**.

---

## 📦 Features

### Automated EDA
- Statistical profiling (mean, std, quartiles)
- Categorical profiling (frequency distribution, unique ratio)
- Outlier detection summary
- Missing value analysis per feature

### Data Quality Intelligence
| Metric          | Basis                    | Weight |
| --------------- | ------------------------ | ------ |
| Missing Score   | % missing values         | 35%    |
| Duplicate Score | duplicate row %          | 15%    |
| Outlier Score   | detected outliers vs N   | 25%    |
| Balance Score   | categorical distribution | 25%    |
- Missing values, duplicates, outliers, balance score
-  💯 Final weighted score (0–100)
-  🔎 Quality verdict: Excellent / Good / Fair / Poor

### Natural-Language Narration
- Generates explanation of dataset shape, variability, missing values, outliers & verdict
- Converts analysis metrics into human-readable insights

### Automated Report Generation
- Markdown export (.md)
- CLI configurable output
- Integrates narratives + scores + stats into a clean report

---

## System Architecture (UML)

![Dataset UML](pics/dataset_uml.png)




---

## 4. Object-Oriented Design

| OOP Concept        | How it’s applied in your project                                                                                                                                                                             |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Classes**        | There are **6 core classes**: `DataLoader`, `Preprocessor`, `EDAAnalyzer` (base), `NumericAnalyzer`/`CategoricalAnalyzer` (children), `QualityScorer`, `Narrator`, `ReportBuilder`, and `DatasetPipeline`.  |
| **Encapsulation**  | Protected attributes (e.g., `_df`, `_eda`, `_scores`) are used in classes. Getters like `get_df()` in `Preprocessor` and `DataLoader` provide controlled access.                                            |
| **Inheritance**    | `NumericAnalyzer` and `CategoricalAnalyzer` **inherit** from `EDAAnalyzer`.                                                                                                                                 |
| **Polymorphism**   | `run_all()` is **overridden** in `NumericAnalyzer` and `CategoricalAnalyzer` to handle numeric vs categorical data differently.                                                                             |
| **Dunder Methods** | `DataLoader` has `__repr__`, `__eq__`, `__len__`; `DatasetPipeline` has `__repr__`.                                                                                                                         |
| **Composition**    | `DatasetPipeline` **contains/uses** instances of `DataLoader`, `Preprocessor`, `EDAAnalyzer`, `QualityScorer`, `Narrator`, `ReportBuilder`.                                                                 |


---

## 5. Project Structure

```
data-narrator/
├─ data/                    # CSV files and sample datasets
│  └─ sample.csv
├─ src/                     # Main modules (importable and reusable)
│  ├─ __init__.py
│  ├─ loader.py             # Loads CSV files
│  ├─ preprocessor.py       # Cleans and preprocesses data
│  ├─ eda_analyzer.py       # Numeric and categorical EDA analysis
│  ├─ quality_scorer.py     # Computes data quality scores
│  ├─ narrator.py           # Generates human-readable insights
│  ├─ report_builder.py     # Builds markdown reports
│  └─ orchestrator.py       # DatasetPipeline: orchestrates all classes
├─ demo.py                  # Ready-to-run mini demo for practical example
├─ tests/                   # Unit tests (optional)
├─ notebooks/               # Jupyter notebooks for exploration (optional)
├─ README.md                # Project documentation
└─ requirements.txt         # Python dependencies
```
# Dataset Facade UML

![Dataset UML](datasetsense_uml.png)

---

| Requirement                                  | Project Implementation                                                                                                                                                                                                                                                                                      |
| -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **At least 5 useful methods across modules** | Example methods: <br>1. `DataLoader.load()` – loads CSV <br>2. `Preprocessor.trim_strings()` – trims text columns <br>3. `NumericAnalyzer.run_all()` – numeric summary <br>4. `QualityScorer.overall_score()` – calculates weighted quality <br>5. `Narrator.generate()` – returns human-readable narrative |
| **Must be importable and reusable**          | All modules are in `src/` with proper `__init__.py`, allowing imports like: <br>`from src.loader import DataLoader`                                                                                                                                                                                         |
---

