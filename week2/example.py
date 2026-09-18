import pandas as pd
data=[1,2,3,4,5,6,7,8,9,10]
df=pd.DataFrame(data)
df.to_csv("output.csv", index=False)
print(df)

# names data set
import pandas as pd
data=[ "Rahul",
    "Priya",
    "Arjun",
    "Sneha",
    "Kiran",
    "Anjali",
    "Rohit",
    "Nikhil",
    "Kavya",
    "Varun"]
df=pd.DataFrame(data)
df.to_csv("friends.csv", index=False)
print(df)

# student information data set
import pandas as pd
data = {
    "Roll_No": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Name": ["Rahul", "Priya", "Arjun", "Sneha", "Kiran", "Anjali", "Rohit", "Nikhil", "Kavya", "Varun"],
    "Age": [20, 19, 21, 20, 22, 19, 21, 20, 22, 19],
    "DS": [85, 90, 78, 88, 92, 81, 76, 89, 95, 84],
    "QC": [80, 85, 75, 90, 88, 79, 82, 91, 87, 83],
    "TOC": [88, 92, 81, 86, 90, 84, 79, 93, 91, 85]
}
df=pd.DataFrame(data)
df.to_csv("Student_information.csv", index=False)
print(df)