import pytest
import json
import allure
from comm import ApiRequest
from comm.readexcel import OpenExcel
@pytest.mark.parametrize('data',OpenExcel().openYaml('apis','shangjia.yaml'))
def testrequest(data):
    url=data['url']
    method=data['method']
    data=data['data']
    r=ApiRequest.send_req().send_requests(method,url=url,data=data)
    assert r.status_code==200