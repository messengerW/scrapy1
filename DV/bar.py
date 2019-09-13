from pyecharts import Bar

attr = ['衬衫','羊毛衫','雪纺衫','裤子','高跟鞋','袜子']
v1 = [5,20,36,10,75,90]
v2 = [10,25,8,60,20,80]
bar = Bar('柱状图','X 轴与 Y 轴交换')
bar.add('商家A',attr,v1)  
bar.add('商家B',attr,v2,is_convert = True)    # is_convert = True:X 轴与 Y 轴交换
bar.render("C:\\Users\\mushr\\Desktop\\433\\DVFiles\\barr.html")