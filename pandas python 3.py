import pandas as pd
import numpy as np
#"**22.** You have a DataFrame `df` with a column 'A' of integers. For example:\n",
#"How do you filter out rows which contain the same integer as the row immediately above?"
df = pd.DataFrame({'A': [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7]})
print(df)
duplicate = df.loc[df.duplicated('A',keep='last'),:]
print(duplicate)
#how do you subtract the row mean from each element in the row?
#"**23.** Given a DataFrame of numeric values, say\n"
#df = pd.DataFrame(np.random.random(size=(5, 3))) # a 5x3 frame of float values\n",
df2 = pd.DataFrame(np.random.random(size=(5, 3)))
print(df2)
df3 = df2.mean(axis=1)
print(df3)
df4=df2.sub(df3,axis=1)
print(df4)

#"**24.** Suppose you have DataFrame with 10 columns of real numbers, for example:\n
#"Which column of numbers has the smallest sum? (Find that column's label.)
df5 = pd.DataFrame(np.random.random(size=(5, 10)), columns=list('abcdefghij'))
print(df5)
df6 = df5.sum().idxmin()
print(df6)

#"**25.** How do you count how many unique rows a DataFrame has (i.e. ignore all rows that are duplicates)?"
df7 = len(df5.drop_duplicates(keep=False))
print(df7)

#26 You have a DataFrame that consists of 10 columns of floating--point numbers. Suppose that exactly 5 entries
# in each row are NaN values. For each row of the DataFrame, find the *column* which contains the *third* NaN value.
# \n",
df8 = (df5.isnull().cumsum(axis=1) == 3).idxmax(axis=1)
print(df8)

#"**27.** A DataFrame has a column of groups 'grps' and and column of numbers 'vals'. For example: \n",
df9 = pd.DataFrame({'grps': list('aaabbcaabcccbbc'),
                      'vals': [12,345,3,1,45,14,4,52,54,23,235,21,57,3,87]})
print(df9.groupby('grps')['vals'].nlargest(3).sum(level=0))

#    "**28.** A DataFrame has two integer columns 'A' and 'B'. The values in 'A' are between 1 and 100 (inclusive).
#    For each group of 10 consecutive integers in 'A' (i.e. `(0, 10]`, `(10, 20]`, ...),
#    calculate the sum of the corresponding values in column 'B'."

df11 = df.groupby(pd.cut(df['A'], np.arange(0, 101, 10)))['B'].sum()
print(df11)