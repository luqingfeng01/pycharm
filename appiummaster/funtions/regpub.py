# encoding: utf-8

'''
注册测试
'''
from appiummaster.untils.log import LOG,logger
from appiummaster.excetfuntion.exectfuntion import Makeappcase
import os
path=os.getcwd()
path_yongli=path+'\\data\\dingwei\\reg.yaml'
@logger('注册测试')
class RegFuntion:
    def __init__(self,deriver):
        self.deriver=deriver
        self.path=path_yongli
        self.open=Makeappcase(self.deriver,path=self.path)
    def reg(self,**kwargs):
        f=self.open.exce_case(**kwargs)
        if f['code']==1:
            LOG.info('无法获取断言')
            return
        else:
            beijing=f['data']
            return beijing