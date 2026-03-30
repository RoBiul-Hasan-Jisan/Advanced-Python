



"""
Bivariate Analysis:
- Relationship between TWO variables

Multivariate Analysis:
- Relationship between THREE or MORE variables

Goal:
- Find patterns, relationships, and insights
"""




import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

sns.set(style="whitegrid")


# 1. LOAD DATASETS

tips = sns.load_dataset('tips')
titanic = pd.read_csv('titanic.csv')   
flights = sns.load_dataset('flights')
iris = sns.load_dataset('iris')

print(" Data Loaded Successfully\n")


# 2. QUICK PREVIEW

print(" Titanic Data:")
print(titanic.head())


# 3. BIVARIATE ANALYSIS


print(" BIVARIATE ANALYSIS")



# 3.1 Numerical vs Numerical (Scatter Plot)

plt.figure(figsize=(6,4))
sns.scatterplot(
    x='total_bill', 
    y='tip', 
    data=tips, 
    hue='sex', 
    style='smoker',
    size='size'
)
plt.title("Total Bill vs Tip")
plt.show()


# 3.2 Categorical vs Numerical (Bar Plot)

plt.figure(figsize=(6,4))
sns.barplot(x='Pclass', y='Age', data=titanic, hue='Sex')
plt.title("Average Age by Class & Gender")
plt.show()


# 3.3 Categorical vs Numerical (Box Plot)

plt.figure(figsize=(6,4))
sns.boxplot(x='Sex', y='Age', hue='Survived', data=titanic)
plt.title("Age Distribution by Gender & Survival")
plt.show()


# 3.4 Distribution Comparison (KDE)

plt.figure(figsize=(6,4))
sns.kdeplot(
    data=titanic, 
    x='Age', 
    hue='Survived', 
    fill=True
)
plt.title("Age Distribution by Survival")
plt.show()


# 3.5 Categorical vs Categorical (Heatmap)

plt.figure(figsize=(6,4))
cross_tab = pd.crosstab(titanic['Pclass'], titanic['Survived'])
sns.heatmap(cross_tab, annot=True, cmap="YlGnBu", fmt='d')
plt.title("Pclass vs Survival")
plt.show()


# 4. MULTIVARIATE ANALYSIS


print(" MULTIVARIATE ANALYSIS")



# 4.1 Clustermap (Pattern Detection)

sns.clustermap(
    pd.crosstab(titanic['SibSp'], titanic['Survived']),
    cmap="coolwarm",
    annot=True
)
plt.title("SibSp vs Survival Clustermap")
plt.show()


# 4.2 Pair Plot (All Numerical Relationships)

sns.pairplot(iris, hue='species')
plt.show()


# 4.3 Line Plot (Time Series)

yearly = flights.groupby('year')['passengers'].sum().reset_index()

plt.figure(figsize=(8,4))
sns.lineplot(x='year', y='passengers', data=yearly, marker='o')
plt.title("Yearly Passenger Growth")
plt.show()


# 4.4 Heatmap (Time vs Category)

pivot = flights.pivot_table(
    values='passengers',
    index='month',
    columns='year'
)

plt.figure(figsize=(10,6))
sns.heatmap(pivot, cmap="YlOrBr")
plt.title("Passengers (Month vs Year)")
plt.show()


# 4.5 Clustermap 

sns.clustermap(pivot, cmap="coolwarm")
plt.title("Clustered Passenger Trends")
plt.show()


#  CORRELATION HEATMAP

print("\n Correlation Analysis")

plt.figure(figsize=(10,6))
sns.heatmap(
    titanic.corr(numeric_only=True),
    annot=True,
    cmap='coolwarm',
    fmt=".2f"
)
plt.title("Correlation Matrix (Titanic)")
plt.show()


