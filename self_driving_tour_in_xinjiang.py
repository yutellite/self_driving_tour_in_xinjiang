import json
import pyecharts.options as opts
from pyecharts.charts import BMap
from pyecharts.globals import BMapType, ChartType

# https://github.com/pyecharts/pyecharts-gallery/tree/master/BMap

data = [
  ["白巴哈", 1],
  ["贾登峪国家森林公园", 2],
  ["哈巴河", 3],
  ["冲乎尔", 4],
  ["布尔津", 5],
  ["北屯", 6],
  ["塔城", 7],
  ["额敏", 8],
  ["富蕴", 9],
  ["裕民", 10],
  ["乌尔禾", 11],
  ["托里", 12],
  ["阿拉山口", 13],
  ["克拉玛依", 14],
  ["博乐", 15],
  ["精河", 16],
  ["果子沟", 17],
  ["奎屯", 18],
  ["沙湾", 19],
  ["霍尔果斯", 20],
  ["伊宁", 21],
  ["霍城", 22],
  ["尼勒克", 23],
  ["乔尔玛", 24],
  ["乌鲁木齐", 25],
  ["独山子", 26],
  ["石河子", 27],
  ["阜康", 28],
  ["奇台", 29],
  ["木垒", 30],
  ["巴里坤", 31],
  ["昭苏", 32],
  ["反修桥", 33],
  ["和硕", 34],
  ["巴仑台", 35],
  ["托克逊", 36],
  ["达坂城", 37],
  ["吐鲁番", 38],
  ["鄯善", 39],
  ["哈密", 40],
  ["星星峡", 41],
  ["库尔勒", 42],
  ["轮台", 43],
  ["阿图什市", 44],
  ["阿克苏", 45],
  ["库车", 46],
  ["34团", 47],
  ["36团", 48],
  ["和田", 49],
  ["于田", 50],
  ["民丰", 51],
  ["塔中镇", 52],
  ["且末县", 53],
  ["喀什市", 54],
  ["依吞布拉克", 55],
  ["若羌", 56],
  ["布伦口", 57],
  ["大柴旦", 58],
  ["塔什库尔干", 59],
  ["红其拉甫", 60],
  ["莎车", 61],
  ["嘉峪关", 62],
  ["张掖", 63],
  ["武威", 64],
  ["花土沟", 65],
  ["格尔木", 66],
  ["西宁", 67],
  ["乌兰", 68],
  ["兰州", 69],

  # 去的路线
  ["柳州", 70],
  ["重庆", 71],
  ["甘南", 72],

  # 回的路线
  ["茫崖", 73],
  ["海西", 74],
  ["马尔康", 75],
  ["成都", 76],
  ["遵义", 77],
]

geoCoordMap = {
  "白巴哈": [86.804051,48.695714],
  "贾登峪国家森林公园": [87.177628,48.497579],
  "哈巴河": [86.424818, 48.066149],
  "冲乎尔": [87.137852,48.122648],
  "布尔津": [86.88136, 47.707952],
  "北屯": [87.843466, 47.338865],
  "塔城": [82.993557, 46.757383],
  "额敏": [83.633374, 46.531885],
  "富蕴": [89.531953, 46.999951],
  "裕民": [82.989439, 46.207454],
  "乌尔禾": [85.700305, 46.095295],
  "托里": [83.612909, 45.942743],
  "阿拉山口": [82.560725, 45.17967],
  "克拉玛依": [84.874295, 45.608471],
  "博乐": [82.057972, 44.86001],
  "精河": [82.900655, 44.606646],
  "果子沟": [81.174523,44.465576],
  "奎屯": [84.909449, 44.432057],
  "沙湾": [85.637971,44.333301],
  "霍尔果斯": [80.42713, 44.235309],
  "伊宁": [81.284242, 43.915299],
  "霍城": [80.885281, 44.06225],
  "尼勒克": [82.518008, 43.804595],
  "乔尔玛": [84.344562,43.667735],
  "乌鲁木齐": [87.416029, 43.477086],
  "独山子": [84.893613, 44.334407],
  "石河子": [86.086886, 44.311976],
  "阜康": [87.993678, 44.163137],
  "奇台": [89.601081, 44.026898],
  "木垒": [90.290789,43.845927],
  "巴里坤": [93.038454,43.60548],
  "昭苏": [81.135654,43.165811],
  "反修桥": [84.960133,43.140168],
  "和硕": [86.883689, 42.288065],
  "巴仑台": [86.320071,42.755331],
  "托克逊": [88.660164, 42.798546],
  "达坂城": [88.317398, 43.369943],
  "吐鲁番": [89.189825,42.95804],
  "鄯善": [90.220094, 42.874759],
  "哈密": [93.512588,42.830693],
  "星星峡": [95.140532,41.799498],
  "库尔勒": [86.181494, 41.732373],
  "轮台": [84.258212, 41.783813],
  "阿图什市": [76.174906, 39.722079],
  "阿克苏": [80.269927, 41.17386],
  "库车": [82.968459, 41.723448],
  "34团": [87.702885,40.655481],
  "36团": [88.908672,39.248695],
  "和田": [79.920212, 37.118336],
  "于田": [81.683783, 36.862954],
  "民丰": [82.702713, 37.070257],
  "塔中镇": [83.637745,39.042402],
  "且末县": [85.531962,38.151161],
  "喀什市": [76.000313, 39.47365],
  "依吞布拉克": [90.16637,38.399114],
  "若羌": [88.175324, 39.028991],
  "布伦口": [74.958314,38.668998],
  "大柴旦": [95.362336,37.860866],
  "塔什库尔干": [75.22793,37.780643],
  "红其拉甫": [75.552982,36.974029],
  "莎车": [77.252437, 38.420157],
  "嘉峪关": [98.296204, 39.77796],
  "张掖": [100.456984,38.932739],
  "武威": [102.64858,37.936882],
  "花土沟": [90.863822,38.258336],
  "格尔木": [94.929289,36.408422],
  "西宁": [101.785021,36.628251],
  "乌兰": [98.486736,36.935748],
  "兰州": [103.843399,36.065134],

  # 去的路线
  "柳州": [109.417752,24.330644],
  "重庆": [106.555562,29.580807],
  "甘南": [102.907813,34.990795],

  # 回的路线
  "茫崖": [90.87952,38.261904],
  "海西": [97.388947,37.360265],
  "马尔康": [102.247424,31.893601],
  "成都": [104.07332,30.666756],
  "遵义": [107.041949,27.719884],
}

data_depart = [
  # 去的路线
  ["柳州", 70],
  ["重庆", 71],
  ["甘南", 72],
]

data_return = [
  # 回的路线
  ["茫崖", 73],
  ["海西", 74],
  ["马尔康", 75],
  ["成都", 76],
  ["遵义", 77],
]

geoCoordMap_depart = {
  # 去的路线
  "柳州": [109.417752,24.330644],
  "重庆": [106.555562,29.580807],
  "甘南": [102.907813,34.990795],
}

geoCoordMap_return = {
  # 回的路线
  "茫崖": [90.87952,38.261904],
  "海西": [97.388947,37.360265],
  "马尔康": [102.247424,31.893601],
  "成都": [104.07332,30.666756],
  "遵义": [107.041949,27.719884],
}

def convert_data():
    res = []
    for i in range(len(data)):
        geo_coord = geoCoordMap[data[i][0]]
        geo_coord.append(data[i][1])
        print("geo_coord.{0}, {1}".format(data[i][0], geo_coord))
        res.append([data[i][0], geo_coord])
    return res

def convert_data_depart():
    res = []
    for i in range(len(data_depart)):
        geo_coord = geoCoordMap_depart[data_depart[i][0]]
        geo_coord.append(data_depart[i][1])
        print("geo_coord.{0}, {1}".format(data_depart[i][0], geo_coord))
        res.append([data_depart[i][0], geo_coord])
    return res

def convert_data_return():
    res = []
    for i in range(len(data_return)):
        geo_coord = geoCoordMap_return[data_return[i][0]]
        geo_coord.append(data_return[i][1])
        print("geo_coord.{0}, {1}".format(data_return[i][0], geo_coord))
        res.append([data_return[i][0], geo_coord])
    return res

# 要获取高速，需要进入百度地图开放平台->驾车路线规划里获取高速的所有经纬度信息
# 服务端的 ak=W0GWUbeHEGp74RlxGCSAthpRLOdk6vOq
# https://api.map.baidu.com/directionlite/v1/driving?origin=40.01116,116.339303&destination=39.936404,116.452562&ak=W0GWUbeHEGp74RlxGCSAthpRLOdk6vOq
# 读取项目中的 json 文件
# 1.G580 高速公路 2.吐和高速
with open("xinjiang_highways.json", "r", encoding="utf-8") as f:
    map_data = json.load(f)

(
    BMap(init_opts=opts.InitOpts(width="1200px", height="800px"))
    .add(
        type_="effectScatter",
        series_name="",
        data_pair=convert_data(),
        symbol_size=5,
        effect_opts=opts.EffectOpts(),
        label_opts=opts.LabelOpts(formatter="{b}", position="right", is_show=True),
        itemstyle_opts=opts.ItemStyleOpts(color="purple"),
    )
    .add(
        type_="effectScatter",
        series_name="",
        data_pair=convert_data_depart(),
        symbol_size=5,
        effect_opts=opts.EffectOpts(),
        label_opts=opts.LabelOpts(formatter="{b}", position="right", is_show=True),
        itemstyle_opts=opts.ItemStyleOpts(color="red"),
    )
    .add(
        type_="effectScatter",
        series_name="",
        data_pair=convert_data_return(),
        symbol_size=5,
        effect_opts=opts.EffectOpts(),
        label_opts=opts.LabelOpts(formatter="{b}", position="right", is_show=True),
        itemstyle_opts=opts.ItemStyleOpts(color="yellow"),
    )
    .add(
        series_name="",
        type_=ChartType.LINES,
        data_pair=map_data,
        is_polyline=True,
        is_large=True,
        linestyle_opts=opts.LineStyleOpts(color="purple", opacity=0.6, width=10),
        effect_opts=opts.EffectOpts(trail_length=0.5),
    )
    .add_schema(
        baidu_ak="15bKtTqehCDWOMdxwPEPUHc6GjA0sjQO",
        center=[104.114129, 37.550339],
        zoom=5,
        is_roam=True
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="新疆自驾游",
            subtitle="xinjiang",
            subtitle_link="",
            pos_left="center",
            title_textstyle_opts=opts.TextStyleOpts(color="#fff"),
        ),
        tooltip_opts=opts.TooltipOpts(trigger="item"),
    )
    .render("self_driving_tour_in_xinjiang.html")
)

# 显示样式可以在线调试https://lbsyun.baidu.com/customv2/editor/4be16f58ba712959f25faea02b27d1dc
'''
map_style={
    "styleJson": [
        {
            "featureType": "highway",
            "elementType": "all",
            "stylers": {"visibility": "on"},
        }
    ]
}
'''