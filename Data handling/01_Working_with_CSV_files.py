# ============================================================
# Opening a CSV file (Local)
# ============================================================

import pandas as pd

df = pd.read_csv("testdataset.csv")   # Read local CSV
print(df.head())


# ============================================================
# Opening a CSV file from URL (Direct - Best)
# ============================================================

url = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
df = pd.read_csv(url)
print(df.head())


# ============================================================
# Opening a CSV using requests (Advanced)
# ============================================================

import requests
from io import StringIO

headers = {"User-Agent": "Mozilla/5.0"}
req = requests.get(url, headers=headers)

data = StringIO(req.text)
df = pd.read_csv(data)
print(df.head())


# ============================================================
# TSV (Tab Separated Values)
# ============================================================

pd.read_csv(
    "movie_titles_metadata.tsv",
    sep="\t",
    names=['sno', 'name', 'release_year', 'rating', 'votes', 'genres']
)


# ============================================================
# Important Parameters in pd.read_csv()
# ============================================================

# 1. index_col → set column as index
pd.read_csv("testdataset.csv", index_col="enrollee_id")

# 2. header → row number as column names
pd.read_csv("testdataset.csv", header=1)

# 3. usecols → select columns
pd.read_csv("testdataset.csv", usecols=['enrollee_id', 'gender'])

# 4. (Modern) get single column
df = pd.read_csv("testdataset.csv")
df['gender']

# 5. skiprows → skip rows
pd.read_csv("testdataset.csv", skiprows=10)

# 6. nrows → limit rows
pd.read_csv("testdataset.csv", nrows=100)

# 7. encoding → fix text issues
pd.read_csv("testdataset.csv", encoding="utf-8")

# 8. on_bad_lines → skip broken rows
pd.read_csv("testdataset.csv", on_bad_lines="skip")

# 9. dtype → set data types
pd.read_csv("testdataset.csv", dtype={"gender": "category"})

# 10. parse_dates → convert to datetime
pd.read_csv("date_data.csv", parse_dates=["joining_date"])

# 11. converters → transform while loading
pd.read_csv("testdataset.csv",
            converters={"gender": lambda x: str(x).upper()})

# 12. na_values → custom missing values
pd.read_csv("testdataset.csv", na_values=["NA", "missing"])

# 13. chunksize → handle large files
for chunk in pd.read_csv("testdataset.csv", chunksize=500):
    print("Chunk size:", chunk.shape)


# ============================================================
# SUMMARY
# ============================================================

# CSV  → comma separated
# TSV  → tab separated (\t)
# read_csv() → main function for loading data

# Most useful params:
# usecols, dtype, parse_dates, na_values, chunksize