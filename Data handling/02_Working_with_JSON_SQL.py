# ============================================================
# What is SQL?
# ============================================================

# SQL = Structured Query Language
# Used to store, manage, and query data in databases
# Examples: MySQL, PostgreSQL, SQLite


# ============================================================
# What is JSON?
# ============================================================

# JSON = JavaScript Object Notation
# Used for storing and exchanging data
# Example:
# {"name": "Alice", "age": 25}


# ============================================================
# Why JSON is important (ML / Data Science)
# ============================================================

# - APIs return data in JSON
# - Many datasets are JSON
# - Easy to read + lightweight
# - Works well with Python


# ============================================================
# Load JSON using Pandas
# ============================================================

import pandas as pd

df = pd.read_json("train.json")   # read JSON file
print(df.head())


# ============================================================
# Connect to MySQL Database
# ============================================================

# Install once:
# pip install mysql-connector-python

import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="world"
)

print("Connected to MySQL")


# ============================================================
# Run SQL Queries with Pandas
# ============================================================

# 1. Cities in India
df_city = pd.read_sql_query(
    "SELECT * FROM city WHERE CountryCode='IND'", conn
)
print(df_city.head())

# 2. Countries with Life Expectancy > 60
df_country = pd.read_sql_query(
    "SELECT * FROM Country WHERE LifeExpectancy > 60", conn
)
print(df_country.head())

# 3. All languages
df_lang = pd.read_sql_query(
    "SELECT * FROM CountryLanguage", conn
)
print(df_lang.head())


# ============================================================
# Close Connection
# ============================================================

conn.close()
print("Connection closed")