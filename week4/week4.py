import seaborn as sns
tips=sns.load_dataset("iris")
print("Dataset shape:",tips.shape)
print(tips.head())


titanic=sns.load_dataset("titanic")
print("Dataset shape:",titanic.shape)
print(titanic.info())
print(titanic.describe())
print(titanic.head())

objective="classification: survived(Yes/No)"
success_criteria="Accuracy > 80%"
constraints="Limited features,missing values,imbalanced classes"
print("Objective:",objective)
print("Success Criteria:",success_criteria)
print("Constraints:",constraints)


