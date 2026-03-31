
"""
Handling Missing Values in Numerical Features

--------------------------------------------------
Types of Imputation
--------------------------------------------------
1. Univariate Imputation:
   - Each feature is handled independently.
   - Examples: Mean, Median, Constant value.

2. Multivariate Imputation:
   - Uses relationships between variables.
   - Examples: KNN Imputer, MICE.

--------------------------------------------------
Techniques Covered
--------------------------------------------------

1. Mean / Median Imputation
   - Replace missing values with mean or median.
   - Median is preferred when outliers exist.
   - Fast and simple, but reduces variance.

2. Arbitrary Value Imputation
   - Replace missing values with extreme values (e.g., -1, 99, 999).
   - Helps models detect missingness patterns.
   - Can introduce artificial outliers.

3. End of Distribution Imputation
   - Replace missing values with extreme tail values:
     (mean + 3 * standard deviation)
   - Preserves distribution shape better than arbitrary values.

4. Random Sample Imputation
   - Replace missing values with random samples from existing values.
   - Preserves original distribution and variance.
   - Requires fixed random_state for reproducibility.

--------------------------------------------------
Key Observations
--------------------------------------------------
- Mean/Median reduces variance and weakens correlations.
- Arbitrary values create strong signals but distort distribution.
- End-of-distribution balances realism and signal.
- Random sampling best preserves original data structure.

--------------------------------------------------
Best Practice
--------------------------------------------------
- Always compare distributions before and after imputation.
- Choose method based on:
  → Missing data percentage
  → Presence of outliers
  → Model type
"""





import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer



# LOAD DATA

def load_data(path):
    df = pd.read_csv(path)
    print("Data Shape:", df.shape)
    return df



# ADD MISSING INDICATORS

def add_missing_flags(df, cols):
    for col in cols:
        df[col + "_missing"] = df[col].isnull().astype(int)
    return df



# MEAN/MEDIAN IMPUTATION

def mean_median_imputation(X_train, X_test):
    trf = ColumnTransformer([
        ("age_median", SimpleImputer(strategy="median"), ["Age"]),
        ("fare_mean", SimpleImputer(strategy="mean"), ["Fare"])
    ], remainder="passthrough")

    trf.fit(X_train)

    print("Median Age:", trf.named_transformers_["age_median"].statistics_)
    print("Mean Fare:", trf.named_transformers_["fare_mean"].statistics_)

    X_train = trf.transform(X_train)
    X_test = trf.transform(X_test)

    return X_train, X_test



# MAIN PIPELINE

def main():
    df = load_data("titanic_toy.csv")

    X = df.drop(columns=["Survived"])
    y = df["Survived"]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Add missing indicators
    X_train = add_missing_flags(X_train, ["Age", "Fare"])
    X_test = add_missing_flags(X_test, ["Age", "Fare"])

    # Apply imputation
    X_train, X_test = mean_median_imputation(X_train, X_test)

    print("Pipeline completed successfully!")



# RUN

if __name__ == "__main__":
    main()