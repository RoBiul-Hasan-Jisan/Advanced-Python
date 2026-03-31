
"""
Techniques Implemented:

1. Random Sample Imputation
   - Replaces missing values using random samples from observed values.
   - Preserves distribution and variance.
   - Must use training data only to avoid leakage.

2. Missing Indicator
   - Adds binary columns indicating missingness.
   - Helps model capture patterns in missing data.

3. SimpleImputer (Sklearn)
   - Automated imputation (mean, median, most_frequent, constant).
   - Supports add_indicator=True for missing flags.

4. Full ML Pipeline
   - ColumnTransformer for feature-specific preprocessing
   - Scaling + Encoding
   - Logistic Regression model
   - Hyperparameter tuning using GridSearchCV

Best Practices:
- Always split data before imputation
- Fit imputers on training data only
- Use pipelines for reproducibility
- Validate with cross-validation
"""


import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# Load data
df = pd.read_csv('train.csv')
df.drop(columns=['PassengerId', 'Name', 'Ticket', 'Cabin'], inplace=True)

X = df.drop(columns=['Survived'])
y = df['Survived']

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Numerical pipeline
num_pipe = Pipeline([
    ('imputer', SimpleImputer()),
    ('scaler', StandardScaler())
])

# Categorical pipeline
cat_pipe = Pipeline([
    ('imputer', SimpleImputer()),
    ('encoder', OneHotEncoder(handle_unknown='ignore'))
])

# ColumnTransformer
preprocessor = ColumnTransformer([
    ('num', num_pipe, ['Age', 'Fare']),
    ('cat', cat_pipe, ['Embarked', 'Sex'])
])

# Full pipeline
pipe = Pipeline([
    ('preprocessor', preprocessor),
    ('model', LogisticRegression(max_iter=1000))
])

# GridSearch
param_grid = {
    'preprocessor__num__imputer__strategy': ['mean', 'median'],
    'preprocessor__cat__imputer__strategy': ['most_frequent', 'constant'],
    'model__C': [0.1, 1, 10]
}

grid = GridSearchCV(pipe, param_grid, cv=5, n_jobs=-1)
grid.fit(X_train, y_train)

# Results
print("Best Params:", grid.best_params_)
print("CV Score:", grid.best_score_)

y_pred = grid.predict(X_test)
print("Test Accuracy:", accuracy_score(y_test, y_pred))