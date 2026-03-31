
"""
Imputation Techniques Compared:

1. KNN Imputer (Multivariate Imputation)
   - Uses k-nearest neighbors to fill missing values.
   - Considers relationships between features.
   - Produces realistic values.

   Pros:
   - Preserves feature relationships
   - Often improves model performance

   Cons:
   - Computationally expensive
   - Sensitive to feature scaling
   - Affected by noise

2. Simple Imputer (Mean Strategy)
   - Replaces missing values with column mean.
   - Treats each feature independently.

   Pros:
   - Fast and simple
   - Works well for baseline models

   Cons:
   - Ignores feature relationships
   - Reduces variance
   - Can hurt model performance

Best Practice:
- Always scale features before KNN Imputer
- Use pipelines to avoid leakage
- Compare multiple imputation strategies
"""



import pandas as pd

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.impute import KNNImputer, SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# Load data
df = pd.read_csv('train.csv')[['Age', 'Pclass', 'Fare', 'Survived']]

X = df.drop(columns=['Survived'])
y = df['Survived']

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# KNN Pipeline

knn_pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('imputer', KNNImputer(n_neighbors=3)),
    ('model', LogisticRegression(max_iter=1000))
])

knn_pipe.fit(X_train, y_train)
knn_score = knn_pipe.score(X_test, y_test)

print("KNN Pipeline Accuracy:", knn_score)


# Simple Imputer Pipeline

simple_pipe = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler()),
    ('model', LogisticRegression(max_iter=1000))
])

simple_pipe.fit(X_train, y_train)
simple_score = simple_pipe.score(X_test, y_test)

print("Simple Imputer Accuracy:", simple_score)


# Cross-validation (better evaluation)

knn_cv = cross_val_score(knn_pipe, X, y, cv=5).mean()
simple_cv = cross_val_score(simple_pipe, X, y, cv=5).mean()

print("KNN CV Score:", knn_cv)
print("Simple CV Score:", simple_cv)