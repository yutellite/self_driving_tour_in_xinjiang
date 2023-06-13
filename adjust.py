from bs4 import BeautifulSoup

with open("custom_travel_route_map.html", "r") as f:
    soup = BeautifulSoup(f, "html.parser")

# 找到存储图表的 <div> 元素并改变其样式
chart_div = soup.find("div", {"class": "chart-container"})
chart_div["style"] = "width:100%;height:100%;"

# 创建新的样式标签
style_tag = soup.new_tag("style")
style_tag.string = """
    html, body {
        width: 100%;
        height: 100%;
        margin: 0;
        padding: 0;
    }
"""

# 将新的样式标签添加到 <head> 部分
soup.head.append(style_tag)

# 写回文件
with open("custom_travel_route_map_full.html", "w") as f:
    f.write(str(soup))
