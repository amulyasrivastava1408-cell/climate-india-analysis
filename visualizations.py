import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ─────────────────────────────
# SETUP
# ─────────────────────────────
df = pd.read_csv("climate_dataset.csv", parse_dates=["Date"])

df["Month"]      = df["Date"].dt.month
df["Month_Name"] = df["Date"].dt.strftime("%b")
df["Season"]     = df["Month"].map({
    12:"Winter",  1:"Winter",  2:"Winter",
     3:"Summer",  4:"Summer",  5:"Summer",
     6:"Monsoon", 7:"Monsoon", 8:"Monsoon",
     9:"Post-Monsoon", 10:"Post-Monsoon", 11:"Post-Monsoon"
})

MONTH_ORDER  = ["Jan","Feb","Mar","Apr","May","Jun",
                "Jul","Aug","Sep","Oct","Nov","Dec"]
SEASON_ORDER = ["Winter","Summer","Monsoon","Post-Monsoon"]

print("Data loaded successfully!")
print("Shape:", df.shape)


# ─────────────────────────────
# 1. BAR CHART
# — Average AQI by City
# ─────────────────────────────
city_aqi = df.groupby("City")["AQI"].mean().sort_values(ascending=False)

plt.figure(figsize=(10, 5))
plt.bar(city_aqi.index, city_aqi.values, color="steelblue", edgecolor="white")
plt.title("Average AQI by City")
plt.xlabel("City")
plt.ylabel("Average AQI")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()
print("1. Bar chart done")


# ─────────────────────────────
# 2. LINE CHART
# — Monthly Average Temperature
# ─────────────────────────────
monthly_temp = df.groupby("Month_Name")["Temperature_Avg (°C)"].mean().reindex(MONTH_ORDER)

plt.figure(figsize=(10, 5))
plt.plot(MONTH_ORDER, monthly_temp.values, marker="o", color="tomato", linewidth=2)
plt.title("Monthly Average Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
print("2. Line chart done")


# ─────────────────────────────
# 3. HISTOGRAM
# — Distribution of AQI
# ─────────────────────────────
plt.figure(figsize=(8, 5))
plt.hist(df["AQI"], bins=30, color="mediumpurple", edgecolor="white")
plt.title("Distribution of AQI Values")
plt.xlabel("AQI")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()
print("3. Histogram done")


# ─────────────────────────────
# 4. BOX PLOT
# — AQI spread per City
# ─────────────────────────────
plt.figure(figsize=(12, 5))
sns.boxplot(data=df, x="City", y="AQI", palette="Set2")
plt.title("AQI Distribution by City")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()
print("4. Box plot done")


# ─────────────────────────────
# 5. SCATTER PLOT
# — Humidity vs AQI
# ─────────────────────────────
plt.figure(figsize=(8, 5))
plt.scatter(df["Humidity (%)"], df["AQI"], alpha=0.3, s=10, color="teal")
plt.title("Humidity vs AQI")
plt.xlabel("Humidity (%)")
plt.ylabel("AQI")
plt.tight_layout()
plt.show()
print("5. Scatter plot done")


# ─────────────────────────────
# 6. HEATMAP
# — Average Temperature: City vs Month
# ─────────────────────────────
pivot = df.pivot_table(
    values="Temperature_Avg (°C)",
    index="City",
    columns="Month_Name",
    aggfunc="mean"
).reindex(columns=MONTH_ORDER)

plt.figure(figsize=(14, 6))
sns.heatmap(pivot, annot=True, fmt=".1f", cmap="YlOrRd", linewidths=0.5)
plt.title("Average Temperature: City vs Month")
plt.tight_layout()
plt.show()
print("6. Heatmap done")


# ─────────────────────────────
# 7. PIE CHART
# — AQI Category Breakdown
# ─────────────────────────────
counts = df["AQI_Category"].value_counts()

plt.figure(figsize=(7, 7))
plt.pie(counts.values, labels=counts.index, autopct="%1.1f%%", startangle=140)
plt.title("AQI Category Breakdown")
plt.tight_layout()
plt.show()
print("7. Pie chart done")


# ─────────────────────────────
# 8. VIOLIN PLOT
# — AQI Distribution by Season
# ─────────────────────────────
plt.figure(figsize=(10, 5))
sns.violinplot(data=df, x="Season", y="AQI", order=SEASON_ORDER, palette="Set3")
plt.title("AQI Distribution by Season")
plt.tight_layout()
plt.show()
print("8. Violin plot done")


# ─────────────────────────────
# 9. SUBPLOTS
# — AQI by City + Rainfall by Season
# ─────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Left chart
axes[0].bar(city_aqi.index, city_aqi.values, color="steelblue", edgecolor="white")
axes[0].set_title("Avg AQI by City")
axes[0].set_ylabel("AQI")
axes[0].tick_params(axis="x", rotation=30)

# Right chart
sns.boxplot(data=df, x="Season", y="Rainfall (mm)",
            order=SEASON_ORDER, palette="Blues", ax=axes[1])
axes[1].set_title("Rainfall Distribution by Season")
axes[1].set_ylabel("Rainfall (mm)")

plt.tight_layout()
plt.show()
print("9. Subplots done")

print("\nAll 9 charts completed!")
