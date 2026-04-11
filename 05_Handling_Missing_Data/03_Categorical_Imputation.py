
"""
Handling Missing Values in Categorical Features

--------------------------------------------------
Techniques Covered
--------------------------------------------------

1. Most Frequent Value (Mode) Imputation
   - Replace missing values with the most frequent category.
   - Suitable when missing data is small and random (MCAR).

   Advantages:
   - Simple and fast
   - Works well with small missing percentages

   Disadvantages:
   - Reduces variability
   - May distort relationships if missingness is not random


2. Missing Category Imputation
   - Replace missing values with a new label (e.g., "Missing").

   Advantages:
   - Preserves all data
   - Captures missingness as a signal for the model

   Disadvantages:
   - Adds artificial category
   - May cause overfitting if missing values are rare


--------------------------------------------------
Best Practices
--------------------------------------------------
- Always analyze missing percentage before choosing method
- Compare target distribution before and after imputation
- Use missing indicators when necessary
- Prefer pipeline-based implementation (sklearn)

"""



import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer



# LOAD DATA

def load_data(path):
    df = pd.read_csv(path, usecols=['GarageQual', 'FireplaceQu', 'SalePrice'])
    print("Data Shape:", df.shape)
    return df



# ADD MISSING INDICATORS

def add_missing_flags(df, cols):
    for col in cols:
        df[col + "_missing"] = df[col].isnull().astype(int)
    return df



# MODE IMPUTATION

def mode_imputation(X_train, X_test):
    imputer = SimpleImputer(strategy='most_frequent')

    imputer.fit(X_train)

    print("Mode Values:", imputer.statistics_)

    X_train = imputer.transform(X_train)
    X_test = imputer.transform(X_test)

    return X_train, X_test



# MISSING CATEGORY IMPUTATION

def missing_category_imputation(X_train, X_test):
    imputer = SimpleImputer(strategy='constant', fill_value='Missing')

    imputer.fit(X_train)

    X_train = imputer.transform(X_train)
    X_test = imputer.transform(X_test)

    return X_train, X_test



# MAIN PIPELINE

def main():
    df = load_data("train.csv")

    X = df.drop(columns=['SalePrice'])
    y = df['SalePrice']

    # Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Add missing indicators
    X_train = add_missing_flags(X_train, ['GarageQual', 'FireplaceQu'])
    X_test = add_missing_flags(X_test, ['GarageQual', 'FireplaceQu'])

    # Choose ONE method:
    
    # 1. Mode Imputation
    X_train, X_test = mode_imputation(X_train, X_test)

    # OR
    
    # 2. Missing Category Imputation
    # X_train, X_test = missing_category_imputation(X_train, X_test)

    print("Categorical Imputation Completed!")



# RUN

if __name__ == "__main__":
    main()