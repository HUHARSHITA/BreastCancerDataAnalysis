import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
file_path = 'df.xlsx'  # Update this path as needed
df = pd.read_excel(file_path)

# Print column names to inspect
print(df.columns)

# Summary statistics
summary_stats = df.describe()
print(summary_stats)

# Distribution of diagnoses
diagnosis_counts = df['diagnosis'].value_counts()
plt.figure(figsize=(8, 6))
diagnosis_counts.plot(kind='bar', color=['#1f77b4', '#ff7f0e'])  # Custom colors
plt.title('Count of Diagnoses')
plt.xlabel('Diagnosis')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.savefig('diagnosis_distribution.png')
plt.show()

# Feature distributions
features = ['Radius_mean', 'Texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean']
for feature in features:
    if feature in df.columns:
        plt.figure(figsize=(8, 6))
        plt.hist(df[feature], bins=30, color='#2ca02c', alpha=0.7)  # Custom color
        plt.title(f'Distribution of {feature}')
        plt.xlabel(feature)
        plt.ylabel('Frequency')
        plt.savefig(f'{feature}_distribution.png')
        plt.show()
    else:
        print(f"Feature '{feature}' not found in columns")

# Scatter plot
plt.figure(figsize=(10, 8))
colors = df['diagnosis'].map({'M': '#d62728', 'B': '#1f77b4'})  # Custom colors
plt.scatter(df['Radius_mean'], df['Texture_mean'], c=colors, alpha=0.6)
plt.title('Radius Mean vs Texture Mean')
plt.xlabel('Radius Mean')
plt.ylabel('Texture Mean')
plt.legend(['Malignant', 'Benign'], loc='upper right')
plt.savefig('scatter_radius_texture.png')
plt.show()

# Correlation matrix - exclude non-numeric columns
numeric_df = df.select_dtypes(include=[float, int])
plt.figure(figsize=(16, 12))  # Increased figure size
correlation_matrix = numeric_df.corr()
sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', linewidths=.5, annot_kws={"size": 8})
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels
plt.yticks(rotation=0)  # Rotate y-axis labels
plt.title('Correlation Matrix')
plt.savefig('correlation_matrix.png')
plt.show()
