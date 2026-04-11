



"""
Univariate Analysis:
- Analyze ONE variable at a time
- Understand distribution, spread, and patterns

Types:
1. Numerical → Histogram, KDE, Boxplot
2. Categorical → Countplot, Barplot, Pie chart
"""



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

pd.set_option('display.max_columns', None)


# 1. LOAD DATA

df = pd.read_csv('titanic.csv')


print(" DATA LOADED")


print("\n First 5 rows:")
print(df.head())


# 2. SEPARATE COLUMN TYPES

num_cols = df.select_dtypes(include=np.number).columns.tolist()
cat_cols = df.select_dtypes(include='object').columns.tolist()

print("\n Numerical Columns:", num_cols)
print("\n Categorical Columns:", cat_cols)


# 3. CATEGORICAL DATA ANALYSIS

print(" CATEGORICAL FEATURES ANALYSIS")


for col in cat_cols + ['Survived'] if 'Survived' in df.columns else cat_cols:

    print(f"\n Column: {col}")
    print(df[col].value_counts())

    plt.figure(figsize=(6,4))
    sns.countplot(x=col, data=df)
    plt.title(f"Count Plot of {col}")
    plt.xticks(rotation=45)
    plt.show()

    # Pie chart (only if unique values small)
    if df[col].nunique() <= 6:
        df[col].value_counts().plot(
            kind='pie',
            autopct='%.1f%%',
            figsize=(5,5),
            title=f"{col} Distribution"
        )
        plt.ylabel("")
        plt.show()


# 4. NUMERICAL DATA ANALYSIS


print(" NUMERICAL FEATURES ANALYSIS")


for col in num_cols:

    print(f"\n Column: {col}")

    # Drop missing values for plotting
    data = df[col].dropna()

    # Basic stats
    print("Mean:", data.mean())
    print("Median:", data.median())
    print("Min:", data.min())
    print("Max:", data.max())
    print("Std Dev:", data.std())

    
    # Histogram + KDE
    
    plt.figure(figsize=(6,4))
    sns.histplot(data, kde=True, bins=30)
    plt.title(f"Distribution of {col}")
    plt.show()

    
    # Boxplot (Outlier Detection)
    
    plt.figure(figsize=(6,4))
    sns.boxplot(x=data)
    plt.title(f"Boxplot of {col}")
    plt.show()


# 5. SPECIAL ANALYSIS (AGE EXAMPLE)

if 'Age' in df.columns:

    print("\n Detailed Age Analysis")

    age = df['Age'].dropna()

    print("Min Age:", age.min())
    print("Max Age:", age.max())
    print("Median Age:", age.median())
    print("Q1:", age.quantile(0.25))
    print("Q3:", age.quantile(0.75))

    IQR = age.quantile(0.75) - age.quantile(0.25)
    print("IQR:", IQR)


# 6. SUMMARY TABLE

print("\n Summary of Numerical Features:")
summary = df.describe().T
summary['IQR'] = summary['75%'] - summary['25%']
print(summary)


