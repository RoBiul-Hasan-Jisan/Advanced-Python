# Advanced Python

A personal, topic-by-topic collection of Python scripts — starting from core language
fundamentals and moving through data handling, exploratory data analysis, feature engineering,
and object-oriented programming. Each folder is a self-contained mini-module: every script is
heavily commented and meant to be read top-to-bottom like a lesson, then run to see the output.

##  Structure

```
Advanced-Python/
├── 01_Basic python/                 Core Python fundamentals
│   ├── Algo/                        Search algorithms (BFS, DFS, Greedy Best-First Search)
│   ├── Dictionaries/                Dictionary exercises & patterns
│   ├── Function/                    Functions, closures, decorators, *args/**kwargs, functools
│   ├── LIST/                        List exercises & patterns
│   ├── Pattern/                     Pattern-printing exercises
│   ├── String/                      String exercises & patterns
│   └── TUPLE/                       Tuple exercises & patterns
│
├── 02_Data handling/                Reading & fetching data
│   ├── 01_Working_with_CSV_files.py
│   ├── 02_Working_with_JSON_SQL.py
│   ├── 03_Web_Scraping_for_Data.py
│   └── 04_Fetching_Data_from_API.py
│
├── 03_Exploratory_Data_Analysis/    EDA with pandas
│   ├── 01_Explore data.py
│   ├── 02_EDA_Univariate_Insights.py
│   ├── 03_Feature_Relationship_Analysis.py
│   └── 04Universal_EDA_Template.py
│
├── 04_Feature_Engineering/          Scaling, encoding, transforms, pipelines
│   ├── 01_What_is_Feature_Engineering.py
│   ├── 02_Feature_Scaling_Standardization.py
│   ├── 03_Feature_Scaling_Normalization.py
│   ├── 04_Encoding_Categorical_Data_(Ordinal_Label_Encoding).py
│   ├── 05_One_Hot_Encoding.py
│   ├── 06_Column_Transformer_in_Sklearn.py
│   ├── 07_Machine_Learning_Pipelines.py
│   ├── 08_Function_Transformer_(Log, Reciprocal, Square Root).py
│   ├── 09_Power_Transformer_(Box-Cox, Yeo-Johnson).py
│   ├── 10_Binning_and_Binarization.py
│   ├── 11_Handling_Mixed_Variables.py
│   ├── 12_Handling_Date_And_Time_Variables.py
│   └── 13_Feature_Construction_Feature_Splitting.py
│
├── 05_Handling_Missing_Data/        Imputation strategies
│   ├── 01_Comprehensive_Case_Review.py
│   ├── 02_Numerical_Imputation.py
│   ├── 03_Categorical_Imputation.py
│   ├── 04_Missing_Indicator_Imputation.py
│   ├── 05_KNN_Imputation.py
│   └── 06_MICE_Imputation.py
│
├── 06_Outliers/                     Outlier detection & treatment
│   ├── 01_What_Are_Outliers.py
│   ├── 02_Z-Score_Method.py
│   ├── 03_IQR_Method.py
│   └── 04_Percentile_Method_(Winsorization).py
│
├── 07_Dimensionality Reduction/     PCA
│   ├── 01_Curse_of_Dimensionality.py
│   ├── 02_PCA_Part_1_(Geometric Intuition).py
│   ├── 03_PCA_Part 2_(Maths & Solution).py
│   └── 04_PCA_Part_3_(Code Example & Visualization).py
│
└── 08_Object-Oriented Programming/  Classes, inheritance, dunder methods, properties
    ├── 01_classes_and_instances.py/
    │   └── 1. Classes_and_Instances.py
    ├── 02_Class Variables/
    │   ├── 01_Class Variables.py
    │   └── 02_Class Variables-2.py
    ├── 03_Class Method and Static Method/
    │   └── 01_Class Method and Static Method.py
    ├── 04_Inheritance - Creating Subclasses/
    │   └── 01_Inheritance.py
    ├── 05_Special (Magic or Dunder) Methods/
    │   └── 01_Special_Dunder_Methods.py
    └── 06_Property Decorators - Getters, Setters and Deleters/
        └── 01_Property_Decorators.py
```

##  Topic notes

### 01 · Basic Python
Warm-up exercises and drills covering lists, tuples, dictionaries, strings, functions
(including closures, decorators, `*args`/`**kwargs`, `map`/`filter`/`reduce`, generators), simple
pattern printing, and a few classic graph-search algorithms (BFS, DFS, Greedy BFS).

### 02 · Data Handling
Getting data into Python from different sources: CSV/TSV files, JSON and SQL, scraping a web
page, and calling a REST API.

### 03 · Exploratory Data Analysis (EDA)
Using pandas to profile a dataset — shape, dtypes, missing values, univariate summaries, and
relationships between features — finishing with a reusable, general-purpose EDA template.

### 04 · Feature Engineering
The largest module: scaling (standardization/normalization), categorical encoding (ordinal,
label, one-hot), `ColumnTransformer` and `Pipeline` in scikit-learn, function/power transforms
(log, reciprocal, square root, Box-Cox, Yeo-Johnson), binning/binarization, mixed-variable
handling, date/time features, and feature construction/splitting.

### 05 · Handling Missing Data
Complete Case Analysis, numerical and categorical imputation, missing-indicator imputation,
KNN imputation, and MICE (Multiple Imputation by Chained Equations).

### 06 · Outliers
What outliers are and why they matter, plus three detection/treatment methods: Z-score, IQR
(Interquartile Range), and percentile-based Winsorization.

### 07 · Dimensionality Reduction
The curse of dimensionality, then PCA (Principal Component Analysis) in three parts — geometric
intuition, the underlying math, and a worked code example with visualization.

### 08 · Object-Oriented Programming
A from-scratch OOP course built around one running example (an `Employee` class), in order:

1. **Classes and Instances** — what a class/instance is, `__init__`, instance attributes.
2. **Class Variables** — variables shared across all instances, and how instance vs. class
   access differs.
3. **Class Methods and Static Methods** — `@classmethod` (incl. alternative constructors) and
   `@staticmethod`.
4. **Inheritance — Creating Subclasses** — subclassing, `super()`, method overriding,
   `isinstance()` vs `issubclass()`.
5. **Special (Magic/Dunder) Methods** — `__repr__`, `__str__`, `__add__`, `__len__`, and how
   Python's data model works.
6. **Property Decorators** — turning methods into attribute-like properties with
   `@property`, `@x.setter`, and `@x.deleter`.

Each script builds directly on the previous one, so they're best read in numeric order.

##  Running the scripts

Everything here uses the standard library plus a few common data-science packages. From the
repo root:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn requests beautifulsoup4
python "01_Basic python/Function/Decorators.py"
python "08_Object-Oriented Programming/06_Property Decorators - Getters, Setters and Deleters/01_Property_Decorators.py"
```

Most scripts in `02` through `07` are written as walkthroughs against sample/placeholder data —
open the file and check the top of the script for any dataset it expects, or swap in your own
CSV where indicated.

