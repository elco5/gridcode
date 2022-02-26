import wt3k
import pandas as pd


wt = wt3k.WT3K()

file = 'pa_data.csv'

wt.read_in_file(file)

#print(wt.data.head(3))
#print(wt.data.loc[0])
#print(wt.data.iloc[0,0])# - First element of first column)
print(type(wt.data['U-3']))

# for i in wt.data['U-3']:
#     # print(i)

step_start = 0

#while 
