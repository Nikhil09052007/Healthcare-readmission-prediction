# Hello viewer, in case if someone is seeing this:

**To prevent the complexities, I have made a specific dir for the better readabiltiy of the steps that I actually performed carrying the logic behind the logic and codes.** It is named as "docs", just left to your screen.


As this will contain all the information of project and an overall idea about the sceenarios which are running behind the code and dataset.

I'm building this as my personal project for a dataset based on the record of USA's Hospital Readmission.

 # Let's just have a theoritical knowledge of the term " Hospital Readmiisson" : **Hospital Readmission occurs when a patient is admitted to a hospital again for the same or a related health condition within a specific timeframe after being discharged from a previous hospital stay.**
# Scenarios: 

* Patient Safety: High readmission rates often indicate that a patient wasn't ready for discharge, didn't understand their discharge instructions, or didn't receive adequate follow-up care.

* Cost: In the US alone, preventable readmissions cost the healthcare system approximately $26 billion per year.

* Policy: Under laws like the ACA (Affordable Care Act) in the US, hospitals with higher-than-expected readmission rates for specific conditions (like heart failure, pneumonia, or diabetes) face financial penalties.

# My goal: ** I'll try to build a model to prevent this scenario listing using ML algorithms such as Regression and Classification.

## 📊 Dataset
- **Source:** UCI Machine Learning Repository (Diabetes 130-US Hospitals)
- **Size:** ~100,000 patient records
- **Features:** Lab results, medications, diagnoses, hospital admission/discharge info.
- **Target:** `readmitted` (Yes/No) and `days_to_readmit` (if applicable).

# Roadmap: Docs are organised in the similar format too. 
* Phase 1 → Problem Understanding & Dataset Acquisition (Done here already and data is in dir.)
* Phase 2 → Exploratory Data Analysis (EDA)
* Phase 3 → Data Cleaning & Preprocessing
* Phase 4 → Feature Engineering
* Phase 5 → Model Building (Track A: Classification)
* Phase 6 → Model Building (Track B: Regression)
* Phase 7 → Hyperparameter Tuning
* Phase 8 → Model Evaluation & Comparison
* Phase 9 → Interpretation (SHAP values, feature importance)
* Phase 10 → Final Report & Insights



I'll keep each directory and files speately that a simpler pipeline structure could be represented for the whole workflow.

