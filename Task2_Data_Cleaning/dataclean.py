import pandas as pd

# 1. Load raw data
df = pd.read_csv("rawdata.csv")

print("Original Data:")
print(df)

# 2. Standardize column names
df.columns = (
    df.columns.str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# 3. Remove duplicate rows
df = df.drop_duplicates()

# 4. Clean text columns
df["name"] = df["name"].astype("string").str.strip()
df["city"] = df["city"].astype("string").str.strip().str.title()

# 5. Convert columns to correct data types
df["age"] = pd.to_numeric(df["age"], errors="coerce")
df["salary"] = pd.to_numeric(df["salary"], errors="coerce")

# 6. Handle missing and invalid values
df["age"] = df["age"].fillna(df["age"].median())
df["city"] = df["city"].fillna("Unknown")

# Remove rows where name or salary is missing
df = df.dropna(subset=["name", "salary"])

# Convert age to integer after filling missing values
df["age"] = df["age"].astype(int)

# 7. Save cleaned data
df.to_csv("cleaned_data.csv", index=False)

# 8. Display results
print("\nCleaned Data:")
print(df)

print("\nCleaning Summary:")
print("Rows after cleaning:", len(df))
print("Missing values remaining:", df.isnull().sum().sum())
print("Output saved to cleaned_data.csv")