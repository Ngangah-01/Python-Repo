import pandas as pd
from sklearn import datasets
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
iris = datasets.load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["species"] = pd.Categorical.from_codes(iris.target, iris.target_names)

print(df.columns)

# Display first few rows
print(df.head())
# Check dataset structure
print("\nDataset Info:")
print(df.info())

# Check for missing values
print("Missing values in each column:\n", df.isnull().sum())

# Drop rows with any missing values
df.dropna(inplace=True)

print("\nCleaned Dataset:\n", df.head())

statistics = df.describe()
print("Basic Statistics:\n", statistics)

#Visualizing the data using graphs

# 1. Line Chart
plt.figure(figsize=(8, 5))
plt.plot(df.index, df["sepal length (cm)"], label="Sepal Length", linestyle="dashed", color="blue")
plt.plot(df.index, df["petal length (cm)"], label="Petal Length", linestyle="solid", color="red")
plt.xlabel("Sample Index")
plt.ylabel("Length (cm)")
plt.title("Line Chart: Sepal and Petal Length over Samples")
plt.legend()
plt.show()

# Bar Chart: Average Petal Length per Species
plt.figure(figsize=(8, 5))
sns.barplot(x="species", y="petal length (cm)", data=df, palette="viridis")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.title("Bar Chart: Average Petal Length per Species")
plt.show()

#3. Histogram: Sepal Length Distribution
plt.figure(figsize=(6, 4))
plt.hist(df["sepal length (cm)"], bins=15, color="teal", edgecolor="black", alpha=0.7)
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.title("Histogram: Sepal Length Distribution")
plt.show()

#Scatter Plot: Sepal Length vs Petal Length
plt.figure(figsize=(6, 4))
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="species", data=df, palette="coolwarm", edgecolor="black")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.title("Scatter Plot: Sepal vs Petal Length")
plt.legend(title="Species")
plt.show()
