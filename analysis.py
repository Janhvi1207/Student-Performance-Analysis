import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("data/students.csv")

# Show first 5 rows
print("Dataset Preview:")
print(df.head())

# Show statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Calculate average scores
average_scores = df[['Math', 'Science', 'English']].mean()
print("\nAverage Subject Scores:")
print(average_scores)

# Plot average scores
average_scores.plot(kind='bar', title='Average Subject Scores')
plt.xlabel('Subjects')
plt.ylabel('Average Score')
plt.tight_layout()
plt.show()
