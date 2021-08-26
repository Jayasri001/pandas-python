import pandas as pd
import numpy as np
#    "**28.** A DataFrame has two integer columns 'A' and 'B'. The values in 'A' are between 1 and 100 (inclusive).
#    For each group of 10 consecutive integers in 'A' (i.e. `(0, 10]`, `(10, 20]`, ...),
#    calculate the sum of the corresponding values in column 'B'."
s= pd.Series(range(1,101))
df = pd.DataFrame({'A': s,'B': s})
print(df)
print(df.groupby(pd.cut(df['A'], np.arange(0, 101, 10)))['B'].sum())

#"**29.** Consider a DataFrame `df` where there is an integer column 'X':\n"
#"For each value, count the difference back to the previous zero (or the start of the Series, whichever is closer).
# These values should therefore be `[1, 2, 0, 1, 2, 3, 4, 0, 1, 2]`. Make this a new column 'Y'."
df2 = pd.DataFrame({'X': [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]})
df2['Y'] = [1, 2, 0, 1, 2, 3, 4, 0, 1, 2]
print(df2)
x=(df2['X']!=0).cumsum()
y= x!=x.shift()
df3 = df2['Y']=y.groupby((y!=y.shift()).cumsum()).cumsum()
print(df3)

#    "**30.** Consider a DataFrame containing rows and columns of purely numerical data.
#    Create a list of the row-column index locations of the 3 largest values."
df4 = pd.DataFrame(np.random.randn(5,3),columns = ["A","B","C"])
print(df4.unstack().sort_values()[-3:].index.tolist())

#"**31.** Given a DataFrame with a column of group IDs, 'grps', and a column of corresponding integer values,
#    'vals',replace any negative values in 'vals' with the group mean."
df5 = pd.DataFrame(np.random.randn(5,2),columns = ["grps","vals"])
print(df5)
def replace(grps):
    mask = grps<0
    grps[mask] = grps[~mask].mean()
    return grps

print(df5.groupby(['grps'])['vals'].transform(replace))

#"**32.** Implement a rolling mean over groups with window size 3, which ignores NaN value. For example consider
df6 = pd.DataFrame({'group': list('aabbabbbabab'),
                       'value': [1, 2, 3, np.nan, 2, 3, np.nan, 1, 7, 3, np.nan, 8]})
print(df6)
g1 = df6.groupby(['group'])['value']              # group values
g2 = df6.fillna(0).groupby(['group'])['value']    # fillna, then group values

s = g2.rolling(3, min_periods=1).sum() / g1.rolling(3, min_periods=1).count() # compute means

print(s.reset_index(level=0, drop=True).sort_index())  # drop/sort index
#    "**33.** Create a DatetimeIndex that contains each business day of 2015 and use it to index a
# Series of random numbers. Let's call this Series `s`."

df7 = pd.date_range(start='2015-01-01', end='2015-12-31', freq='b')
s = pd.Series(np.random.rand(len(df7)), index=df7)
print(s)
#**34.** Find the sum of the values in `s` for every Wednesday."
s1 = s[s.index.weekday == 2].sum()
print(s1)
# "**35.** For each calendar month in `s`, find the mean of values."
s2 = s.resample('M').mean()
print(s2)
#"**36.** For each group of four consecutive calendar months in `s`," \
#" find the date on which the highest value occurred."
s3 = s.groupby(pd.Grouper(freq='4MS',label='right')).max()[:3]
print(s3)

#"**37.** Create a DateTimeIndex consisting of the third Thursday in each month for the years 2015 and 2016."
s4 = pd.date_range('2015-01-01', '2016-12-31', freq='WOM-3THU')
print(s4)

