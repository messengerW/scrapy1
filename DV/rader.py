from pyecharts import Radar
import xlwings as xw

filepath = "C:/Users/mushr/Desktop/433/创3/前锋.xlsx"

app = xw.App(visible=False, add_book=False)
app.display_alerts = False
app.screen_updating = False
book = app.books.open(filepath)
sheet = book.sheets['sheet1']

data1 = sheet.range('G2:P2').value  # 第一串数据
data2 = sheet.range('G3:P3').value  # 第二串数据

_list1 = []
_list2 = []
i = 0
j = 0

print(data1)
radar = Radar("雷达图", "球员能力值")
k = 0
for itemm in data1:
    print("%d : %s" % (k, itemm))
    k = k + 1
for item in data1:
    print(item)
    _list1.append(item)

radar_data1 = [_list1]
radar_data2 = [_list2]
schema = [
    ("出场时间(minutes)", 3500),
    ("进球", 30),
    ("助攻", 25),
    ("传球成功率", 100),
    ("创造机会", 22),
    ("争顶成功", 1),
    ("全场最佳", 25),
    ("综合得分", 10)
]
radar.config(schema)
radar.add("阿扎尔", radar_data1)
radar.add("斯特林", radar_data2, item_color="#1C86EE")
radar.render("C:\\Users\\mushr\\Desktop\\433\\创3\\DVFiles\\radar.html")
