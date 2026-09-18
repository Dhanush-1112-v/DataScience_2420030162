import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df=sns.load_dataset("titanic")
sns.histplot(df['age'], bins=50, kde=True)
plt.title('AgeDistribution')
plt.show()

df=pd.read_csv("student.csv")
sns.histplot(df['Attendance'], bins=20, kde=True)
plt.title('Attendance Distribution')
plt.show()