#计算函数执行时间

import time

def wrapper(func):
    def inner(*args,**kwargs):
        """函数执行之前的操作"""
        start_time=time.time()
        res=func(*args,**kwargs)
        dur=time.time()-start_time
        print('函数名:%s' %func)
        print("该函数的执行时间：%s" %dur)
        """函数执行后执行的操作"""
        return res
    return inner
