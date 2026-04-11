

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

pd.set_option('display.max_columns', None)
sns.set(style="whitegrid")


# 1. LOAD DATA

file_path = "titanic.csv"   
df = pd.read_csv(file_path)


print(" DATA LOADED")



# 2. BASIC OVERVIEW

print("\n Shape:", df.shape)

print("\n Columns:")
print(df.columns.tolist())

print("\n First rows:")
print(df.head())

print("\n Random sample:")
print(df.sample(5))


# 3. DATA INFO

print("\n Info:")
df.info()

print("\n Data Types:")
print(df.dtypes)


# 4. MISSING VALUES

print("\n Missing Values:")
missing = df.isnull().sum()
missing_percent = (missing / len(df)) * 100

missing_df = pd.DataFrame({
    'Missing_Count': missing,
    'Missing_%': missing_percent
}).sort_values(by='Missing_%', ascending=False)

print(missing_df)

# Plot missing values
plt.figure(figsize=(10,5))
missing_percent[missing_percent > 0].sort_values().plot(kind='barh')
plt.title("Missing Values %")
plt.show()


# 5. DUPLICATES

duplicates = df.duplicated().sum()
print("\n Duplicate Rows:", duplicates)


# 6. COLUMN TYPES

num_cols = df.select_dtypes(include=np.number).columns.tolist()
cat_cols = df.select_dtypes(include='object').columns.tolist()

print("\n Numerical Columns:", num_cols)
print("\n Categorical Columns:", cat_cols)


# 7. STATISTICAL SUMMARY

print("\n Numerical Summary:")
print(df.describe())

print("\n Categorical Summary:")
print(df.describe(include='object'))


# 8. UNIVARIATE ANALYSIS

print(" UNIVARIATE ANALYSIS")


# Numerical
for col in num_cols:
    plt.figure(figsize=(6,4))
    sns.histplot(df[col].dropna(), kde=True)
    plt.title(f"{col} Distribution")
    plt.show()

    plt.figure(figsize=(6,4))
    sns.boxplot(x=df[col])
    plt.title(f"{col} Boxplot")
    plt.show()

# Categorical
for col in cat_cols:
    plt.figure(figsize=(6,4))
    sns.countplot(x=col, data=df)
    plt.title(f"{col} Countplot")
    plt.xticks(rotation=45)
    plt.show()


# 9. BIVARIATE ANALYSIS


print(" BIVARIATE ANALYSIS")


# Correlation heatmap
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

# Scatter plots (numerical vs numerical)
for i in range(len(num_cols)):
    for j in range(i+1, len(num_cols)):
        plt.figure(figsize=(5,4))
        sns.scatterplot(x=df[num_cols[i]], y=df[num_cols[j]])
        plt.title(f"{num_cols[i]} vs {num_cols[j]}")
        plt.show()


# 10. MULTIVARIATE ANALYSIS


print(" MULTIVARIATE ANALYSIS")


# Pairplot (if dataset not too big)
if len(df) < 1000:
    sns.pairplot(df, hue=cat_cols[0] if len(cat_cols)>0 else None)
    plt.show()


# 11. OUTLIER DETECTION

print("\n OUTLIER DETECTION")

for col in num_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    outliers = df[(df[col] < lower) | (df[col] > upper)]

    print(f"{col}: {len(outliers)} outliers")


# 12. UNIQUE VALUES

print("\n Unique Values:")

for col in df.columns:
    print(f"{col}: {df[col].nunique()} unique values")

