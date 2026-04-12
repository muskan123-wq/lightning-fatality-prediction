import pandas as pd
import matplotlib.pyplot as plt
import os

# ============================
# 1. Load data
# ============================
base_path = os.path.dirname(__file__)

intensity_df = df = pd.read_csv("Machine_learning/datawarehouse/lightning_intensity.csv")
fatalities_df = pd.read_csv("Machine_learning/datawarehouse/lightning_fatalities.csv")

# ============================
# 2. Clean numeric columns
# ============================

# Lightning intensity
intensity_df["lightning_intensity"] = (
    intensity_df["lightning_intensity"]
    .astype(str)
    .str.replace(",", "", regex=True)
)
intensity_df["lightning_intensity"] = pd.to_numeric(
    intensity_df["lightning_intensity"], errors="coerce"
)

# Fatalities
fatalities_df["num_deaths"] = (
    fatalities_df["num_deaths"]
    .astype(str)
    .str.replace(",", "", regex=True)
)
fatalities_df["num_deaths"] = pd.to_numeric(
    fatalities_df["num_deaths"], errors="coerce"
)

# ============================
# 3. Merge datasets (FIXED)
# ============================
merged_df = pd.merge(
    intensity_df,
    fatalities_df,
    on=["state", "year"], 
    how="inner"
)

merged_df = merged_df.dropna(
    subset=["lightning_intensity", "num_deaths"]
)

# ============================
# 4. FIGURE 16
# ============================
plt.figure()

plt.scatter(
    merged_df["lightning_intensity"],
    merged_df["num_deaths"],
    alpha=0.7
)

plt.xscale("log")
plt.xlabel("Lightning Intensity (log scale)")
plt.ylabel("Lightning-Induced Fatalities")
plt.title("Lightning Intensity vs Fatalities (2019–2020)")

plt.grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig(os.path.join(base_path, "intensity_vs_fatalities.png"), dpi=300)
plt.show()

# ============================
# 5. FIGURE 17
# ============================

avg_intensity = (
    intensity_df
    .groupby("state", as_index=False)["lightning_intensity"]
    .mean()
)

avg_intensity = avg_intensity.sort_values(
    by="lightning_intensity",
    ascending=False
)

plt.figure()

plt.bar(
    avg_intensity["state"],
    avg_intensity["lightning_intensity"]
)

plt.xlabel("State")
plt.ylabel("Average Lightning Intensity")
plt.title("Average Lightning Intensity by State (2019–2020)")

plt.xticks(rotation=90)

plt.tight_layout()
plt.show()