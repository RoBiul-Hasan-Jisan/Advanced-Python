



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

# Display settings
pd.set_option('display.max_columns', None)


# 1. LOAD DATA

file_path = "test.csv"   # change if needed
df = pd.read_csv(file_path)


print(" DATA LOADED SUCCESSFULLY")



# 2. BASIC OVERVIEW

print("\n Shape of Dataset:")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

print("\n Column Names:")
print(df.columns.tolist())

print("\n First 10 Rows:")
print(df.head(10))

print("\n Random Sample Rows:")
print(df.sample(5))


# 3. DATA INFORMATION

print("\n Dataset Info:")
df.info()

print("\n Data Types:")
print(df.dtypes)


# 4. MISSING VALUES ANALYSIS

print("\n Missing Values Count:")
missing_count = df.isnull().sum()
print(missing_count)

print("\n Missing Values Percentage:")
missing_percent = (missing_count / len(df)) * 100
print(missing_percent.sort_values(ascending=False))

# Visualization
plt.figure(figsize=(10,5))
missing_percent.sort_values(ascending=False).plot(kind='bar')
plt.title("Missing Values Percentage")
plt.ylabel("% Missing")
plt.xticks(rotation=45)
plt.show()


# 5. DUPLICATE VALUES

duplicates = df.duplicated().sum()
print("\n Duplicate Rows:", duplicates)


# 6. STATISTICAL SUMMARY

print("\n Numerical Features Summary:")
print(df.describe())

print("\n Categorical Features Summary:")
print(df.describe(include='object'))


# 7. UNIQUE VALUES ANALYSIS

print("\n Unique Values in Each Column:")
for col in df.columns:
    print(f"{col}: {df[col].nunique()} unique values")


# 8. CORRELATION ANALYSIS

corr_matrix = df.corr(numeric_only=True)

print("\n Correlation Matrix:")
print(corr_matrix)

# Heatmap
plt.figure(figsize=(12,8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()


# 10. NUMERICAL FEATURE DISTRIBUTION

num_cols = df.select_dtypes(include=np.number).columns

for col in num_cols:
    plt.figure(figsize=(6,4))
    sns.histplot(df[col], kde=True)
    plt.title(f"Distribution of {col}")
    plt.show()


# 11. CATEGORICAL FEATURE DISTRIBUTION

cat_cols = df.select_dtypes(include='object').columns

for col in cat_cols:
    plt.figure(figsize=(6,4))
    sns.countplot(x=df[col])
    plt.title(f"Count Plot of {col}")
    plt.xticks(rotation=45)
    plt.show()


