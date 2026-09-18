# import seaborn as sns
# import numpy as np
# import matplotlib.pyplot as plt
# x = np.random.rand(200)
# y = np.random.rand(200)
# sns.kdeplot(x=x, y=y)
# plt.show()


# import seaborn as sns
# import matplotlib.pyplot as plt
# df=sns.load_dataset('iris')
# sns.kdeplot(x=df['petal_length'])
# sns.kdeplot(x=df['petal_width'], shade=True)
# plt.show()


# import seaborn as sns
# import matplotlib.pyplot as plt
# df=sns.load_dataset('iris')
# sns.kdeplot(x=df['petal_length'],y=df['petal_width'])
# plt.show()

# import seaborn as sns
# import matplotlib.pyplot as plt
# data=sns.load_dataset("tips")
# sns.displot(data["total_bill"],kde=True,color='red',bins=30)
# plt.show()

# import seaborn as sns
# import matplotlib.pyplot as plt
# data=sns.load_dataset("tips")
# sns.displot(data["total_bill"],kde=False,color='red',bins=30)
# plt.show()

# import seaborn as sns
# import matplotlib.pyplot as plt
# data=sns.load_dataset("tips")
# sns.jointplot(x='total_bill',y='tip',data=data)
# plt.show()

# import seaborn as sns
# import matplotlib.pyplot as plt
# data=sns.load_dataset("tips")
# sns.countplot(x='sex',hue='smoker',data=data)
# plt.show()

# import seaborn as sns
# import matplotlib.pyplot as plt
# data=sns.load_dataset("tips")
# sns.countplot(y='sex',hue='smoker',data=data)
# plt.show()


# import seaborn as sns
# import matplotlib.pyplot as plt
# data=sns.load_dataset("tips")
# sns.boxplot(data['total_bill'])
# plt.show()

# import seaborn as sns
# import matplotlib.pyplot as plt
# data=sns.load_dataset("tips")
# sns.boxplot(data['tip'])
# plt.show()

# import seaborn as sns
# import matplotlib.pyplot as plt
# data=sns.load_dataset("tips")
# sns.boxplot(data['size'])
# plt.show()

# import seaborn as sns
# import pandas as pd
# import matplotlib.pyplot as plt
# df=pd.read_csv('temporal.csv')
# sns.boxplot(df['data science'])
# plt.show()

# import seaborn as sns
# import pandas as pd
# import matplotlib.pyplot as plt
# df=pd.read_csv('temporal.csv')
# sns.boxplot(df['deep learning'])
# plt.show()


# import seaborn as sns
# import pandas as pd
# import matplotlib.pyplot as plt
# df=pd.read_csv('temporal.csv')
# sns.boxplot(df['machine learning'])
# plt.show()


# import seaborn as sns
# import pandas as pd
# import numpy as np
# df=pd.read_csv('temporal.csv')
# df
# q1=np.percentile(df['data science'],25,method='midpoint')
# q3=np.percentile(df['data science'],75,method='midpoint')
# IQR=q3-q1
# print("The out put of IQR")
# print(IQR)

#SEABORN HEAT MAPS 
# import seaborn as sns
# import numpy as np
# import matplotlib.pyplot as plt
# data=np.random.randint(1,100,(10,10))
# sns.heatmap(data)
# plt.show()

# import seaborn as sns
# import numpy as np
# import matplotlib.pyplot as plt
# data=np.random.randint(1,100,(10,10))
# sns.heatmap(data,vmin=30,vmax=70)
# plt.show()

# import seaborn as sns
# import numpy as np
# import matplotlib.pyplot as plt
# data=np.random.randint(1,100,(10,10))
# sns.heatmap(data,vmin=30,vmax=70,annot=True)
# plt.show()

# import seaborn as sns
# import numpy as np
# import matplotlib.pyplot as plt
# data=np.random.randint(1,100,(10,10))
# sns.heatmap(data,cmap='tab20',annot=True)
# plt.show()

# import seaborn as sns
# import numpy as np
# import matplotlib.pyplot as plt
# data=sns.load_dataset('tips')
# sns.heatmap(data[['tip']])
# plt.show()

# import seaborn as sns
# import numpy as np
# import matplotlib.pyplot as plt
# data=sns.load_dataset('iris')
# sns.heatmap(data[['petal_length']])
# plt.show()


#HISTOGRAMS
# import seaborn as sns
# import matplotlib.pyplot as plt
# data=[12,15,20,20,22,23,25,25,25,30,32,35,40]
# plt.hist(data,bins=5,color='red',edgecolor='green')
# plt.title('Histogram example')
# plt.xlabel('Values range')
# plt.ylabel('Frequency')
# plt.show()

# import seaborn as sns
# import matplotlib.pyplot as plt
# data=sns.load_dataset("tips")
# plt.hist(data['total_bill'],bins=10,color='pink',edgecolor='blue')
# plt.title('Histogram example')
# plt.xlabel('Values range')
# plt.ylabel('Frequency')
# plt.show()

# import seaborn as sns
# import matplotlib.pyplot as plt
# data=sns.load_dataset("iris")
# sns.violinplot(x='species',y=data['petal_length'],data=data)
# plt.title('Violin plot')
# plt.show()
