import pandas as pd
import numpy as np

df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm',
                               'Budapest_PaRis', 'Brussels_londOn'],
              'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
              'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
                   'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
                               '12. Air France', '"Swiss Air"']})
print(df)
#"**38.** Some values in the the FlightNumber column are missing." \
#" These numbers are meant to increase by 10 with each row so 10055 and 10075 need to be put in place." \
#" Fill in these missing numbers and make the column an integer column (instead of a float column)."
df['FlightNumber'] = df['FlightNumber'].interpolate().astype(int)
print(df['FlightNumber'])

#"**39.** The From_To column would be better as two separate columns! Split each string on the underscore delimiter" \
#" `_` to give" "a new temporary DataFrame with the correct values. Assign the correct column names to this temporary DataFrame. "
sep = df.From_To.str.split('_',expand = True)
sep.columns = ['From','To']
print(sep[sep.columns])

#"**40.** Notice how the capitalisation of the city names is all mixed up in this temporary DataFrame." \
#" Standardise the strings so that only the first letter is uppercase (e.g. \"londON\" should become \"London\".)"
sep['From'] = sep['From'].str.capitalize()
sep['To'] = sep['To'].str.capitalize()
print(sep['From'] , sep['To'])

#"**41.** Delete the From_To column from `df` and attach the temporary DataFrame from the previous questions."
df = df.drop('From_To',axis=1)
print(df.join(sep))

#"**42**. In the Airline column, you can see some extra puctuation and symbols have appeared around the " \
#"airline names. Pull out just the airline name. E.g. `'(British Airways. )'` should become `'British Airways'`."
df['Airline'] = df['Airline'].str.extract('([a-zA-Z\s]+)', expand=False).str.strip()
print(df['Airline'])

#"**43**. In the RecentDelays column, the values have been entered into the DataFrame as a list." \
#" We would like each first value in its own" \
#" column, each second value in its own column, and so on. If there isn't an Nth value, the value should be NaN.\n",
df4 = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm',
                               'Budapest_PaRis', 'Brussels_londOn'],
              'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
              'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
                   'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
                               '12. Air France', '"Swiss Air"']})

delays = df4['RecentDelays'].apply(pd.Series)

delays.columns = ['delay_{}'.format(n) for n in range(1, len(delays.columns)+1)]

df5 = df4.drop('RecentDelays', axis=1).join(delays)
print(df5)
#    "**44**. Given the lists `letters = ['A', 'B', 'C']` and `numbers = list(range(10))`,
#    construct a MultiIndex object from the product of the two lists. Use it to index a Series of random numbers.
#    Call this Series `s`."
letters = ['A', 'B', 'C']
numbers = list(range(10))

multiindex = pd.MultiIndex.from_product([letters,numbers])
s = pd.Series(np.random.rand(30),index = multiindex)
print(s)


#    "**45.** Check the index of `s` is lexicographically sorted
#    (this is a necessary proprty for indexing to work correctly with a MultiIndex)."

#"**46**. Select the labels `1`, `3` and `6` from the second level of the MultiIndexed Series."
df7 = s.loc[:,[1,3,6]]
print(df7)
#    "**47**. Slice the Series `s`; slice up to label 'B' for the first level and from label 5 onwards
#    for the second level."
df8 = s.loc[pd.IndexSlice[:'B', 5:]]
print(df8)

#"**48**. Sum the values in `s` for each label in the first level
# (you should have Series giving you a total for labels A, B and C)."
df9 = s.sum(level=0)
print(df9)
#    "**49**. Suppose that `sum()` (and other methods) did not accept a `level` keyword argument.
#    How else could you perform the equivalent of `s.sum(level=1)`?"
df10 = s.unstack().sum(axis=0)
print(df10)
# "**50**. Exchange the levels of the MultiIndex so we have an index of the form (letters, numbers).
# Is this new Series properly lexsorted? If not, sort it."
s1 = s.swaplevel(0, 1)

print(s1.index.is_lexsorted())

s1 = s1.sort_index()
print(s1)

#