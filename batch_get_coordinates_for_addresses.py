'''
{
    "status":"OK",
    "result":{
        "location":{
            "lng":116.30657,
            "lat":40.059181
        },
        "precise":0,
        "confidence":80,
        "level":"\u95e8\u5740"
    }
}
15bKtTqehCDWOMdxwPEPUHc6GjA0sjQO
'''
import requests
import json
import time

def get_location(address):
    time.sleep(0.1)
    url = f"http://api.map.baidu.com/geocoder?address={address}&output=json&key=15bKtTqehCDWOMdxwPEPUHc6GjA0sjQO"
    print("URL:", url)
    res = requests.get(url)
    json_data = res.text
    try:
        json_data = json.loads(json_data)
        if json_data['status'] == 'OK':
            lng = json_data['result']['location']['lng']
            lat = json_data['result']['location']['lat']
            return address, (lng, lat)
        else:
            print(f"无法获取地址 {address} 的坐标信息")
            print(f"API 响应: {json_data}")
            return None
    except json.decoder.JSONDecodeError:
        print("无法解析响应中的 JSON 数据")
        print("URL:", url)
        print("响应内容:", res.text)
        return None

def get_locations(addresses):
    locations = []
    for address in addresses:
        location = get_location(address)
        if location:
            locations.append(location)
    return locations
'''
addresses = [
    '白巴哈',
    '贾登峪国家森林公园',
    '哈巴河',
    '冲乎尔',
    '布尔津',
    '北屯',
    '塔城',
    '额敏',
    '富蕴',
    '裕民',
    '乌尔禾',
    '托里',
    '阿拉山口',
'克拉玛依',
'博乐',
'精河',
'果子沟',
'奎屯',
'沙湾',
'霍尔果斯',
'伊宁',
'霍城',
'尼勒克',
'乔尔玛',
'乌鲁木齐',
'独山子',
'石河子',
'阜康',
'奇台',
'木垒',
'巴里坤',
'昭苏',
'反修桥',
'和静',
'和硕',
'巴仑台',
'托克逊',
'达坂城',
'吐鲁番',
'鄯善',
'哈密',
'星星峡',
'库尔勒',
'尉犁',
'轮台',
'阿图什市',
'阿克苏',
'库车',
'34团',
'36团',
'和田',
'于田',
'民丰',
'塔中',
'且末',
'喀什',
'依吞布拉克',
'若羌',
'布伦口',
'大柴旦',
'塔什库尔干',
'红其拉甫',
'莎车'
]
'''
addresses = [
'瓜州',
'敦煌',
'嘉峪关',
'酒泉',
'临泽',
'张掖',
'武威',
'花土沟',
'格尔木',
'西宁',
'乌兰',
'德令哈',
]
locations = get_locations(addresses)
print(locations)
