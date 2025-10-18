********** Automated Claims Eligibility – Full Multi-Week Plan **********
Week 1 – Project Setup & Initial Dataset - Done✅
--> Goals:
Set up folder structure - Done✅
Add sample dataset - Done✅
Create basic Python script to load and inspect data - Done✅
Push to GitHub

--> Tasks:
Folder structure:
automated-claims-eligibility/
├── data/
├── scripts/
├── README.md
├── requirements.txt
└── .gitignore
Sample dataset


Week 2 – Data Cleaning & Validation

Goals:

Handle missing values

Validate claim data

Generate a clean dataset

Tasks:

Add scripts/clean_claims.py

Check for missing/null values

Fill missing claim_status with "Pending"

Validate numeric columns (claim_amount ≥ 0)

Save cleaned dataset data/claims_cleaned.csv

Update README with instructions for cleaning script

Add automated checks in script for basic data validation

Week 3 – Exploratory Data Analysis (EDA)

Goals:

Visualize dataset trends

Generate summary statistics and plots

Tasks:

Python script: scripts/eda_claims.py

Count claims by status (Approved, Pending, Rejected)

Total and average claim amounts

Plot bar charts for claim counts by status

Plot time series of claims filed over dates

Dependencies: add matplotlib and seaborn to requirements.txt

Update README with EDA instructions

Week 4 – Feature Engineering

Goals:

Prepare dataset for future machine learning models

Tasks:

Add scripts/feature_engineering.py

Encode categorical columns (claim_status)

Generate new features (e.g., days_since_filed)

Save transformed dataset data/claims_features.csv

Update README with instructions for feature engineering

Week 5 – Eligibility Rules Engine (Basic Logic)

Goals:

Implement basic rules to determine claim eligibility

Use Python functions for decision-making

Tasks:

Add scripts/eligibility_rules.py

Rules example:

Claim_amount ≤ 1000 → Auto-approve

Claim_amount > 1000 → Manual review

Apply rules to dataset and save results to data/claims_eligibility.csv

Print summary: number of auto-approved vs manual review claims

Update README with eligibility rules description

Week 6 – Integration & Automation

Goals:

Combine scripts into a pipeline

Make it reproducible

Tasks:

Add scripts/run_pipeline.py

Steps: load → clean → feature engineering → eligibility

Save final output data/claims_final.csv

Print final summary

Optionally use Python’s logging module to log each step

Week 7 – Optional Machine Learning Prototype

Goals:

Build a basic ML model to predict claim approval

Evaluate performance

Tasks:

Add scripts/ml_model.py

Train a simple classifier (e.g., Decision Tree)

Split dataset into train/test

Print accuracy, confusion matrix

Save trained model using pickle for future use

Week 8 – Documentation & GitHub Presentation

Goals:

Make project GitHub-ready for showcase

Tasks:

Update README.md:

Add screenshots of outputs

Add project description, folder structure, dependencies, and pipeline steps

Add .gitignore (ignore __pycache__, .ipynb_checkpoints, datasets if needed)

Ensure all scripts run on any machine

Key GitHub Practices Throughout

Commit frequently with clear messages

Pull/rebase before pushing to avoid conflicts

Keep branches organized if adding new features

Tag releases for milestones (Week 1, Week 4, Week 8)
