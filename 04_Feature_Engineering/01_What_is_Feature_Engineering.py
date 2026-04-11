
"""

Feature Engineering is the process of transforming raw data
into meaningful and informative features that enhance the 
performance of Machine Learning models.

It combines domain knowledge, data analysis, and creativity
to make data more suitable for modeling.
"""

# ------------------------------------------------------------
#  Why is Feature Engineering Important?
# ------------------------------------------------------------
#  Improves model accuracy and generalization
#  Helps models learn patterns more effectively
#  Reduces overfitting by removing noise
#  Enhances training speed and efficiency

# ------------------------------------------------------------
#  Where is it Used?
# ------------------------------------------------------------
#  Structured Data     → (Tabular: CSV, databases)
#  Unstructured Data   → (Text, Images, Audio, Video)
#  Time Series Data    → (Stock prices, sensor data)
#  Big Data Systems    → (Real-world large-scale ML pipelines)

# ------------------------------------------------------------
#  When is Feature Engineering Done?
# ------------------------------------------------------------
#  During Data Preprocessing Stage
#  After Data Cleaning
#  Before Model Training
#  Iteratively during model improvement

# ------------------------------------------------------------
#  How is Feature Engineering Performed?
# -----------------------------------------------------------

# 1. Feature Transformation
# -------------------------
# - Scaling (Normalization, Standardization)
# - Encoding (Label Encoding, One-Hot Encoding)
# - Log / Power Transformations

# 2. Feature Construction
# ------------------------
# - Creating new features from existing ones
#   Example: BMI = weight / height²
#   Example: Age from Date of Birth

# 3. Feature Selection
# ---------------------
# - Removing irrelevant or redundant features
# - Methods:
#   • Filter Methods (Correlation, Chi-Square)
#   • Wrapper Methods (RFE)
#   • Embedded Methods (Lasso, Tree-based)

# 4. Feature Extraction
# ----------------------
# - Extracting useful information from raw data
#   • Text → TF-IDF, Word Embeddings
#   • Images → CNN features
#   • Audio → MFCC features

# ------------------------------------------------------------
#  Key Insight
# ------------------------------------------------------------
# "Better features > Better model"
# Even simple algorithms perform well with strong features,
# while complex models fail with poor features.

# --------------------------------------------------
# 1. FEATURE TRANSFORMATION 
# --------------------------------------------------
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# -----------------------------
# Create DataFrame
# -----------------------------
data = {
    "Name": ["Ali", "Sara", "John", "Mary", "Tom"],
    "Age": [25, np.nan, 30, 22, np.nan],
    "Gender": ["Male", "Female", "Male", "Female", "Male"],
    "Salary": [30000, 35000, 40000, 1000000, 45000],
    "Height_cm": [160, 170, 180, 175, 165],
    "Weight_kg": [50, 80, 100, 70, 60],
    "Date_of_Birth": pd.to_datetime(
        ["2000-01-01", "1998-05-15", "1995-07-23", "2002-09-10", "1999-12-30"]
    )
}

df = pd.DataFrame(data)


# 1. FEATURE TRANSFORMATION


# Missing Values Handling
df["Age"] = df["Age"].fillna(df["Age"].mean())

# One-Hot Encoding (better than Label Encoding for ML models)
df = pd.get_dummies(df, columns=["Gender"], drop_first=True)

# Outlier Handling (IQR Method - dynamic)
Q1 = df["Salary"].quantile(0.25)
Q3 = df["Salary"].quantile(0.75)
IQR = Q3 - Q1

upper_bound = Q3 + 1.5 * IQR
df["Salary_Capped"] = np.where(df["Salary"] > upper_bound, upper_bound, df["Salary"])

# Feature Scaling
minmax_scaler = MinMaxScaler()
df["Height_Scaled"] = minmax_scaler.fit_transform(df[["Height_cm"]])

standard_scaler = StandardScaler()
df["Weight_Standardized"] = standard_scaler.fit_transform(df[["Weight_kg"]])


# 2. FEATURE CONSTRUCTION


current_year = pd.Timestamp.now().year
df["Age_from_DOB"] = current_year - df["Date_of_Birth"].dt.year

# BMI Feature (Very strong real-world feature)
df["BMI"] = df["Weight_kg"] / ((df["Height_cm"] / 100) ** 2)


# 3. FEATURE SELECTION


# Drop less useful or redundant columns
df = df.drop(columns=["Name", "Date_of_Birth"])


# 4. FEATURE EXTRACTION


# Extracting information from text
df["Name_Length"] = data["Name"]
df["Name_Length"] = df["Name_Length"].apply(len)


# FINAL OUTPUT


print(df.head())