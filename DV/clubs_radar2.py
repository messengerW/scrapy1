from pyecharts import Radar, Pie, Page
import xlwings as xw

filepath = "C:/Users/mushr/Desktop/433/创3/clubs.xlsx"

def CreateCharts():
    page = Page()

    app = xw.App(visible=False, add_book=False)
    app.display_alerts = False
    app.screen_updating = False
    book = app.books.open(filepath)
    sheet = book.sheets['sheet1']

    _list1 = []
    _list2 = []
    _list3 = []
    _list4 = []
    _list5 = []
    # 从 excel 中获取数据
    cells1 = sheet.range('F3:K3').value  # 第 1 支球队
    cells2 = sheet.range('F4:K4').value  # 第 2 支球队
    cells3 = sheet.range('F5:K5').value  # 第 3 支球队
    cells4 = sheet.range('F6:K6').value  # 第 4 支球队
    cells5 = sheet.range('F7:K7').value  # 第 5 支球队

    # print(data1)
    for cell1,cell2,cell3,cell4,cell5 in zip(cells1,cells2,cells3,cells4,cells5):
        _list1.append(cell1)
        _list2.append(cell2)
        _list3.append(cell3)
        _list4.append(cell4)
        _list5.append(cell5)

    v1 = [_list1]
    v2 = [_list2]
    v3 = [_list3]
    v4 = [_list4]
    v5 = [_list5]

    chart = Radar("进攻属性")
    schema = [
        ("进球", 15),
        ("射门", 20),
        ("射正", 9),
        ("绝佳机会", 20),
        ("机会把握率", 70),
        ("过人", 16),
        # ("被侵犯", 18),
        # ("越位", 5),
    ]

    chart.config(schema)
    chart.add("利物浦", v1)
    chart.add("诺维奇", v2)
    chart.add("曼城", v3)
    chart.add("西汉姆联", v4)
    chart.add("伯恩利", v5)
    page.add(chart)


    # 玫瑰图
    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v2 = [19, 21, 32, 20, 20, 33]
    chart = Pie("饼图-玫瑰图示例", title_pos='center')
    chart.add("商品A", attr, v2, is_random=True,
              radius=[30, 75], rosetype='area',
              is_legend_show=False, is_label_show=True)
    page.add(chart)

    # 雷达图
    schema = [
        ("销售", 6500), ("管理", 16000), ("信息技术", 30000),
        ("客服", 38000), ("研发", 52000), ("市场", 25000)
    ]
    v1 = [[4300, 10000, 28000, 35000, 50000, 19000]]
    v2 = [[5000, 14000, 28000, 31000, 42000, 21000]]
    v3 = [[3000, 9000, 27890, 33000, 43098, 18000]]
    v4 = [[3890, 12098, 29022, 32000, 41000, 20000]]
    chart = Radar("雷达图-默认指示器")
    chart.config(schema)
    chart.add("预算分配", v1)
    chart.add("实际开销", v2)
    chart.add("ddd", v3)
    chart.add("fff", v4)
    page.add(chart)







    app.kill()
    return page

CreateCharts().render("C:\\Users\\mushr\\Desktop\\433\\创3\\DVFiles\\clubs_chart2.html")
