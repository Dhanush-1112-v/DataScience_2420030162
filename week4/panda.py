import pandas as pd
data={'apples':[3,2,0,1],'oranges':[0,3,7,2]}
df=pd.DataFrame(data)
print(df)

# with index specified

import pandas as pd
data={'apples':[3,2,0,1],'oranges':[0,3,7,2]}
df=pd.DataFrame(data,index=['dhanu','shetty','cherry','ammu'])
print(df)

# READING LOCATION OF DATAFRAME
import pandas as pd
data={'apples':[3,2,0,1],'oranges':[0,3,7,2]}
df=pd.DataFrame(data,index=['dhanu','shetty','cherry','ammu'])
print(df.loc['dhanu'])