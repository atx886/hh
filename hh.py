import os
import notify
import requests
import ddddocr
from bs4 import BeautifulSoup
import time
import random

list_l = []


def shibie(img):
    ocr = ddddocr.DdddOcr()
    a = ocr.classification(img)
    return a


def 随机等待():
    t = random.randint(1, 3)
    print("等待" + str(t) + "秒")

    time.sleep(t)


# print(a)

session = requests.session()
url = 'https://lixianla.com/user-login.htm'
url1 = 'https://lixianla.com/vcode.htm'

h1 = {
    'Host': 'lixianla.com',
    'Connection': 'keep-alive',
    'Content-Length': '12',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Microsoft Edge";v="98"',
    'Accept': 'text/plain, */*; q=0.01',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56',
    'sec-ch-ua-platform': "Windows",
    'Origin': 'https://lixianla.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://lixianla.com/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
}
# Cookie: bbs_sid=n93p8jo1497f75ucjie6hhllm8; ezosuibasgeneris-1=b019b332-e678-4075-5c0b-e87afa947b2c; __gads=ID=ad702f9bb4b6295a-22153bc09ed0005c:T=1644839642:RT=1644839642:S=ALNI_MZ_7du4pvUoTQQ5lGnVxAHkbTQJrQ; __qca=P0-168962060-1644839680910; bbs_token=qWOmQIaUUtkgdLkpEKFCBjjaDg_2BX1mat8nFufta61HfSvZy1FEy2geVPGIM5YfzHKGRHlVJ4unhrt6MPPxXRJjX2QWc_3D; ezux_lpl_327928=1644935345869|946d7930-ebf1-43b1-6909-3c74ed493bc5|true


# Key: Host; Value: lixianla.com
# Key: Connection; Value: keep-alive
# Key: Content-Length; Value: 11
# Key: sec-ch-ua; Value: " Not A;Brand";v="99", "Chromium";v="98", "Microsoft Edge";v="98"
# Key: Accept; Value: text/plain, */*; q=0.01
# Key: Content-Type; Value: application/x-www-form-urlencoded; charset=UTF-8
# Key: X-Requested-With; Value: XMLHttpRequest
# Key: sec-ch-ua-mobile; Value: ?0
# Key: User-Agent; Value: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56
# Key: sec-ch-ua-platform; Value: "Windows"
# Key: Origin; Value: https://lixianla.com
# Key: Sec-Fetch-Site; Value: same-origin
# Key: Sec-Fetch-Mode; Value: cors
# Key: Sec-Fetch-Dest; Value: empty
# Key: Referer; Value: https://lixianla.com/
# Key: Accept-Encoding; Value: gzip, deflate, br
# Key: Accept-Language; Value: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
# Key: Cookie; Value: bbs_sid=n93p8jo1497f75ucjie6hhllm8; ezosuibasgeneris-1=b019b332-e678-4075-5c0b-e87afa947b2c; __gads=ID=ad702f9bb4b6295a-22153bc09ed0005c:T=1644839642:RT=1644839642:S=ALNI_MZ_7du4pvUoTQQ5lGnVxAHkbTQJrQ; __qca=P0-168962060-1644839680910; bbs_token=qWOmQIaUUtkgdLkpEKFCBjjaDg_2BX1mat8nFufta61HfSvZy1FEy2geVPGIM5YfzHKGRHlVJ4unhrt6MPPxXRJjX2QWc_3D; ezux_lpl_327928=1644935345869|946d7930-ebf1-43b1-6909-3c74ed493bc5|true
# header = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
#     'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Connection': 'keep-alive',
#
#     # 'Cookie': 'bbs_sid=pkac8069i99d47t04rtu23lsqh; __gads=ID=99891ebcb30ce90b-22ade08eb6d00043:T=1645538760:RT=1645538760:S=ALNI_MZ24FodZO-vFOqoK-0ptLx-zQ1-Mw; bbs_token=ugxem2qYU7xXRIZZUIrCbKbnT6KlN8_2Bo_2Btw94lMOggZKt9pTEn_2B2e6WGPef7okGYkJdYjAAEMI1B4Q_2B9r9qnsuyAZp8_3D; lx_cdn=4ae1ba38',
#     'Upgrade-Insecure-Requests': '1',
#     'Sec-Fetch-Dest': 'document',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-Site': 'same-origin',
#     # 'Sec-Fetch-User': '?1',
# }

k = ""
#
# h = {
#     'Content-Length': '12',
#     'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Microsoft Edge";v="98"',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Dest': 'empty',
#     'Sec-Fetch-Site': 'same-origin',
#     'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
#     'sec-ch-ua-platform': "Windows",
#     'Accept': 'text/plain, */*; q=0.01',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56',
#     # 'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
#     # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'
# }


res = ''

while k != "登录成功":
    x = 0

    r = session.get(url1)
    img = r.content
    res = shibie(img)
    print(res)

    data = {
        'email': "1932245379@qq.com",
        'password': "0e7e378cafe81fe8fb07987084608eb3",
        "vcode": res

    }
    r = session.post(url, data=data)
    # h = r.headers

    bs = BeautifulSoup(r.content, 'html.parser')
    a = bs.find(id='body').text.strip()
    k = a
    print(a)
#
r = session.get(url)
bs4 = BeautifulSoup(r.content, 'html.parser')

list = bs4.select('nav.nav:nth-child(6) > li:nth-child(2) > a:nth-child(1)')
urlt = ''
for i in list:
    urlt = i.get('data-modal-url')

# urlt = list
urlt = 'https://lixianla.com/' + urlt
print(urlt)
# os.close()

if k == "登录成功":
    随机等待()
    m = "签到失败，请稍后再重试！"
    while m == "签到失败，请稍后再重试！" or m == "验证码错误!!!":
        url4 = 'https://lixianla.com/vcode.htm'
        session.get(urlt)
        x = 0
        r = session.get(url4)
        # h = r.headers
        img = r.content
        res2 = shibie(img)
        print(res2)

        data1 = {
            "vcode": res2
        }
        随机等待()
        r = session.post(urlt, data=data1)
        bs = BeautifulSoup(r.content, 'html.parser')
        a = bs.find(id='body').text.strip()
        print(a)
        list_l.append(a)
        m = a
notify.send('签到', list_l)
