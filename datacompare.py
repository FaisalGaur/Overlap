import pandas as pd
import numpy as np
from functools import reduce

DateWise = pd.read_excel('WYNBRANDS.xls', sheet_name='DateWise')
Ledger = pd.read_excel('WYNBRANDS.xls', sheet_name='Ledger')
Warehouse = pd.read_excel('WYNBRANDS.xls', sheet_name='Stock_Avail_By_Warehouse')

final_df = [DateWise, Ledger, Warehouse]

Results = reduce(lambda left, right: pd.merge(left, right, on='Product ID', how='outer'), final_df)

Results['Match'] = np.where(((Results['Qty Datewise'] == Results['Qty Ledger']) &
                            (Results['Qty Datewise'] == Results['Qty Warehouse']) &
                            (Results['Qty Ledger'] == Results['Qty Warehouse'])), 'True', 'False')
Results.to_csv("Results.csv", sep=',')

