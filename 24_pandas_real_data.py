import pandas as pd
from pathlib import Path

# ---------------------------------------------------------
# 1. Load the dataset
# ---------------------------------------------------------

FILE_NAME = Path("titanic.csv")
OUTPUT_FILE = Path("titanic_cleaned.csv")

if not FILE_NAME.exists():
    print(f"Error: {FILE_NAME} was not found in the current directory.")
    exit()

df = pd.read_csv(FILE_NAME)

print("Original Dataset")
print("-" * 50)
print(df.head())

print("\nDataset Shape:", df.shape)


# ---------------------------------------------------------
# 2. Display basic information
# ---------------------------------------------------------

print("\nDataset Information")
print("-" * 50)
print(df.info())

print("\nMissing Values")
print("-" * 50)
print(df.isnull().sum())


# ---------------------------------------------------------
# 3. Remove duplicate records
# ---------------------------------------------------------

duplicate_count = df.duplicated().sum()

print("\nDuplicate Rows:", duplicate_count)

if duplicate_count > 0:
    df = df.drop_duplicates()

print("Shape after removing duplicates:", df.shape)


# ---------------------------------------------------------
# 4. Clean column names
# ---------------------------------------------------------

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

print("\nCleaned Column Names:")
print(df.columns.tolist())


# ---------------------------------------------------------
# 5. Handle missing values
# ---------------------------------------------------------

# Age:
# Replace missing age values with the median age.
df["age"] = df["age"].fillna(df["age"].median())

# Embarked:
# Replace missing values with the most common value (mode).
df["embarked"] = df["embarked"].fillna(df["embarked"].mode()[0])

# Fare:
# Replace missing fare values with the median fare.
df["fare"] = df["fare"].fillna(df["fare"].median())

# Cabin:
# Cabin has many missing values, so instead of deleting
# passengers, create a new feature indicating whether
# cabin information is available.
df["has_cabin"] = df["cabin"].notna().astype(int)

# Replace missing cabin values with "Unknown".
df["cabin"] = df["cabin"].fillna("Unknown")


# ---------------------------------------------------------
# 6. Convert data types
# ---------------------------------------------------------

numeric_columns = [
    "passengerid",
    "survived",
    "pclass",
    "age",
    "sibsp",
    "parch",
    "fare"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")


# ---------------------------------------------------------
# 7. Clean text columns
# ---------------------------------------------------------

text_columns = [
    "name",
    "sex",
    "ticket",
    "cabin",
    "embarked"
]

for column in text_columns:
    df[column] = df[column].astype(str).str.strip()


# ---------------------------------------------------------
# 8. Create additional useful features
# ---------------------------------------------------------

# Family size = siblings/spouses + parents/children + passenger
df["family_size"] = df["sibsp"] + df["parch"] + 1

# Whether the passenger was travelling alone
df["is_alone"] = (df["family_size"] == 1).astype(int)

# Extract passenger title from name
df["title"] = df["name"].str.extract(r",\s*([^.]*)\.", expand=False)

# Clean title
df["title"] = df["title"].str.strip()

# Group uncommon titles
common_titles = ["Mr", "Miss", "Mrs", "Master"]

df["title"] = df["title"].apply(
    lambda x: x if x in common_titles else "Other"
)


# ---------------------------------------------------------
# 9. Encode categorical variables
# ---------------------------------------------------------

# Convert Sex to numeric values
df["sex"] = df["sex"].map({
    "male": 0,
    "female": 1
})

# Convert Embarked to dummy/one-hot variables
df = pd.get_dummies(
    df,
    columns=["embarked"],
    prefix="embarked",
    dtype=int
)

# One-hot encode passenger title
df = pd.get_dummies(
    df,
    columns=["title"],
    prefix="title",
    dtype=int
)


# ---------------------------------------------------------
# 10. Remove unnecessary columns
# ---------------------------------------------------------

# Name, Ticket and Cabin are textual identifiers that are
# not directly required for this preprocessing example.

df = df.drop(
    columns=["name", "ticket", "cabin"],
    errors="ignore"
)


# ---------------------------------------------------------
# 11. Check for remaining missing values
# ---------------------------------------------------------

print("\nMissing Values After Cleaning")
print("-" * 50)
print(df.isnull().sum())


# ---------------------------------------------------------
# 12. Save the cleaned dataset
# ---------------------------------------------------------

df.to_csv(OUTPUT_FILE, index=False)

print("\nCleaned Dataset")
print("-" * 50)
print(df.head())

print("\nFinal Dataset Shape:", df.shape)

print(f"\nCleaned dataset saved as: {OUTPUT_FILE}")
