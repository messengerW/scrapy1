"""
    File   : club_turn_charts.py
    Author : msw
    Date   : 2019/9/20 19:17
    Ps     : ...
    
"""
import xlwings as xw
from pyecharts import Bar, Radar, Line, Overlap, Page, Timeline

# 打开 excel
filepath = "C:/Users/mushr/Desktop/433/club_turn.xlsx"
app = xw.App(visible=False, add_book=False)
app.display_alerts = False
app.screen_updating = False
book = app.books.open(filepath)


def Chart1():
    # 第一张图，绘制的是两支球队的对比图，只用到了第一轮的数据
    sheet1 = book.sheets['turn1']
    _list1 = []
    _list2 = []
    # 从 sheet 中获取数据
    cells1 = sheet1.range('B4:J4').value  # 第 1 支球队
    cells2 = sheet1.range('B3:J3').value  # 第 2 支球队
    for cell1, cell2 in zip(cells1, cells2):
        _list1.append(cell1)
        _list2.append(cell2)

    v1 = [_list1]
    v2 = [_list2]
    chart = Radar("进攻属性", title_pos='center')
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
    chart.config(schema)
    chart.add("曼城", v1, item_color="#330f67")
    chart.add("利物浦", v2, legend_orient='vertical', legend_pos='left')
    return chart


def Chart2():
    # 绘制第二张图,本赛季 利物浦 每一轮的走势
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
    cells2 = sht2.range('B3:J3').value  # 第 2 轮
    cells3 = sht3.range('B3:J3').value  # 第 3 轮
    cells4 = sht4.range('B3:J3').value  # 第 4 轮
    cells5 = sht5.range('B3:J3').value  # 第 5 轮

    for cell1, cell2, cell3, cell4, cell5 in zip(cells1, cells2, cells3, cells4, cells5):
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

    radar1 = Radar("2019-2020赛季-利物浦（第 1 轮）")
    radar2 = Radar("2019-2020赛季-利物浦（第 2 轮）")
    radar3 = Radar("2019-2020赛季-利物浦（第 3 轮）")
    radar4 = Radar("2019-2020赛季-利物浦（第 4 轮）")
    radar5 = Radar("2019-2020赛季-利物浦（第 5 轮）")

    schema = [
        ("评分", 10),  # B:rate
        ("传球", 1000),  # C:passes
        ("传球成功率", 1),  # D:passSucc
        ("控球率", 0.8),  # E:
        ("射门", 30),  # F:
        ("拦截", 15),  # G:
        ("解围", 30),  # H:
        ("抢断", 25),  # I:
        ("争顶成功", 25),  # J:
    ]
    radar1.config(schema)
    radar2.config(schema)
    radar3.config(schema)
    radar4.config(schema)
    radar5.config(schema)
    radar1.add("利物浦", v1)
    radar2.add("利物浦", v2)
    radar3.add("利物浦", v3)
    radar4.add("利物浦", v4)
    radar5.add("利物浦", v5)

    chart = Timeline(is_auto_play=True, timeline_bottom=0)
    chart.add(radar1, '第 1 轮')
    chart.add(radar2, '第 2 轮')
    chart.add(radar3, '第 3 轮')
    chart.add(radar4, '第 4 轮')
    chart.add(radar5, '第 5 轮')
    return chart

def Chart3():
    # 绘制第 3 张图,本赛季 曼城 每一轮的走势
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
    cells1 = sht1.range('B4:J4').value  # 第 1 轮
    cells2 = sht2.range('B4:J4').value  # 第 2 轮
    cells3 = sht3.range('B4:J4').value  # 第 3 轮
    cells4 = sht4.range('B4:J4').value  # 第 4 轮
    cells5 = sht5.range('B4:J4').value  # 第 5 轮

    for cell1, cell2, cell3, cell4, cell5 in zip(cells1, cells2, cells3, cells4, cells5):
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

    radar1 = Radar("2019-2020赛季-曼城（第 1 轮）")
    radar2 = Radar("2019-2020赛季-曼城（第 2 轮）")
    radar3 = Radar("2019-2020赛季-曼城（第 3 轮）")
    radar4 = Radar("2019-2020赛季-曼城（第 4 轮）")
    radar5 = Radar("2019-2020赛季-曼城（第 5 轮）")

    schema = [
        ("评分", 10),  # B:rate
        ("传球", 750),  # C:passes
        ("传球成功率", 1),  # D:passSucc
        ("控球率", 0.8),  # E:
        ("射门", 30),  # F:
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
    return chart

def Chart4():
    v1 = []
    v2 = []
    sht1 = book.sheets['turn1']
    sht2 = book.sheets['turn2']
    sht3 = book.sheets['turn3']
    sht4 = book.sheets['turn4']
    sht5 = book.sheets['turn5']
    v1.append(float(sht1.range('D3').value)*100)
    v1.append(float(sht2.range('D3').value)*100)
    v1.append(float(sht3.range('D3').value)*100)
    v1.append(float(sht4.range('D3').value)*100)
    v1.append(float(sht5.range('D3').value)*100)

    v2.append(float(sht1.range('D4').value)*100)
    v2.append(float(sht2.range('D4').value)*100)
    v2.append(float(sht3.range('D4').value)*100)
    v2.append(float(sht4.range('D4').value)*100)
    v2.append(float(sht5.range('D4').value)*100)

    attr = ["第{}轮".format(i) for i in range(1, 6)]
    chart = Line("传球成功率")
    chart.add("利物浦", attr, v1)
    chart.add("曼城", attr, v2,is_more_utils=True)

    return chart

def CreateCharts():
    page = Page()

    # 获取到 Chart1() 函数绘制的图，并添加到 page 中
    chart1 = Chart1()
    page.add(chart1)

    # 获取到 Chart2() 函数绘制的图，并添加到 page 中
    chart2 = Chart2()
    page.add(chart2)

    chart3 = Chart3()
    page.add(chart3)

    chart4 = Chart4()
    page.add(chart4)

    app.kill()
    return page


CreateCharts().render("C:/Users/mushr/Desktop/433/创3/DVFiles/club_turn_chart.html")
