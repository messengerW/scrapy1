from pyecharts import Radar
import xlwings as xw

filepath = "C:/Users/mushr/Desktop/433/创3/clubs.xlsx"

app = xw.App(visible=False, add_book=False)
app.display_alerts = False
app.screen_updating = False
book = app.books.open(filepath)
sheet = book.sheets['sheet1']

i = 0
j = 0
_list1 = []
_list2 = []
data1 = sheet.range('B2:G2').value  # 第 1 支球队
data2 = sheet.range('B3:G3').value  # 第 2 支球队

# print(data1)
for item in data1:
    _list1.append(item)

for item in data2:
    _list2.append(item)

radar_data1 = [_list1]
radar_data2 = [_list2]

radar = Radar("雷达图", "球队势力值")
schema = [
    ("射门数", 20),
    ("控球率", 65),
    ("传球成功率", 100),
    ("绝佳机会", 20),
    ("争顶成功", 22),
    ("综合得分", 10)
]

radar.config(schema)
radar.add("曼城", radar_data1)
radar.add("利物浦", radar_data2, item_color="#1C86EE")
radar.render("C:\\Users\\mushr\\Desktop\\433\\创3\\DVFiles\\clubs_radar.html")
