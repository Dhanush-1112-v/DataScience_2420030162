import seaborn as sns
import pandas as pd
df=pd.read_csv("student.csv")
#finding duplicates
df.drop_duplicates(inplace=True)
#finding duplicates 
df=pd.get_dummies(df,columns=['Gender','Department'],drop_first=True)
print(df.head())