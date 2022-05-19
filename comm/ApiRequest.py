import requests
def send_request(url,method,data=None,params=None,hearder=None):
    return requests.request(url=url,method=method,data=data,params=params,headers=hearder)
url='http://192.168.1.205:8000/api/moto/car/series/getSeriesById'
method='get'
params={'seriesId':395}
req=requests.request(url=url,method=method,params=params)
print(req.text)