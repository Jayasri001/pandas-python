
#"**1.** Import pandas under the name `pd`."
import pandas as pd
#"**2.** Print the version of pandas that has been imported."
import numpy as np
print(pd.__version__)
#"**3.** Print out all the version information of the libraries that are required by the pandas library."
pd.show_versions()
#"**4.** Create a DataFrame `df` from this dictionary `data` which has the index `labels`."

data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
            'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
            'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
           'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(data,index)
#"**5.** Display a summary of the basic information about this DataFrame and its data."
df.info()
print(df)

#"**6.** Return the first 3 rows of the DataFrame `df`."
df1 = df.head(3)
print(df1)
#"**7.** Select just the 'animal' and 'age' columns from the DataFrame `df
print(df[['animal','age']])

#"**8.** Select the data in rows `[3, 4, 8]` *and* in columns `['animal', 'age']`."
df2 = (df[["animal","age"]].loc[["d","e","i"],:])

print(df2)

#"**9.** Select only the rows where the number of visits is greater than 3."
df3 = df[df["visits"]>3]
print(df3)

#"**10.** Select the rows where the age is missing, i.e. is `NaN`."

df4 = df[df["age"].isnull()]
print(df4)

#"**11.** Select the rows where the animal is a cat *and* the age is less than 3."
df5 = df[(df["animal"]== "cat")& (df["age"]<3)]
print(df5)

#"**12.** Select the rows the age is between 2 and 4 (inclusive)."
df6 = df["age"].between(2, 4, inclusive=True)
print(df[df6])

#"**13.** Change the age in row 'f' to 1.5."
df7 =df[(df.loc['f',['age']])] = 1.5
print(df7)

#"**14.** Calculate the sum of all visits (the total number of visits)."
df8 = df['visits'].sum()
print(df8)

#"**15.** Calculate the mean age for each different animal in `df`."
df9 = df['age'].mean()
print(df9)

