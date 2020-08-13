# extract_url('http://dsds18327384719/ds=352210991208294$==352230199604021817?=352223930213123')
import re

str1 = '18337158710---12345678902--15150578228-18337158---'

p1 = [numbers for numbers in re.findall(r'\d+', str1) if len(numbers) == 11 and re.match(r'^1[3-9]\d{9}$', numbers)]
pattern_phone = re.compile((r'^1[3-9]\d{9}$'), re.UNICODE)
phones = [numbers for numbers in re.findall(r'\d+', str1) if len(numbers) == 11 and pattern_phone.match(numbers)]
print('youle :%s' % phones)

c = '322230199604021817-==-323=35223019960802181X--3522301996040218172385885-'
pattern_card18 = re.compile((r'([1-9]\d{5}(19|20)\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx])')
                            , re.UNICODE)

#
# cards = [ card for card in re.findall(r'\d{17}[0-9Xx]*',c)]


# 护照号
h_s = 'EO9485958---e90090090'
pattern_passport = re.compile(
    (r'([EeKkGgDdSsPp]\d{8})|((([Ee][a-hjklmnp-zA-HJKLMNP-Z])|([DdSsPp][Ee])|([Kk][Jj])|([Mm][Aa]))\d{7})'), re.UNICODE)
passports = [passport[1].upper() if passport[0] == '' else passport[0].upper() for passport in
             pattern_passport.findall(h_s)]

print(passports)
# print(cards)


h = ['https://api.weibo.cn/2/sdk/login', 'http://api.weibo.cn/2/sdk/login',
     'https://api.weibo.com/2/proxy/sdk/statistic.json', 'https://service.weibo.com/share/mobilesdk_uppic.php',
     'https://service.weibo.com/share/mobilesdk.php', 'https://open.weibo.cn/oauth2/authorize?',
     'https://api.weibo.com/oauth2/access_token',
     'https://paygate-yf.meituan.com/paygate/notify/alipay/paynotify/simple',
     'https://render.alipay.com/p/s/errorpage/?', 'https://render.alipay.com/p/s/h5misc/resource_error?url=']

# import requests
# import time
# start = time.time()
# for url in h:
#     r = requests.get(url)
#     if r.status_code == 200:
#         print(r.text)
# end = time.time()
#
# print(end-start)


li = [1]
if not len(li):
    print(1)

first_result = [
    {'urls':
        [
            {
                'phones': [],
                'cards': ['1'],
                'passports': [],
                'url': 'https://20.com'
            },
            {
                'phones': ['13172636233'],
                'cards': ['15042700050885'],
                'passports': [],
                'url': 'https://201.com'
            }
        ],
        'path': 'xxxxx333'
    },
    {'urls':
        [
            {
                'phones': [],
                'cards': ['15042700050885'],
                'passports': [],
                'url': 'https://201504272200050887.hybrid.alipay-eco.com'
            }
        ],
        'path': 'xxxxx222'
    },
    {'urls':
        [
            {
                'phones': [],
                'cards': ['1123123112312313'],
                'passports': [],
                'url': 'https://2.com'
            }
        ],
        'path': 'xxxxx111'
    },
]
ap_result = [{
    'phones': ['tete'],
    'cards': ['15042700050886'],
    'passports': ['E13298293'],
    'url': 'https://201.com',
    'response': 'xsxsx33333--201'
}, {
    'phones': [],
    'cards': ['15042700050886'],
    'passports': ['E13298293'],
    'url': 'https://201504270005088731.hybrid.alipay-eco.com',
    'response': 'xsxsxssxsxsxs'
}, {
    'phones': ['1231212'],
    'cards': ['15042700050886+123'],
    'passports': ['E13298293'],
    'url': 'https://2.com',
    'response': 'xsxsxssxsxsxs'
}]

first_length = len(first_result)
print(first_length)
ap_len = len(ap_result)
print(ap_len)
for i in range(first_length):
    for dic in first_result[i]['urls']:
        for ar in ap_result:
            if ar['url'] == dic['url']:
                dic['phones'].extend(ar['phones'])
                dic['cards'].extend(ar['cards'])
                dic['passports'].extend(ar['passports'])
                dic['response'] = ar['response']
            elif not dic.get('response',None):
                dic['response'] = ''
print(first_result)

a = [
    {'urls': [
        {'phones': [], 'cards': ['15042700050885'], 'passports': [],
                'url': 'https://20150427000508ds81117.hybrid.alipay-eco.com'},
        {'phones': ['13172636233'], 'cards': ['15042700050885'], 'passports': [],
                'url': 'https://201.hybrid.alipay-eco.com'}],
    'path': 'xxxxx333'
    },
    {'urls': [
        {'phones': [], 'cards': ['15042700050885'], 'passports': [],
        'url': 'https://201504272200050887.hybrid.alipay-eco.com'}],
        'path': 'xxxxx222'
    },
    {'urls': [
    {'phones': ['1231212'], 'cards': ['1123123112312313', '15042700050886+123'], 'passports': ['E13298293'],
     'url': 'https://2.com', 'response': 'xsxsxssxsxsxs'}],
        'path': 'xxxxx111'
    }
]

# for dic in dict2:
#     for d, v in dic.items():
#         print(d, v)
#         if d in dict1.keys():
#             if isinstance(dict2[d], list):
#                 dict2[d].extend(dict1[d])
#         else:
#             print('没有')
# print(dict2)
