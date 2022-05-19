import pandas as pd
def read_excel(file, **kwargs):
    data_dict = []
    try:
        data = pd.read_excel(file, **kwargs)
        data_dict = data.to_dict('records')
    finally:
        return data_dict


a=read_excel('../apis/add.xls')
b=read_excel('../apis/add.xls', sheet_name='Sheet1')
print(a)
print(b)