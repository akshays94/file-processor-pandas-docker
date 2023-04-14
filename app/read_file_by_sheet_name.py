import pandas as pd


def read_file_by_sheet_name(file_path, sheet_name):
    the_file = pd.read_excel(file_path, sheet_name=sheet_name)
    return the_file.to_dict('records')
