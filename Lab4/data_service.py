from pandas import *
def open(path):
    """Excel file opener

    Args:
        path (string): Path to excel file

    Returns:
        string: json output
    """
    xls = ExcelFile(path)
    df = xls.parse(xls.sheet_names[0])
    dict = df.to_dict()
    return dict
print (open('/Users/violetta/Desktop/ICS-485278/Lab4/data/db.xlsx'))