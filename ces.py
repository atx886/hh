import time
import requests
import re
import json
import random
import notify

ls = []


def dl(ph):
    base_url = 'https://ri09fjiomkvfrefcvc98s.spzhuisu.com'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data1 = {
        'username': ph,
        'password': ph}
    sess = requests.session()
    response = sess.post(base_url, headers=headers)
    data = response.text
    # r = requests.get(data)
    print(data)
    # print(r.content())
    url1 = 'https://ri09fjiomkvfrefcvc98s.spzhuisu.com/index/login/login.html?token='
    url2 = "https://ri09fjiomkvfrefcvc98s.spzhuisu.com/index/index/jf_dk.html?token="
    s1 = re.compile('token=(.+)\'')
    te = s1.findall(data)
    print(te[0])
    dl1 = sess.post(url1 + te[0], headers=headers, data=data1)
    print(dl1.text)
    s = sess.post(url=url2 + te[0], headers=headers).json()
    print(s)
    t = s['msg']
    print(t)
    return t
    # return t == '打开成功'


# dl('17017916658')
# notify.send('签到',

# file = open('1.txt', 'r')
# cont = file.read()
# print(cont)
# print(cont[0])

start = time.time()
with open('1.txt', 'r', encoding='utf-8') as f:
    cont = f.readlines()
    print(cont)
    print('a')
    f.close()
num = []
for c in cont:
    num.append(c.strip())
print(num)

ydk = 0
dkcg = 0
shibai = 0
for n in num:
    jg = dl(n)
    time.sleep(random.random() + random.randint(0, 3))
    if jg == '你今天已经打过卡了':
        ydk += 1
    elif jg == '打卡成功':
        dkcg += 1
    else:
        shibai += 1

end = time.time()
runTime = end - start
shijian = "耗时:{:.2f}秒".format(runTime)
print(shijian)
ls.append(shijian)
ydks = "今日已经打卡" + str(ydk) + "个"
dkcgs = "成功打卡" + str(dkcg) + "个"
shibais = "失败" + str(shibai) + "个"
ls.append(ydks)
ls.append(dkcgs)
ls.append(shibais)
notify.send('qd', ls)
