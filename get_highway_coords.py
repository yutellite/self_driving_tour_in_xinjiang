# encoding:utf-8
import requests 

# 接口地址
url = "https://api.map.baidu.com/directionlite/v1/driving"

# 此处填写你在控制台-应用管理-创建应用后获取的AK
ak = "W0GWUbeHEGp74RlxGCSAthpRLOdk6vOq"

params = {
    "origin":    "42.967329,89.182926", # 吐鲁番
    "destination":    "37.120217,79.934835", # 和田
    "ak":       ak,
    "tactics" : 3,
    "radius" : 6,
    "coord_type" : "bd09ll",
    "ret_coordtype" : "bd09ll",

}

response = requests.get(url=url, params=params)
if response:
    print(response.json())