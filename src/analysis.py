# src/analysis.py
# NYC Public Schools SAT Performance Analysis
# Author: Kiarash Aghakhani
# Date: 2025

import pandas as pd
import matplotlib.pyplot as plt
import os

# Set plot style
plt.rcParams['font.size'] = 12
plt.rcParams['figure.figsize'] = (10, 6)

# Create output directories
os.makedirs("../results", exist_ok=True)
os.makedirs("../plots", exist_ok=True)

# Load dataset
schools = pd.read_csv("../data/schools.csv")

print("Dataset loaded successfully.")
print(f"Total schools: {len(schools)}")
print(f"Boroughs: {', '.join(schools['borough'].unique())}\n")

# Question 1
best_math_schools = schools[schools["average_math"] >= 640][["school_name", "average_math"]]
best_math_schools = best_math_schools.sort_values("average_math", ascending=False).reset_index(drop=True)
print("Best Math Schools (average_math >= 640):")
print(best_math_schools.head(10))
best_math_schools.to_csv("../results/best_math_schools.csv", index=False)

# Question 2
schools["total_SAT"] = schools["average_math"] + schools["average_reading"] + schools["average_writing"]
top_10_schools = schools[["school_name", "total_SAT"]].sort_values("total_SAT", ascending=False).head(10).reset_index(drop=True)
print("\nTop 10 Schools by Total SAT:")
print(top_10_schools)
top_10_schools.to_csv("../results/top_10_schools.csv", index=False)

# Question 3
borough_stats = schools.groupby("borough")["total_SAT"].agg(
    num_schools="count",
    average_SAT="mean",
    std_SAT="std"
).round(2).reset_index()

largest_std_dev = borough_stats.loc[borough_stats["std_SAT"].idxmax()].to_frame().T
largest_std_dev["num_schools"] = largest_std_dev["num_schools"].astype(int)
largest_std_dev = largest_std_dev[["borough", "num_schools", "average_SAT", "std_SAT"]].reset_index(drop=True)
print("\nBorough with Largest Standard Deviation in SAT:")
print(largest_std_dev)
largest_std_dev.to_csv("../results/largest_std_dev.csv", index=False)

# Plot 1: Top 10 schools
plt.figure()
plt.barh(top_10_schools["school_name"], top_10_schools["total_SAT"], color='skyblue')
plt.xlabel("Total SAT Score")
plt.title("Top 10 NYC Schools by Total SAT Score")
plt.gca().invert_yaxis()
for i, v in enumerate(top_10_schools["total_SAT"]):
    plt.text(v + 10, i, str(v), va='center')
plt.tight_layout()
plt.savefig("../plots/top_10_schools_bar.png", dpi=300, bbox_inches='tight')
plt.show()

# Plot 2: Boxplot by borough
plt.figure()
schools.boxplot(column="total_SAT", by="borough", ax=plt.gca())
plt.title("SAT Score Distribution by Borough")
plt.suptitle("")  # Remove default title
plt.xlabel("Borough")
plt.ylabel("Total SAT Score")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../plots/borough_sat_distribution.png", dpi=300, bbox_inches='tight')
plt.show()

# Plot 3: Scatter
plt.figure()
for borough in schools["borough"].unique():
    data = schools[schools["borough"] == borough]
    plt.scatter(data["average_math"], data["total_SAT"], label=borough, alpha=0.7)
plt.title("Average Math vs Total SAT Score")
plt.xlabel("Average Math Score")
plt.ylabel("Total SAT Score")
plt.legend(title="Borough")
plt.tight_layout()
plt.savefig("../plots/math_vs_total_scatter.png", dpi=300, bbox_inches='tight')
plt.show()

print("\nAll results and plots have been saved!")