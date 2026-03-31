

"""
MICE (Iterative Imputer) - Advanced Missing Data Handling

--------------------------------------------------
What is MICE?
--------------------------------------------------
MICE is a multivariate imputation technique that fills missing
values by modeling each feature with missing data as a function
of other features.

The process is iterative:
1. Initialize missing values (e.g., mean)
2. For each feature:
   - Treat it as target
   - Use other features to predict missing values
3. Repeat multiple times until convergence

--------------------------------------------------
Key Idea
--------------------------------------------------
Each variable is imputed using a regression model built
from other variables.

--------------------------------------------------
Advantages
--------------------------------------------------
- Preserves relationships between variables
- Produces realistic imputations
- Works well with correlated features

--------------------------------------------------
Disadvantages
--------------------------------------------------
- Computationally expensive
- Sensitive to model choice
- Requires careful tuning

--------------------------------------------------
Best Practice
--------------------------------------------------
- Use sklearn IterativeImputer (production)
- Scale features before applying
- Combine with pipelines
"""
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.experimental import enable_iterative_imputer  # required
from sklearn.impute import IterativeImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import BayesianRidge, LogisticRegression
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv('train.csv')[['Age', 'Fare', 'Pclass', 'Survived']]

X = df.drop(columns=['Survived'])
y = df['Survived']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# MICE pipeline
mice_pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('imputer', IterativeImputer(
        estimator=BayesianRidge(),
        max_iter=10,
        random_state=42
    )),
    ('model', LogisticRegression(max_iter=1000))
])

# Train
mice_pipe.fit(X_train, y_train)

# Evaluate
y_pred = mice_pipe.predict(X_test)
print("MICE Accuracy:", accuracy_score(y_test, y_pred))