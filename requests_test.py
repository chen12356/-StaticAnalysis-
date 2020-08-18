import requests

u = ['https://h5.m.taobao.com/','https://detail.m.tmall.com/item.htm',
     'http://detail.tmall.com/item','http://agoodm.m.taobao.com/agoo/report',
     'http://aps.testing.amap.com/collection/collectData?src=baseCol&ver=v74',
     'https://accountlink.taobao.com/confirmUnbind.htm',
     'https://e.189.cn/sdk/agreement/detail.do?appKey=E_189&hidetop=true&returnUrl=',
     'https://d.alipay.com/mbresultyy/prc.htm',
     'https://nbsdk-baichuan.alicdn.com/2.0.0/applink.htm?plat=android&appKey=%s','http://agoodm.m.taobao.com/agoo/report']

for i in u:
    res = requests.get(i)
    print('++++++++++++++++++++++++++++')
    print(res.status_code,i)