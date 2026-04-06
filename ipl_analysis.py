import pandas as pd
import matplotlib.pyplot as plt

print("IPL Data Analysis Project")

# Load dataset
df = pd.read_csv("ipl.csv")

# -------------------------------
# Dataset Preview
# -------------------------------
print("Dataset Preview:\n")
print(df.head())

# -------------------------------
# 1. Top Winning Teams
# -------------------------------
wins = df["winner"].value_counts()

print("\nTop Winning Teams:\n")
print(wins.head())

wins.head(5).plot(kind="bar")
plt.title("Top 5 IPL Teams by Wins")
plt.xlabel("Teams")
plt.ylabel("Wins")
plt.tight_layout()
plt.show()

# -------------------------------
# 2. Toss Impact Analysis
# -------------------------------
toss_win_match = df[df["toss_winner"] == df["winner"]]

print("\nMatches won after winning toss:", len(toss_win_match))
print("Total matches:", len(df))

# -------------------------------
# 3. City-wise Matches
# -------------------------------
print("\nTop Cities by Matches:\n")
print(df["city"].value_counts().head())

# -------------------------------
# 4. Toss Decision Analysis
# -------------------------------
df["toss_decision"].value_counts().plot(kind="bar")
plt.title("Toss Decision Distribution")
plt.xlabel("Decision")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# -------------------------------
# 5. Top Players (Player of Match)
# -------------------------------
top_players = df["player_of_match"].value_counts().head(10)

print("\nTop Players of the Match:\n", top_players)

top_players.plot(kind="bar")
plt.title("Top 10 Player of the Match Winners")
plt.xlabel("Players")
plt.ylabel("Awards")
plt.tight_layout()
plt.show()

# -------------------------------
# 6. Win Analysis (Runs vs Wickets)
# -------------------------------
print("\nAverage Win by Runs:", df["win_by_runs"].mean())
print("Average Win by Wickets:", df["win_by_wickets"].mean())

# -------------------------------
# 7. Matches per Season
# -------------------------------
df["season"].value_counts().sort_index().plot(kind="bar")
plt.title("Matches per Season")
plt.xlabel("Season")
plt.ylabel("Matches")
plt.tight_layout()
plt.show()

# -------------------------------
# 8. Most Popular Venues
# -------------------------------
print("\nTop Venues:\n", df["venue"].value_counts().head())