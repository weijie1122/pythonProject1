
import pytest
from comm.ApiRequest import send_request
from comm.readexcel import OpenExcel
from comm.readexcel import ExcelVarles

@pytest.mark.parametrize('data',OpenExcel().open_excelvalue('apis','add.xls',0))
def test_add(data):
    print(data)
    a=data[ExcelVarles().case_id]
    print(a)



