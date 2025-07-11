# Isolation Forest for Outlier Detection in E-Commerce Data

This project applies the **Isolation Forest** algorithm to detect outliers in an e-commerce purchase dataset. The analysis helps identify anomalous customer behaviors that could impact business decisions.

## Dataset Overview

- The dataset contains customer purchase information, including demographics and transaction metrics.
- Columns include both **categorical** and **numerical** data.
- Null values are handled using appropriate strategies (mean for numerical, mode for categorical).
- Duplicate records are removed.

## Data Preprocessing

1. **Drop Unnecessary Columns** : Irrelevant or redundant data columns are eliminated.
2. **Categorical vs Numerical Separation** : Features are split for easier preprocessing.
3. **Missing Values Handling**:
   - Numerical: Replaced with mean.
   - Categorical: Filled using mode.

## Model Used: Isolation Forest

- Isolation Forest is a machine learning algorithm for **anomaly detection**.
- It isolates outliers instead of profiling normal data points, making it efficient for high-dimensional datasets.

### Why Isolation Forest?

- It’s particularly effective for large datasets.
- It works well without requiring a labeled dataset (unsupervised).
- Helps detect fraudulent users or unexpected behaviors in e-commerce.

## Business Impact

- Outliers can represent:
  - Fraudulent activities
  - High-value customers
  - Data entry errors
- Detecting and analyzing these helps:
  - Improve fraud detection systems
  - Enhance marketing targeting
  - Refine customer segmentation

## Example Code Snippet

```python
import pandas as pd     
from sklearn.model_selection import train_test_split
from sklearn.ensemble import IsolationForest
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv('ecommerce_purchase_data.csv')```

## Technologies Used
- Python

- Pandas

- scikit-learn (IsolationForest, train_test_split, metrics)
