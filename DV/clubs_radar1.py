from pyecharts import Pie
attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [11, 12, 13, 10, 10, 10]
pie = Pie("饼图示例")#新建饼图示例pie

pie.add("", attr, v1, is_label_show=True)
pie.show_config()#是否在命令行中显示config，此行可省略
pie.render("普通饼图示例.html")