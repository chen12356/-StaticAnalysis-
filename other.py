# extract_url('http://dsds18327384719/ds=352210991208294$==352230199604021817?=352223930213123')
import re

str1 = 'rr-8618337158713X---86183372587108992--ere1515058678228-008618337154338-00851722-00+8618633232222-'
t = re.findall(r'((1|\+861|00861)[3-9]\d{9})', str1)
pattern_phone = re.compile(r'((1|0086|\+861)\d+)', re.UNICODE)
phones_ = [phone[0] for phone in re.findall(pattern_phone, str1) if
           (phone[0].startswith('1') and len(phone[0]) == 11) or ('86' in phone[0] and len(phone[0]) in [14, 15])]
print(phones_)

p1 = [numbers for numbers in re.findall(r'\d+', str1) if len(numbers) == 11 and re.match(r'^1[3-9]\d{9}$', numbers)]
pattern_phone = re.compile((r'^(1|\+86|86)[3-9]\d{9}$'), re.UNICODE)
phones = [numbers for numbers in re.findall(r'\d+|\+86\d+', str1) if
          len(numbers) in [11, 14] and pattern_phone.match(numbers)]
print('youle :%s' % phones)

c = '322230199604021817-==-323=35223019960802181X--3522301996040218172385885-156327827431'
pattern_card = re.compile((r'([1-9]\d{5}(19|20)\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx])')
                            , re.UNICODE)

print(pattern_card.findall(c))
pattern_card_18 = re.compile(
            (r'(([1-6][1-9]|50)\d{4}(19|20)\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx])'),
            re.UNICODE)
pattern_card_15 = re.compile((
            r'(([1-6][1-9]|50)\d{4}\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d+)'
        ),re.UNICODE)
print(pattern_card_18.findall(c))
print('xxxxxxxxxxxxxxxxxxxxxxxxxx')
for x in pattern_card_15.findall(c):
    print(len(x[0]))
card_15 = [ c_15[0] for c_15 in pattern_card_15.findall(c) if len(c_15[0])==15 ]
print(card_15)

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
                'cards': ['352230199008101728'],
                'passports': ['E43123178'],
                'gps_lng_lat': [],
                'url': 'https://20.com'
            },
            {
                'phones': ['13172636233'],
                'cards': ['15042700050885'],
                'passports': [],
                'gps_lng_lat': [('22', '122')],
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
                'gps_lng_lat': [],
                'url': 'https://2.com'
            }
        ],
        'path': 'xxxxx222'
    },
    {'urls':
        [
            {
                'phones': ['2'],
                'cards': ['1123123112312313'],
                'passports': [],
                'gps_lng_lat': [],
                'url': 'https://2.com'
            }
        ],
        'path': 'xxxxx111'
    },{'urls':
        [
            {
                'phones': ['2'],
                'cards': ['1123123112312313'],
                'passports': [],
                'gps_lng_lat': [],
                'url': 'https://re正则.com'
            }
        ],
        'path': 'xxxxx123456789'
    }
]
ap_result = [{
    'phones': ['231'],
    'cards': ['15042700050886'],
    'passports': ['E13298293'],
    'gps_lng_lat': [("3", "43")],
    'url': 'https://201.com',
    'response': 'xsxsx33333--201',
    'path':'xxxxx111'
}, {
    'phones': [],
    'cards': ['15042700050886'],
    'passports': ['E13298293'],
    'gps_lng_lat': [],
    'url': 'https://201504270005088731.hybrid.alipay-eco.com',
    'response': 'xsxsxssxsxsxs',
'path':'dsdsdsd1234'
}, {
    'phones': ['两个都有'],
    'cards': ['15042700050886+123'],
    'passports': ['E13298293'],
    'gps_lng_lat': [],
    'url': 'https://2.com',
    'response': 'xsxsxssxsxsxs',
'path':'dsdsdsd123'
},{
    'phones': [],
    'cards': ['15042700050886+123'],
    'passports': ['E13298293'],
    'gps_lng_lat': [],
    'url': 'https://怎么说.com',
    'response': 'xsxsxssxsxsxs',
'path':'dsdsdsd123'
}
]

first_length = len(first_result)
print(first_length)
ap_len = len(ap_result)
print(ap_len)
for i in range(first_length):

    for dic in first_result[i]['urls']:
        for ar in ap_result:
            if ar['url'] == dic['url']:  #如何存在
                dic['phones'].extend(ar['phones'])
                dic['cards'].extend(ar['cards'])
                dic['passports'].extend(ar['passports'])
                dic['gps_lng_lat'].extend(ar['gps_lng_lat'])
            elif not dic.get('response', None):
                dic['response'] = ''


print(first_result)
#判断url是不是一样的，是一样的组装新字典数据，不考虑重复情况


def assemble_data(first_result,resp_result):
    for i in range(len(first_result)):
        for dic in first_result[i]['urls']:
            for ar in ap_result:
                if ar['url'] == dic['url']:
                    # dic['phones'] = {'u_p': dic['phones'], 'r_p': ar['phones']}
                    # dic['cards'] = {'u_c': dic['cards'], 'r_p': ar['cards']}
                    # dic['passports'] = {'u_pp': dic['passports'], 'r_pp': ar['passports']}
                    # dic['gps_lng_lat'] = {'u_g': dic['gps_lng_lat'], 'r_g': ar['gps_lng_lat']}
                    # dic['response'] = ar['response']

                    # data['u_c'] = dic['cards']
                    # data['resp_c'] = ar['cards']
                    # data['u_pp'] = dic['passport']
                    # data['resp_pp'] = ar['passport']
                    # data['u_gps'] = dic['gps_lng_lat']
                    # data['resp_gps'] = dic['gps_lng_lat']
                    dic['phones'].extend(ar['phones'])
                    dic['cards'].extend(ar['cards'])
                    dic['passports'].extend(ar['passports'])
                    dic['gps_lng_lat'].extend(ar['gps_lng_lat'])
                elif not dic.get('response', None):
                    dic['response'] = ''




# 合并的结果如下:result
result = [{'urls': [
    {'phones': [], 'cards': ['1'], 'passports': [], 'gps_lng_lat': [], 'url': 'https://20.com', 'response': ''},
    {'phones': ['13172636233', '231'], 'cards': ['15042700050885', '15042700050886'], 'passports': ['E13298293'],
     'gps_lng_lat': [('22', '122'), (3, 43)], 'url': 'https://201.com', 'response': 'xsxsx33333--201'}],
           'path': 'xxxxx333'}, {'urls': [
    {'phones': [], 'cards': ['15042700050885'], 'passports': [], 'gps_lng_lat': [],
     'url': 'https://201504272200050887.hybrid.alipay-eco.com', 'response': ''}], 'path': 'xxxxx222'}, {'urls': [
    {'phones': ['2', '1231212'], 'cards': ['1123123112312313', '15042700050886+123'], 'passports': ['E13298293'],
     'gps_lng_lat': [], 'url': 'https://2.com', 'response': 'xsxsxssxsxsxs'}], 'path': 'xxxxx111'}]

# for dic in dict2:
#     for d, v in dic.items():
#         print(d, v)
#         if d in dict1.keys():
#             if isinstance(dict2[d], list):
#                 dict2[d].extend(dict1[d])
#         else:
#             print('没有')
# print(dict2)


#GPＳ信息(经纬度信息)
s = 'http://tyu089.2311ew134.2390132e-32.04-3.43842'
pattern_gps_lng = re.compile(
    (r'((\+)?(((\d|[1-9]\d|1[0-7]\d|0{1,3})\.\d{0,7})|(\d|[1-9]\d|1[0-7]\d|0{1,3})|180\.0{0,7}|180))'), re.UNICODE
)
pattern_gps_lat = re.compile(
    # (r'((\+)?[0-8]?\d{1}\.\d{0,7}|90\.0{0,7}|[0-8]?\d{1}|90)'),
    (r'((\+)?[0-8]?\d{1}\.\d{0,7}|90\.0{0,7}|[0-8]?\d{1}|90)'),
    re.UNICODE
)
lng = [lg[0]  for lg in pattern_gps_lng.findall(s) if '.' in lg[0] and (73.000000<float(lg[0])<135.000000) and (len(lg[0])>7)]  # 经度 lng
print(lng)
lat = [la[0] for la in pattern_gps_lat.findall(s) if '.' in la[0] and (4.000000<float(la[0])<53.560000) and (len(la[0])>7)]  # 经度 lat
print(lat)
# 上面简化
new = [(i, c) for i in lng for c in lat]
print(new)
# print(new)
