import pandas as pd
df=pd.read_json('sample1.json')
print(df.head(2))
df.info()
