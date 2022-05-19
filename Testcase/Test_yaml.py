import pytest
import os
from comm.ApiRequest import send_request
from comm.readexcel import OpenExcel
import allure
@pytest.mark.parametrize('data',OpenExcel().openYaml('apis','data.yaml'))
def test_yaml(data):
    url=data['url']
    method=data['method']
    params=data['params']
    print(url)
    req=send_request(url=url,method=method,params=params)
    assert req.status_code==200
if __name__=='__main__':
    pytest.main()










