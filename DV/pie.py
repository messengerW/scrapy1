from pyecharts import Pie

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [11, 12, 13, 10, 10, 10]
pie = Pie("饼图-圆环图示例", title_pos='left')
pie.add("", attr, v1, radius=[40, 75], label_text_color=None,
        is_label_show=True,legend_orient='vertical',
        legend_pos='right')
pie.show_config()           # 是否在命令行中显示config，此行可省略
pie.render("pie.html")