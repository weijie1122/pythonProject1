import requests
class send_req:
    '''
    def send_requests(self,method,url,data=None,params=None,headers=None,cookies=None,json=None,files=None,timeout=10):
        self.r=requests.request(method,url,data=data,params=params,headers=headers,cookies=cookies,json=json,files=files,timeout=timeout)
        return self.r
        '''
    def send_post(self,url,data=None,**kwargs):
        r=requests.post(url=url,data=data,**kwargs)
        return r
    def send_get(self,url,params=None,**kwargs):
        r=requests.get(url=url,params=params,**kwargs)
        return r
    def send_main(self,method,url,data=None,params=None,**kwargs):
        if method=='post':
            req=self.send_post(url=url,data=data,**kwargs)
            return req
        elif method=='get':
            req=self.send_get(url=url,params=params,**kwargs)
            return req

