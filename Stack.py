import sqlite3
from collections import OrderedDict
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from numpy import *
filename='Excel_sheet.xlsx'
path="C:\\Users\\abhishek.vashisht\\Desktop\\Python_(Learning)\\"
excel=pd.read_excel(path + filename)
print(excel)
excel=excel.set_index(['loanid','unit'])
stacked=excel.stack()
dff=pd.DataFrame(stacked)
print(dff)
# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('New_Stacked.xlsx', engine='xlsxwriter')
# Write each dataframe to a different worksheet.
dff.to_excel(writer, sheet_name='Sheet1')
# Close the Pandas Excel writer and output the Excel file.
writer.save()


print(input('PRESS TO CLOSE'))

