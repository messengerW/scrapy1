"""
    File   : club_turn_charts.py
    Author : msw
    Date   : 2019/9/20 19:17
    Ps     : ...
    
"""
from pyecharts import Radar, Page, Timeline
import xlwings as xw

filepath = "C:/Users/mushr/Desktop/433/club_turn.xlsx"

def CreateCharts():
    page = Page()

    app = xw.App(visible=False, add_book=False)
    app.display_alerts = False
    app.screen_updating = False
    book = app.books.open(filepath)             # 打开 excel

    # 第一张图，绘制的是两支球队的对比图，只用到了第一轮的数据
    sheet1 = book.sheets['turn1']
    _list1 = []
    _list2 = []
    # 从 sheet 中获取数据
    cells1 = sheet1.range('B3:J3').value  # 第 1 支球队
    cells2 = sheet1.range('B4:J4').value  # 第 2 支球队
    for cell1, cell2 in zip(cells1, cells2):
        _list1.append(cell1)
        _list2.append(cell2)

    v1 = [_list1]
    v2 = [_list2]
    chart = Radar("进攻属性")
    schema = [
        ("评分", 10),             # B:rate
        ("传球", 550),            # C:passes
        ("传球成功率", 0.9),       # D:passSucc
        ("控球率",0.6),           # E:
        ("射门", 15),             # F:
        ("拦截", 15),             # G:
        ("解围", 20),             # H:
        ("抢断", 20),             # I:
        ("争顶成功", 20),          # J:
    ]
    chart.config(schema)
    chart.add("曼城", v1)
    chart.add("曼联", v2, item_color="#330f67")
    page.add(chart)

    # 绘制第二张图,某支球队每一轮的走势,用到了 excel 中所有的 sheet
    sht1 = book.sheets['turn1']
    sht2 = book.sheets['turn2']
    sht3 = book.sheets['turn3']
    sht4 = book.sheets['turn4']
    sht5 = book.sheets['turn5']
    _turn1 = []
    _turn2 = []
    _turn3 = []
    _turn4 = []
    _turn5 = []
    # 从 sheet 中获取数据
    cells1 = sht1.range('B3:J3').value  # 第 1 轮
    cells2 = sht2.range('B7:J7').value  # 第 2 轮
    cells3 = sht3.range('B6:J6').value  # 第 3 轮
    cells4 = sht4.range('B3:J3').value  # 第 4 轮
    cells5 = sht5.range('B13:J13').value  # 第 5 轮

    for cell1, cell2, cell3, cell4, cell5 in zip(cells1,cells2,cells3,cells4,cells5):
        _turn1.append(cell1)
        _turn2.append(cell2)
        _turn3.append(cell3)
        _turn4.append(cell4)
        _turn5.append(cell5)

    v1 = [_turn1]
    v2 = [_turn2]
    v3 = [_turn3]
    v4 = [_turn4]
    v5 = [_turn5]

    radar1 = Radar("2019-2020赛季曼城数据（第 1 轮）")
    radar2 = Radar("2019-2020赛季曼城数据（第 2 轮）")
    radar3 = Radar("2019-2020赛季曼城数据（第 3 轮）")
    radar4 = Radar("2019-2020赛季曼城数据（第 4 轮）")
    radar5 = Radar("2019-2020赛季曼城数据（第 5 轮）")

    schema = [
        ("评分", 10),  # B:rate
        ("传球", 550),  # C:passes
        ("传球成功率", 0.9),  # D:passSucc
        ("控球率", 0.6),  # E:
        ("射门", 15),  # F:
        ("拦截", 15),  # G:
        ("解围", 20),  # H:
        ("抢断", 20),  # I:
        ("争顶成功", 20),  # J:
    ]
    radar1.config(schema)
    radar2.config(schema)
    radar3.config(schema)
    radar4.config(schema)
    radar5.config(schema)
    radar1.add("曼城", v1)
    radar2.add("曼城", v2)
    radar3.add("曼城", v3)
    radar4.add("曼城", v4)
    radar5.add("曼城", v5)

    chart = Timeline(is_auto_play=True, timeline_bottom=0)
    chart.add(radar1, '第 1 轮')
    chart.add(radar2, '第 2 轮')
    chart.add(radar3, '第 3 轮')
    chart.add(radar4, '第 4 轮')
    chart.add(radar5, '第 5 轮')
    page.add(chart)


    app.kill()
    return page


CreateCharts().render("C:\\Users\\mushr\\Desktop\\433\\创3\\DVFiles\\club_turn_chart.html")
