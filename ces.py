import time
import requests
import re
import json
import random
# import os
import notify
from requests.adapters import HTTPAdapter

k = 0
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
    time.sleep(1)
    data = response.text
    # r = requests.get(data)
    # print(data)
    # print(r.content())
    url1 = 'https://ri09fjiomkvfrefcvc98s.spzhuisu.com/index/login/login.html?token='
    url2 = "https://ri09fjiomkvfrefcvc98s.spzhuisu.com/index/index/jf_dk.html?token="
    s1 = re.compile('token=(.+)\'')
    te = s1.findall(data)
    print(te[0])
    dl1 = sess.post(url1 + te[0], headers=headers, data=data1)
    print(dl1.text)
    time.sleep(1)
    s = sess.post(url=url2 + te[0], headers=headers).json()
    # print(s)
    t = s['msg']
    print(t)
    print(ph)
    # sess.close()
    return t
    # return t == '打开成功'


# dl('17017916658')
# notify.send('签到',

# file = open('1.txt', 'r')
# cont = file.read()
# print(cont)
# print(cont[0])

txx = """17016303166
17017916658
17024465648
13635131423
15823222088
15524973396
18252599609
13788578566
13991235630
15676374414
13581267955
13807734498
13059752282
18268967786
18876596734
17758504815
17542126271
13387731997
13687742445
15078379920
13978378809
13978366143
13977382287
15277366963
15185772160
13707734071
16698122781
13319068078
18177382185
18551706928
15008993271
13182990578
18290067776
15209057363
18855129172
13679974735
13204218839
18999787371
13109973772
13364860882
18690315228
19768534691
18899998888
18878322945
16772431002
18377332663
17777371078
15677329978
18377389198
19167630872
18178315758
18878395957
19167630872
17014541765
17050822672
17000650766
17140941200
17026708043
16238822630
17050999813
17016303512
17000654207
17016304658
17000652147
17140940875
16223734012
17020834653
16785371339
16785370776
17000655184
17171261565
16274745949
17040670785
16223738754
15874182074
17000655206
17041518145
16261656278
17017932410
16238822506
16785370695
17016304138
17140945763
17090648860
17171262021
17016304133
16785371361
16740445025
17024464392
17026963728
16223739395
17171261410
17140946763
16785981410
17000652848
16212917882
17171261547
17000652969
17050589608
17026708136
16223735966
16785371331
16756020575
17017932508
17026709124
16785511714
16212911631
16220710647
17000653700
17016303166
17017916658
17024465648
16273445450
17024465520
17000652438
17000650369
16756608611
17016303325
17171261670
16223735896
16785370325
17000651850
17140941033
17014541647
16238822397
17000653326
17000653224
17000651568
17167856960
17140941075
16785370591
17050545608
17000650543
17143467187
16785371081
17069624066
16756020612
17016304809
17000652790
16220710317
17016304207
17016303433
16223737486
16223732056
17016304762
17000653705
17016304262
17000654147
17016304363
17041516095
17040670806
17050580493
16522190930
17000650782
18721440254
17140941260
16740445053
17000654465
16521635466
16238822698
17014541659
18721491806
18640816212
13641797504
16571182183
17140940991
17000655027
17166764490
16522194944
16219420538
17000651091
16536225024
16785371073
16274742974
16536227106
16223736363
16212948481
16785371307
17016303418
16571153054
16212949527
17024078629
17050540195
17050589726
17024077169
17028070356
17050540322
17017044624
17050588482
17054269502
17038343227
17017038310
17050998986
17017041624
17050588514
17017036196
17017918959
17023307623
17050589231
17026846921
17017024504
17017043145
17038391007
17024078579
17038391355
17017021150
17050589007
17017036157
17019468560
17017910903
17026846720
17023309554
17026846113
17010682124
17028070169
17017594996
17028014604
17024074884
17092332340
17090641335
17018404361
17084436953
17090641064
17017932698
17019959968
17024075294
17017038395
17017034385
17024071696
17017043092
17017036561
17017038227
18721431062
13641794464
17555003191
13095508970
15665502970
17050549213
17050588973
17050545561
17040278449
17017043084
17090648571
17028070408
17026846982
17024074409
17050540521
17024073321
17017910701
17017034335
17024074396
17050999896
17028070051
17023309623
17090641809
17017044712
17017912732
17028013264
17017047421
17017036198
17017022503
17024075261
17050548967
17050588930
17017912487
17019468584
17024073067
17017039382
17017038171
17026848332
17021344063
17050588646
17092331702
17050588662
17017919132
17050588559
17017049413
17026848774
17050548804
17017912464
17038391622
17038392077
17024076049
17050585754
17024078045
17092332237
16756681780
16261656283
16259504158
16571303534
16237904306
16220710574
16522199853
17050549324
16521234348
16571304155
16536765735
16259508463
17138524496
16571133502
16237900409
17024075145
16536227375
16536766169
16521630609
17138524503
16536895635
16227211036
16228346934
16259506409
16756340073
16259506517
17145236189
16222653531
16227211148
16756340586
16536766117
16532473587
17010012914
16521985521
16259508478
16232404653
16259502932
16211721839
17050548922
16259506103
16259504708
17040275013
17050999781
16756071767
16263386853
16210747838
16259504495
16536730187
17024078580
16254432630
16211721820
16522196200
16259508192
16232403989
17024074872
16259504381
16227211422
16263386736
16232407823
16232405612
17084436751
16571133323
17144317993
17017918813
16259509365
16536895563
16237900452
17019415774
16210991390
17024076582
16232401856
17050545571
16222651506
17025594903
16232403910
16210993155
16238822391
16798260374
16536736346
16259509416
16237904086
16259504873
16211956030
16756340010
16731809699
16521620210
16756020161
16756340686
17040278590
16211721668
17108391286
17108390662
16232404742
16571116016
16764763341
17019416468
16211956008
17136265347
16571716230
16228347059
16228348576
17092647813
16536799062
17092648996
16211957500
17144346187
16220710425
17010010582
17116494889
16250451395
17025594659
17092646531
17017919339
16232406282
16536229371
16571115963
17108391581
16537630560
17138524413
16743142074
17108391290
16227211015
17144318025
17138524506
16232406061
16227211564
16536797359
17050545894
16227210892
16756072302
16756612976
16571133450
16259503078
16536582214
17025821232
16259503190
16211722187
17025820264
16210744943
16211952767
16237904268
16571714780
16536612639
17050588780
16250451384
16521426311
16232404546
16259504351
16571115691
16232403712
16250451469
16731807038
16571765487
16571189314
16222651509
16571303276
16756020705
16238822450
16210994654
16536895906
16536895362
16521420913
16571185273
16521593311
17145236827
16536220451
16254432601
16536895767
17010011432
16259504801
17010011674
16238820955
16232406321
16259504795
16536797602
16536895191
16756681760
16210745028
17144346297
16536895297
16227212120
16259507039
16756340325
16756340693
16227210991
17017911036
16228204941
16210993049
16259504609
16270202598
16538587509
16259506032
16210745106
16254437312
16210744954
16259506394
17025598335
16259503457
16259503463
16756071952
16756681930
16232406261
16521425122
17112487504
16731809599
16259503270
16521426800
16259503159
16259504383
16756613092
17017918751
16764764209
16731806258
16740445080
16756305682
16536732458
16222651606
16764764110
16537630230
16536730238
16536226915
16521620233
16254431395
17144318580
16536894119
16227211589
16259508691
16237904047
16521988917
17025826806
17144346317
16536765393
17050990781
17040275032
16571304029
16210745051
16571184069
16756340667
17108391180
17108390464
16227211141
16731809322
16222653537
16259507313
16536730200
17144318019
17050540722
16743142079
16254432612
16232408247
16259503167
17013710029
16521626321
17144317965
16521630908
16756340267
17050549451
17090646324
16250451370
16521429288
16756681780
16536610105
16536893496
16536736494
17040278104
16227212024
16731806858
16210747745
16521596622
17092643245
16536582349
16211721679
16536227570
16756892756
16756102902
17028258431
16536227256
16764764213
17025594890
17040274465
17029097742
16785651046
16764764240
16211957746
16536894014
16571133274
17019414429
16536799275
17025597071
16537633246
17025595995
16536580450
17025825495
16571182001
16536733165
17017919395
17025598319
16237719581
17025595919
16210743757
16227210442
16731807578
16571303186
16537636491
17108391691
16756713606
16536227990
16536582554
16571184467
17025824940
16536226603
16756072565
17070943987
16210745219
17108391231
17025594831
17025826103
17092648110
17144346593
17127960511
16756072103
16785884227
17087131755
17025821973
16536735496
16756340536
16536227214
16571301896
17024569632
16536227561
16536737554
16210769709
16521918813
17025597214
16536894525
17144318701
16222653484
16211729508
17092643740
16571133592
16536737440
16571304122
16537630503
16537635324
16571183716
17019416904
17021346486
17017910590
17138524527
17024074513
17040278461
17025822717
17025596963
17021341794
15659050371
16222652437
16222652251
17025597161
17144346337
17025594806
17019413629
17144293556
16756072337
17050998807
16222652392
16222653615
16259508587
17144346755
16210994783
17084431175
16536735374
17108391737
17028257184
16222652473
16756103181
16522059338
16756713753
17064651068
16227210963
16257129254
18659938604
17020125014
16756681989
16571303771
16222651352
16238822645
16238822653
17140946882
16259508257
17019414389
16764763243
16536637717
16259503160
16537639394
16259508272
16536895352
16536735062
17050582335
17019415429
16259509468
17144317910
17050545790
17019415417
17140946862
16537630120
16536766007
16259503380
16731807518
16521621201
16227211521
16211956017
17144346382
16536226510
16228348573
16250451399
16571181549
16521622765
16756072021
17118625157
16571116590
16522190538
17166763964
16211722289
17025827429
16210745290
16756090776
17108390463
16210745084
16211956126
16259503209
16537630325
17025594798
16211721802
17108391662
17084437332
16536896067
17025826865
16536895752
16232408646
16232408587
16536895131
16259507476
16756340159
17138524467
16210745018
16537630573
16211955837
16536731844
16521999611
16210745261
16227212129
16756340321
17025822054
17106139162
17025594919
16756612990
16222651556
17145236617
17019416834
16211722271
16756340395
16254431323
16259504130
16798260640
17145343479
17108391563
17108390272
17025829392
"""

nr = txx.splitlines()
print(nr)

# ff = os.getcwd()
start = time.time()
# with open(ff + '\\1.txt', 'r', encoding='utf-8') as f:
#     cont = f.readlines()
#     # print(cont)
#     # print('a')
#     f.close()
# num = []
# for c in cont:
#     num.append(c.strip())
num = nr
print(num)

ydk = 0
dkcg = 0
shibai = 0
i = 0
for n in num:
    if i < k:
        i += 1
        continue
    i += 1
    # s1 = 0
    for s1 in range(1, 4):
        try:
            jg = dl(n)
            k += 1
            print("开始", k)
            time.sleep(random.random())
            if jg == '你今天已经打过卡了':
                ydk += 1
            elif jg == '积分打卡成功':
                dkcg += 1
            else:
                shibai += 1
            break
        except BaseException:
            print("异常，重试，当前", n)
            time.sleep(5)
            continue
            # s1 += 1

end = time.time()
runTime = end - start
shijian = "耗时:{:.2f}秒".format(runTime)
print(shijian)
ls.append(shijian)
ydks = "今日已经打卡" + str(ydk) + "个"
dkcgs = "积分打卡成功" + str(dkcg) + "个"
shibais = "失败" + str(shibai) + "个"
ls.append(ydks)
ls.append(dkcgs)
ls.append(shibais)
notify.send('qd', ls)
print("已经全部登录")
