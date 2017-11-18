import requests
import random
from lxml import etree
import sys


# login_url
index_url = 'http://home.51cto.com/index'
home_url = 'http://home.51cto.com/home'

ua_pool = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
]

headers = {'User-Agent': random.choice(ua_pool),
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9'}


def login(username, password):
    # 初始化一个链接，获取cookie
    client = requests.Session()
    resp = client.get(index_url, headers=headers)
    # 获取_csrf
    selector = etree.HTML(resp.text)
    csrf = selector.xpath('//*[@id="login-form"]/input[@name="_csrf"]/@value')[0]
    print(csrf)
    data = {'_csrf': csrf,
            'LoginForm[username]': username,
            'LoginForm[password]': password,
            'rememberMe': 0,
            'login-button': '登 录'}
    client.post(index_url, data=data, headers=headers)

    # 判断是否登陆成功
    resp_home = client.get(home_url)
    selector_home = etree.HTML(resp_home.text)
    nickname = selector_home.xpath('//div[@id="login_status"]/ul/li[1]/a[1]/text()')
    print(nickname)
    with open('D:/tmp/test6.html', 'wb') as f:
        f.write(resp_home.content)
        f.close()
    if nickname:
        return client
    else:
        return None


def postlog(client, title, htmlcontent, tags):
    addblog_url = 'http://blog.51cto.com/user_index.php?action=addblog_new'
    headers['Referer'] = home_url
    client.get(addblog_url, headers=headers)
    headers['Content-Type'] = 'multipart/form-data; boundary=----WebKitFormBoundaryXiouIq6AoO73YSj1'
    headers['Upgrade-Insecure-Requests'] = '1'
    headers['Origin'] = 'http://blog.51cto.com'
    data = '------WebKitFormBoundaryXiouIq6AoO73YSj1\r\n' \
           'Content-Disposition: form-data; name="isorg"\r\n' \
           '\r\n0\r\n' \
           '------WebKitFormBoundaryXiouIq6AoO73YSj1\r\n' \
           'Content-Disposition: form-data; name="atc_title"\r\n' \
           '\r\n' + title + '\r\n' \
           '------WebKitFormBoundaryXiouIq6AoO73YSj1' \
           '\r\nContent-Disposition: form-data; name="atc_content"\r\n' \
           '\r\n' +  htmlcontent + '\r\n' \
           '------WebKitFormBoundaryXiouIq6AoO73YSj1\r\n' \
           'Content-Disposition: form-data; name="tags"\r\n' \
           '\r\n' + tags + '\r\n' \
           '------WebKitFormBoundaryXiouIq6AoO73YSj1\r\n' \
           'Content-Disposition: form-data; name="Input22"\r\n' \
           '\r\n\r\n' \
           '------WebKitFormBoundaryXiouIq6AoO73YSj1\r\n' \
           'Content-Disposition: form-data; name="Input223"\r\n' \
           '\r\n\r\n' \
           '------WebKitFormBoundaryXiouIq6AoO73YSj1\r\n' \
           'Content-Disposition: form-data; name="Input22"\r\n' \
           '\r\n\r\n' \
           '------WebKitFormBoundaryXiouIq6AoO73YSj1\r\n' \
           'Content-Disposition: form-data; name="Input223"\r\n' \
           '\r\n\r\n' \
           '------WebKitFormBoundaryXiouIq6AoO73YSj1\r\n' \
           'Content-Disposition: form-data; name="Input22"\r\n' \
           '\r\n\r\n' \
           '------WebKitFormBoundaryXiouIq6AoO73YSj1\r\n' \
           'Content-Disposition: form-data; name="Input223"\r\n' \
           '\r\n\r\n' \
           '------WebKitFormBoundaryXiouIq6AoO73YSj1\r\n' \
           'Content-Disposition: form-data; name="classname"\r\n' \
           '\r\nLinux\r\n------WebKitFormBoundaryXiouIq6AoO73YSj1\r\n' \
           'Content-Disposition: form-data; name="sub_class"\r\n' \
           '\r\n\r\n' \
           '------WebKitFormBoundaryXiouIq6AoO73YSj1\r\n' \
           'Content-Disposition: form-data; name="dirid"\r\n' \
           '\r\n0\r\n' \
           '------WebKitFormBoundaryXiouIq6AoO73YSj1\r\n' \
           'Content-Disposition: form-data; name="copy"\r\n' \
           '\r\n0\r\n' \
           '------WebKitFormBoundaryXiouIq6AoO73YSj1\r\n' \
           'Content-Disposition: form-data; name="ishide"\r\n' \
           '\r\n0\r\n' \
           '------WebKitFormBoundaryXiouIq6AoO73YSj1\r\n' \
           'Content-Disposition: form-data; name="atc_info"\r\n' \
           '\r\n\r\n' \
           '------WebKitFormBoundaryXiouIq6AoO73YSj1\r\n' \
           'Content-Disposition: form-data; name="plc"\r\n' \
           '\r\n0\r\n' \
           '------WebKitFormBoundaryXiouIq6AoO73YSj1\r\n' \
           'Content-Disposition: form-data; name="drf_id"\r\n' \
           '\r\n\r\n' \
           '------WebKitFormBoundaryXiouIq6AoO73YSj1\r\n' \
           'Content-Disposition: form-data; name="step"\r\n' \
           '\r\n2\r\n' \
           '------WebKitFormBoundaryXiouIq6AoO73YSj1\r\n' \
           'Content-Disposition: form-data; name="job"\r\n' \
           '\r\nadd\r\n' \
           '------WebKitFormBoundaryXiouIq6AoO73YSj1\r\n' \
           'Content-Disposition: form-data; name="pusher"\r\n' \
           '\r\n\r\n' \
           '------WebKitFormBoundaryXiouIq6AoO73YSj1\r\n' \
           'Content-Disposition: form-data; name="uploadplus"\r\n' \
           '\r\n\r\n' \
           '------WebKitFormBoundaryXiouIq6AoO73YSj1\r\n' \
           'Content-Disposition: form-data; name="cidpre"\r\n' \
           '\r\n\r\n' \
           '------WebKitFormBoundaryXiouIq6AoO73YSj1\r\n' \
           'Content-Disposition: form-data; name="tid"\r\n\
           \r\n\r\n' \
           '------WebKitFormBoundaryXiouIq6AoO73YSj1--'
    resp_post = client.post(addblog_url, data=data, headers=headers)
    selector = etree.HTML(resp_post.text)
    article_url = selector.xpath('//a[@class="btn" and @target="_blank"]/@href')
    if article_url:
        return article_url[0]
    else:
        return None






