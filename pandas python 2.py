import pandas as pd
import numpy as np
#    "**16.** Append a new row 'k' to `df` with your choice of values for each column.
#    Then delete that row to return the original DataFrame."
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
            'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
            'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
           'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(data,index)
print(df)
df1 = ({'animal':['goat'],
        'age':[7],
        'visits':[2],
        'priority':['yes']})
index= ['k']
df2 = pd.DataFrame(df1,index)
print(df2)

df3=df.append(df2,ignore_index=False)
print(df3)

df4 = df3.drop('k')
print(df4)

#"**17.** Count the number of each type of animal in `df`."
df5 = df4['animal'].value_counts()
print(df5)

#"**18.** Sort `df` first by the values in the 'age' in *decending* order, then by the value in the 'visit' column in *ascending*
df6 = df.sort_values("age",ascending = False)
df7 = df6.sort_values("visits",ascending = True)
print(df6)
print(df7)

#"**19.** The 'priority' column contains the values 'yes' and 'no'. Replace this column " \
#"with a column of boolean values: 'yes' should be `True` and 'no' should be `False`."
df['priority'] = df['priority'].map({'yes': True, 'no': False})
print(df['priority'])


#"**20.** In the 'animal' column, change the 'snake' entries to 'python'."
df10 = df.replace("snake","python")
print(df10)

#"**21.** For each animal type and each number of visits, find the mean age. In other words, each row is an animal," \
#" " \"each column is a number of visits and the values are the mean ages (hint: use a pivot table)."
df11 = pd.pivot_table(df, 'age', ['animal','visits'],aggfunc = np.mean)
print(df11)

