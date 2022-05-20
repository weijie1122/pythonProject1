import allure
import pytest
from comm.readexcel import OpenExcel
from comm.readexcel import ExcelVarles

@pytest.mark.parametrize('data',OpenExcel().open_excelvalue('apis','add.xls',0))
def testadd(data):
    print(data)
    a=data[ExcelVarles().case_id]
    assert a==40



