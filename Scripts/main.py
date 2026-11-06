import pandas as pd

pd.set_option('display.max_columns', None)

print("Reading Healthcare Claims Data...")

df = pd.read_csv("Data/claims.csv")

print("\nOriginal Data:")
print(df)

print("\nMissing Values:")
print(df.isnull().sum())

df["amount"] = df["amount"].fillna(
    df["amount"].mean()
)

print("\nCleaned Data:")
print(df)

df.to_csv(
    "Data/cleaned_claims.csv",
    index=False
)

print("\nCleaned claims file saved successfully!")
print("\nClaims Status Summary:")

print(
    df["status"].value_counts()
)