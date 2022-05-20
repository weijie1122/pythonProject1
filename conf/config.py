import os
from configparser import ConfigParser
_conf_dir = os.path.dirname(__file__)
_conf_file = os.path.join(_conf_dir, 'config.ini')
class myparser(ConfigParser):
    def as_dict(self):
        d=dict(self._sections)
        for k in d :
            d[k]=dict(d[k])
        return d
def _get_all_conf():
    _config=myparser()
    result={}
    if os.path.isfile(_conf_file):
        try:
            _config.read(_conf_file,encoding='UTF-8')
            result=_config.as_dict()
        except OSError :
            raise ValueError('读取文件错误: %s' %OSError)
    return result

c=_get_all_conf()
s=c['sys']
sql=c['smtp']
log=c['log']
email=c['email']


