from requests import post
import os
import sys
import json

def get_shop_cards(ck):
    """
    获取加入店铺列表
    :return: 返回店铺列表
    """

    url = "https://api.m.jd.com/client.action?functionId=getWalletReceivedCardList_New&clientVersion=9.5.2&build" \
            "=87971&client=android&d_brand=Xiaomi&d_model=M2007J3SC&osVersion=11&screen=2266*1080&partner=xiaomi001" \
            "&oaid=e02a70327f315862&openudid=3dab9a16bd95e38a&eid=eidA24e181233bsdmxzC3hIpQF2nJhWGGLb" \
            "%2F1JscxFOzBjvkqrXbFQyAXZmstKs0K6bUwkQ0D3s1%2F7MzLZ7JDdhztfcdZur9xPTxU1ahqtHWYb54%2FyNK&sdkVersion=30" \
            "&lang=zh_CN&uuid=3dab9a16bd95e38a&aid=3dab9a16bd95e38a&area=13_1000_40488_54442&networkType=wifi" \
            "&wifiBssid=c609e931512437a8806ae06b86d3977b&uts=0f31TVRjBSsu47QjbY5aZUsO5LYa1B%2F3wqL7JjlFB60vmw6" \
            "%2F8Xbj74d3sWoT4CTQgX7X0M07W75JvIfz5eu7NxdNJ73NSVbgTHkdsiVZ770PEn0MWPywxr4glUdddS6uxIQ5VfPG65uoUmlB6" \
            "%2BBwwDqO1Nfxv8%2Bdm15xR%2BFG4fJWb6wCFO7DFMtnoOMo2CQ8mYoECYG3qT%2Bso7P%2FKLgQcg%3D%3D&uemps=0-0&st" \
            "=1620105615175&sign=65996ece830b41aabdaba32c9d782d07&sv=100"
    payload = "body=%7B%22v%22%3A%224.1%22%2C%22version%22%3A1580659200%7D&"
    headers = {
        'Host': 'api.m.jd.com',
        'cookie': ck,
        'charset': 'UTF-8',
        'accept-encoding': 'br,gzip,deflate',
        'user-agent': 'okhttp/3.12.1;jdmall;android;version/9.5.2;build/87971;screen/1080x2266;os/11;network/wifi;',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'content-length': '60'
        }

    card_list = []
    resp = post(url, headers=headers, data=payload)
    ret = json.loads(resp.text)
    if ret["code"] == "0":
        if ret["message"] == "用户未登录":
            print("请输入正确的京东cookie")
            sys.exit(1)

        if "cardList" not in ret["result"]:
            print("当前卡包中会员店铺为0个")
            sys.exit(1)

        card_list = (ret["result"]["cardList"])
    else:
        print("echo")

    return card_list

ck = input("请输入你的京东cookie（含有py_key和pt_pin）：")
card_list = get_shop_cards(ck)

# 判定一下是否有会员卡
if len(card_list) == 0:
    print ("当前没有加入的店铺信息")
    sys.exit (0)
    
print("本次运行获取到", len(card_list), "家店铺会员信息")

for card in card_list:
    print("店铺名称：" + card["brandName"])
    print("注销地址：https://shopmember.m.jd.com/member/memberCloseAccount?venderId=" + card["brandId"])


print ("\n\n本项目开源地址为：https://www.github.com/hyzaw/JDMemberCloseLinks")
