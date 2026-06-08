import pandas as pd

df = pd.read_csv("climate_dataset.csv", parse_dates=["Date"])

# ─────────────────────────────
# 1. FIRST LOOK
# ─────────────────────────────
print("Shape:", df.shape)
print()
print("Column Names:")
print(df.columns.tolist())
print()
print("Data Types:")
print(df.dtypes)
print()
print("First 5 Rows:")
print(df.head())

# ─────────────────────────────
# 2. SUMMARY STATISTICS
# ─────────────────────────────
print("\n--- Summary Statistics ---")
print(df.describe())

print("\nAQI Mean:  ", df["AQI"].mean().round(2))
print("AQI Median:", df["AQI"].median())
print("AQI Std:   ", df["AQI"].std().round(2))
print("AQI Min:   ", df["AQI"].min())
print("AQI Max:   ", df["AQI"].max())

# ─────────────────────────────
# 3. MISSING VALUES
# ─────────────────────────────
print("\n--- Missing Values ---")
print(df.isnull().sum())

# ─────────────────────────────
# 4. UNIQUE VALUES & FREQUENCY
# ─────────────────────────────
print("\n--- Unique Cities ---")
print(df["City"].unique())

print("\n--- AQI Category Counts ---")
print(df["AQI_Category"].value_counts())

print("\n--- AQI Category Percentage ---")
print(df["AQI_Category"].value_counts(normalize=True).mul(100).round(2))

# ─────────────────────────────
# 5. GROUPBY
# ─────────────────────────────
print("\n--- Average AQI per City ---")
print(df.groupby("City")["AQI"].mean().round(2))

print("\n--- Total Rainfall per City ---")
print(df.groupby("City")["Rainfall (mm)"].sum().round(2))

print("\n--- AQI Stats per City ---")
print(df.groupby("City")["AQI"].agg(["mean", "min", "max", "std"]).round(2))

# ─────────────────────────────
# 6. CORRELATION
# ─────────────────────────────
print("\n--- Correlation with AQI ---")
print(df.corr(numeric_only=True)["AQI"].sort_values(ascending=False).round(3))

# ─────────────────────────────
# 7. FILTERING
# ─────────────────────────────
print("\n--- Delhi Data Sample ---")
print(df[df["City"] == "Delhi"].head())

print("\n--- Days with AQI > 300 ---")
print(df[df["AQI"] > 300][["Date", "City", "AQI", "AQI_Category"]])

print("\n--- Delhi in Winter with Bad AQI ---")
delhi_winter = df[(df["City"] == "Delhi") & (df["AQI"] > 200)]
print(delhi_winter[["Date", "AQI", "AQI_Category"]].head(10))

# ─────────────────────────────
# 8. TIME-BASED ANALYSIS
# ─────────────────────────────
df["Month"]      = df["Date"].dt.month
df["Year"]       = df["Date"].dt.year
df["Month_Name"] = df["Date"].dt.strftime("%b")

print("\n--- Monthly Average AQI ---")
print(df.groupby("Month")["AQI"].mean().round(2))

print("\n--- Monthly Average Rainfall ---")
print(df.groupby("Month_Name")["Rainfall (mm)"].mean().round(2))

# ─────────────────────────────
# 9. PIVOT TABLE
# ─────────────────────────────
print("\n--- Avg Temperature: City vs Month ---")
pivot = df.pivot_table(
    values="Temperature_Avg (°C)",
    index="City",
    columns="Month_Name",
    aggfunc="mean"
).round(1)
print(pivot)

# ─────────────────────────────
# 10. RANKING & SORTING
# ─────────────────────────────
print("\n--- Top 5 Most Polluted Days ---")
print(df.nlargest(5, "AQI")[["Date", "City", "AQI", "AQI_Category"]])

print("\n--- Top 5 Rainiest Days ---")
print(df.nlargest(5, "Rainfall (mm)")[["Date", "City", "Rainfall (mm)"]])

print("\n--- City Ranking by Avg AQI (Worst to Best) ---")
ranking = df.groupby("City")["AQI"].mean().round(2).sort_values(ascending=False)
print(ranking)
