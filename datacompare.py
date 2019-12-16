import pandas as pd
from functools import reduce


def all_same(items):
    return all(x == items[0] for x in items)


def read_data(filename, sheet):
    data_frame = pd.read_excel(filename, sheet_name=sheet)
    return data_frame


def calculate_results(final_frame, common_field, result_field):
    result = reduce(lambda left, right: pd.merge(left, right, on=common_field, how='outer'), final_frame)
    result[result_field] = (result.iloc[:, 1:].eq(result.iloc[:, 1], axis=0)).all(1)
    return result


if __name__ == '__main__':
    DateWise = read_data('WYNBRANDS.xls', 'DateWise')
    Ledger = read_data('WYNBRANDS.xls', 'Ledger')
    Warehouse = read_data('WYNBRANDS.xls', 'Stock_Avail_By_Warehouse')
    final_df = [DateWise, Ledger, Warehouse]
    Results = calculate_results(final_df, 'Product ID', 'Match Result')
    Results.to_csv("Results.csv", sep=',')


