import pandas as pd
from scipy.stats import spearmanr

# Example Dataset
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1]
})

# Pearson correlation
cor_mat = df.corr(method='pearson')
print("Pearson Correlation Matrix:\n", cor_mat)

# Spearman correlation
corr_values, p_value = spearmanr(df['A'], df['B'])
print("Spearman Correlation Coefficient:", corr_values)
print("P-Value:", p_value)


# Correlation using 3 subjects marks
df = pd.DataFrame({
    'math': [10, 20, 34, 43, 57],
    'science': [55, 44, 33, 22, 11],
    'physics': [26, 32, 45, 57, 68]
})

cor_mat = df.corr(method='pearson')
print("Pearson Correlation Matrix:\n", cor_mat)

# Spearman 3 subjects
corr_values, p_value = spearmanr(df[['math', 'science', 'physics']])
print("Spearman Correlation Matrix:\n", corr_values)
print("P-Value Matrix:\n", p_value)


# Iris dataset
df = pd.read_csv('iris.csv')

print("Pearson Correlation Matrix:\n")
print(df.corr(method='pearson', numeric_only=True))

print("Spearman Correlation Matrix:\n")
print(df.corr(method='spearman', numeric_only=True))