
"""
Missing Data Handling: Complete Case Analysis (CCA)

--------------------------------------------------
What is Complete Case Analysis?
--------------------------------------------------
Complete Case Analysis (CCA), also known as list-wise deletion,
is a technique where we remove all rows (observations) that contain
missing values in any feature.

Only rows with complete data across all selected variables are retained
for further analysis or modeling.

--------------------------------------------------
Key Assumption
--------------------------------------------------
CCA assumes that data is MCAR (Missing Completely At Random),
meaning the probability of missingness is independent of both
observed and unobserved data.

--------------------------------------------------
Advantages
--------------------------------------------------
1. Simple and easy to implement (no imputation required).
2. Keeps data integrity intact when MCAR holds true.
3. Does not introduce artificial values into the dataset.

--------------------------------------------------
Disadvantages
--------------------------------------------------
1. Can lead to significant data loss if missing values are high.
2. May introduce bias if data is not MCAR.
3. Not suitable for small datasets.
4. Models trained using CCA may fail in production if missing
   values appear again.

--------------------------------------------------
When to Use CCA?
--------------------------------------------------
- When missing data is less than 5%.
- When data is likely MCAR.
- When dataset size is sufficiently large.

--------------------------------------------------
Best Practice
--------------------------------------------------
Always compare feature distributions before and after applying CCA
to ensure that important patterns are not lost.
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



# 1. LOAD DATA

def load_data(path):
    df = pd.read_csv(path)
    print("Data Loaded Successfully!")
    print("Shape:", df.shape)
    return df



# 2. MISSING VALUE ANALYSIS

def missing_analysis(df):
    print("\n--- Missing Value Percentage ---")
    missing = df.isnull().mean() * 100
    print(missing[missing > 0].sort_values(ascending=False))



# 3. SELECT COLUMNS (<5% missing)

def select_columns(df, threshold=0.05):
    cols = [col for col in df.columns if df[col].isnull().mean() < threshold]
    print("\nSelected Columns:", cols)
    return cols



# 4. APPLY CCA

def apply_cca(df, cols):
    new_df = df[cols].dropna().reset_index(drop=True)
    print("\nOriginal Shape:", df.shape)
    print("After CCA Shape:", new_df.shape)

    retained_fraction = len(new_df) / len(df)
    print("Retained Data Fraction:", retained_fraction)

    return new_df



# 5. FIX DATA TYPES (IMPORTANT STEP)

def fix_experience(df):
    if 'experience' in df.columns:
        df['experience'] = df['experience'].replace({
            '>20': 21,
            '<1': 0
        })
        df['experience'] = pd.to_numeric(df['experience'], errors='coerce')
    return df



# 6. COMPARE NUMERICAL DISTRIBUTIONS

def compare_distribution(df, new_df, col):
    fig, ax = plt.subplots()

    df[col].hist(bins=50, density=True, alpha=0.5, label='Original', ax=ax)
    new_df[col].hist(bins=50, density=True, alpha=0.5, label='CCA', ax=ax)

    plt.legend()
    plt.title(f"{col} Distribution")
    plt.show()



# 7. COMPARE CATEGORICAL DISTRIBUTIONS

def compare_categorical(df, new_df, col):
    temp = pd.concat([
        df[col].value_counts(normalize=True),
        new_df[col].value_counts(normalize=True)
    ], axis=1)

    temp.columns = ['Original', 'CCA']
    print(f"\n--- {col} Distribution ---")
    print(temp)



# 8. MAIN FUNCTION

def main():
    # Load dataset
    df = load_data('data_science_job.csv')

    # Analyze missing values
    missing_analysis(df)

    # Select columns
    cols = select_columns(df)

    # Fix data types
    df = fix_experience(df)

    # Apply CCA
    new_df = apply_cca(df, cols)

    # Compare numerical features
    numerical_cols = ['training_hours', 'city_development_index', 'experience']
    for col in numerical_cols:
        if col in df.columns:
            compare_distribution(df, new_df, col)

    # Compare categorical features
    categorical_cols = ['enrolled_university', 'education_level']
    for col in categorical_cols:
        if col in df.columns:
            compare_categorical(df, new_df, col)



# 9. RUN SCRIPT

if __name__ == "__main__":
    main()