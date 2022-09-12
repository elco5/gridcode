import pandas as pd
import csv as csv
import numpy as np


excel_file = 'Grades.xlsx'
data = pd.read_excel(excel_file)

  

# with pd.ExcelWriter("ExcelWriter-result.xlsx") as writer:
#     data.to_excel(writer) 

print(data.columns[1])
print(data['Name'])