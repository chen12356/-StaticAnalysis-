import re


def extract_access_urls(urls: list):  # 插入源码第一个函数，对code_an_dic['urls']进行解析，获取可以访问的urls
    """
    提取可访问的url
    :param urls: 需处理的url数据
    :return: 格式['urls':[],'path':'']，urls可访问
    """
    url_list = []
    for url in urls:
        need_url = []
        for url_ in url['urls']:
            if url_.lower().startswith('http'):
                need_url.append(url_)
            elif url_.lower().startswith('www'):
                url_ = 'http://' + url_
                need_url.append(url_)
        if need_url:
            need_url = list(set(need_url))
            url_list.append({'urls': need_url, 'path': url['path']})
    return url_list


def extract_phone_card_passport(data: str):
    """
    提取 手机号、身份证号、护照号
    :param data:需要利用re提取的数据
    :return:{'phones:[],'cards':[],'passports':[]}返回一个Dict类型
    """
    pattern_phone = re.compile((r'^1[3-9]\d{9}$'), re.UNICODE)
    phones = [numbers for numbers in re.findall(r'\d+', data) if len(numbers) == 11 and pattern_phone.match(numbers)]
    pattern_card = re.compile(
        (r'(([1-6][1-9]|50)\d{4}(19|20)\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx])|'
         r'(([1-6][1-9]|50)\d{4}\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d+)'),
        re.UNICODE)
    cards = [card[0] if card[8] == '' else card[8] for card in re.findall(pattern_card, data)]
    pattern_passport = re.compile(
        (r'([EeKkGgDdSsPp]\d{8})|((([Ee][a-hjklmnp-zA-HJKLMNP-Z])|([DdSsPp][Ee])|([Kk][Jj])|([Mm][Aa]))\d{7})'),
        re.UNICODE)
    passports = [passport[1].upper() if passport[0] == '' else passport[0].upper() for passport in
                 pattern_passport.findall(data)]
    total = len(phones) + len(cards) + len(passports)
    if total != 0:
        return {'phones':phones,'cards':cards,'passports':passports}

def handle_urls_emails(datas: list):
    """
    处理url与email数据
    :param datas: datas可以是url/email的列表
    :return:返回样式 [{},{}] --> {'urls'/'emails':[{'phones':[],'cards':[],'passports':[],'url/email':'xx'}],'path':'',}
    """
    results = []
    for data in datas:
        data_dict, need_datas = {}, []
        try:
            key = 'urls' if data.get('urls') else 'emails'
            print(key)
            for tag in data[key]:
                print(tag)
                result = extract_phone_card_passport(tag)
                print(result)
                if result:
                    result[key.replace('s','')] = tag
                    need_datas.append(result)
                    # print(need_datas)
            if need_datas:
                data_dict[key] = need_datas
                data_dict['path'] = data['path']
                results.append(data_dict)
        except KeyError as e:
            print('遍历得到的data中缺少Key：%s' % e)
    return results