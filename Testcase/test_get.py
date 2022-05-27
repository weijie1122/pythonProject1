import pytest
import json
from comm import ApiRequest
from comm.readexcel import OpenExcel
@pytest.mark.parametrize('data',OpenExcel().openYaml('apis','data.yaml'))
def testrequest(data):
    url=data['url']
    method=data['method']
    params=data['data']
    r=ApiRequest.send_req().send_main(method,url=url,params=params)
    assert r.status_code==200












