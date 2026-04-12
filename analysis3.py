import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ============================
# 1. Load data
# ============================
df = pd.read_csv("Machine_learning/datawarehouse/final_dataset.csv")
df.columns = df.columns.str.strip()
df_grouped = df.groupby("state_name", as_index=False).agg({
    "deaths": "sum",          # total deaths per state
    "poverty_rate": "first"   # same per state
})

# ============================
# 3. Plot (Figure 18)
# ============================
sns.set(style="whitegrid")

plt.figure(figsize=(9,6))

sns.regplot(
    data=df_grouped,
    x="poverty_rate",
    y="deaths",
    scatter_kws={"s": 80},
    line_kws={"color": "red"}
)

# Label top 10 states
top_states = df_grouped.nlargest(10, "deaths")

for _, row in top_states.iterrows():
    plt.text(
        row["poverty_rate"] + 0.2,
        row["deaths"] + 5,
        row["state_name"],
        fontsize=9
    )

plt.xlabel("Poverty Rate (%)")
plt.ylabel("Total Lightning-Induced Fatalities")
plt.title("Poverty Rate vs Lightning-Induced Fatalities by State")

plt.tight_layout()
plt.savefig("poverty_vs_fatalities.png", dpi=300)

plt.show()