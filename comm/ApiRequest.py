import requests
class send_req:
    def send_requests(self,method,url,data=None,params=None,headers=None,cookies=None,json=None,files=None,timeout=10):
        self.r=requests.request(method,url,data=data,params=params,headers=headers,cookies=cookies,json=json,files=files,timeout=timeout)
        return self.r

