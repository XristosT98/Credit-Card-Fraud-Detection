# Credit Card Fraud Detection & Unsupervised Clustering

This repository contains a comprehensive Data Mining and Machine Learning project analyzing a dataset of **1,000,000 credit card transactions** using **Weka**. The study covers both Supervised (Classification) and Unsupervised (Clustering) learning techniques, focusing heavily on real-world banking constraints and risk management.

---

## Project Overview & The "Accuracy Paradox"
Fraud detection datasets are characterized by extreme class imbalance, where fraudulent transactions represent only a tiny fraction (~9%) of the total volume. This creates the **Accuracy Paradox**: a naive model predicting "no fraud" achieves ~91% accuracy but has zero business value as it fails to catch any fraud. 

To overcome this, our objective was not to maximize raw accuracy, but to optimize **Recall** (catching 100% of frauds) and control **Precision / False Positives** (minimizing customer friction and unnecessary alerts).

---

## Methodology & Preprocessing
Given the scale of 1,000,000 records and the memory constraints of Weka, a rigorous preprocessing and validation pipeline was implemented:
1. **Data Type Conversion (`NumericToNominal`):** Converted target and binary features to nominal variables to enable classification and confusion matrix generation.
2. **Class Imbalance Handling (`SpreadSubsample`):** Applied undersampling to establish a strict 1:1 class ratio (50% fraud, 50% legal) in the training folds. To prevent **Data Leakage**, this was executed strictly inside a `FilteredClassifier` during 10-fold Cross-Validation.
3. **Advanced Transformations for Naive Bayes:** 
   * Tested logarithmic scaling (`log(A+1)`) to handle skewed distributions.
   * Applied Supervised Discretization (`Discretize`) to optimize probability boundaries, significantly boosting performance.

---

## Models Evaluated & Key Results

| Model / Experiment | Recall (TP Rate) | Precision | ROC Area (AUC) | Key Business takeaway |
| :--- | :---: | :---: | :---: | :--- |
| **Random Forest** (Baseline) | 1.000 | 0.999 | 1.000 | Flawless detection (only 1 missed fraud, 66 false alarms). |
| **Cost-Sensitive J48** (1:100) | 1.000 | 0.999 | 1.000 | Balances risk appetite by heavily penalizing missed frauds (only 3 missed, 92 false alarms). |
| **J48 (Decision Tree)** | 1.000 | 0.999 | 1.000 | Excellent "White Box" interpretability with clear business rule extraction. |
| **Naive Bayes (Discretization)**| 1.000 | 0.688 | 1.000 | Solid probabilistic baseline after proper bucketing. |

### ⚠️ Critical Finding on Data Nature
Both Random Forest and J48 achieved near-perfect results (AUC ~1.0). In real-world noisy environments, such perfection is virtually impossible. This strongly indicates that the dataset (`card_transdata.csv`) is **synthetic**, generated via strict mathematical rules (e.g., *Online Order + High Price Ratio + Wrong PIN = Fraud*), which decision tree algorithms fully decoded.

---

## Unsupervised Clustering Analysis
To explore data geometry without labels, **SimpleKMeans** and **DBSCAN** were deployed:
* **Fraud as "Mimicry" (DBSCAN):** Results proved that fraudsters do not act as isolated noise/outliers; rather, they successfully mimic the behavior of legitimate users, hiding inside dense data regions.
* **High-Risk Geometric Zones (K-Means):** Utilizing the Elbow Method ($k=10$), K-Means successfully isolated a high-risk core (Cluster 2 with ~49.5% fraud rate driven by high `ratio_to_median_purchase_price`) alongside low-risk **"White Lists"** (Clusters 0, 4, 6, 7, 9 with >98% legal transactions) which can bypass heavy real-time checks.

---

## Repository Structure
* `reports/`: Contains the full project report in PDF format (`project_report.pdf`).
* `outputs/`: Contains the raw text logs and evaluation outputs from Weka (`.txt` files for Cross-Validation, Confusion Matrices, and Tree structures).

---

