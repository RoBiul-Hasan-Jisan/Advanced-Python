
# What is API?


# API = Application Programming Interface
# Used to send/receive data (mostly JSON)



# Required Libraries


import requests
import pandas as pd



# 1. Single API Request


url = "API_URL_HERE"

res = requests.get(url)

if res.status_code == 200:
    data = res.json()

    df = pd.DataFrame(data.get("results", []))[
        ['id', 'title', 'overview', 'release_date']
    ]

    print(df.head(2))
else:
    print("Error:", res.status_code)



# 2. Pagination (Multiple Pages)


all_data = []

for page in range(1, 430):   # total pages
    res = requests.get(f"{url}?page={page}")

    if res.status_code != 200:
        print("Error on page", page)
        continue

    results = res.json().get("results", [])

    if results:
        df_temp = pd.DataFrame(results)[
            ['id', 'title', 'overview', 'release_date']
        ]
        all_data.append(df_temp)



# 3. Combine Data


df = pd.concat(all_data, ignore_index=True)

print("Final shape:", df.shape)



# 4. Save Data


df.to_csv("test_data.csv", index=False)
print("Saved successfully")