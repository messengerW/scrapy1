# # 好吧，试了好多次，暂时还不会直接在别的类里面使用这个类爬到的 urls，没办法只能通过先把
# # 这个类爬到的 urls 写进 excel 里面 然后再在需要的类里面读取
# # 使用的话，只需要把目录下的原来的urls.xls清空，然后把 下面 start_urls 地址的数字改一下就可以了
# # 还在不断完善中···
# # 已淘汰，新的 -> League_GetUrl.py
# import scrapy
# import xlrd
# import os
# from xlutils.copy import copy
#
# filepath = "C:/Users/mushr/Desktop/433/urls.xls"  # 要保存的地址及文件名
#
#
# class GetUrl(scrapy.Spider):
#     name = 'spider_geturls'
#
#     allowed_domains = ['tzuqiu.cc']
#
#     start_urls = ['http://www.tzuqiu.cc/teams/16/fixture.do', ]
#
#     def parse(self, response):
#         # 打开一个workbook
#         rb = xlrd.open_workbook(filepath)  # readbook
#         wb = copy(rb)  # writebook
#         # 获取sheet对象，通过sheet_by_index()获取的sheet对象没有write()方法
#         sheet = wb.get_sheet(0)
#
#         # 获取当前页面的球队，即打开的是哪个球队的赛程板
#         mpage_team = response.xpath("//div[@class='container mainfdb']/div[1]/div[1]/div[1]/div[1]/h1/text()").extract_first()
#         mpage_team = "".join(mpage_team.split())
#
#         # 获取到当前页面 table 下面所有的 tr，存入列表
#         tr_list = response.xpath("//table[@class='fiture team-fixture']//tbody[@id='fixture-body']/tr")
#         print("========>>>> %s 一共有 %d 条比赛信息" %(mpage_team, len(tr_list)))
#         for i in tr_list:  # 注意这里的 i 可不是数字 而是一个个的 xpath
#             # 获取到比赛性质（欧冠、联赛、足总杯...）
#             game_properties = i.xpath(".//td[3]/a/@title").extract_first()
#             # 获取 tr 中主队那一栏的球队名称，与之前获取的整个页面的球队名称比较
#             home_team = i.xpath(".//td[5]/a/@title").extract_first()
#             url = i.xpath(".//td[10]/a/@href").extract_first()
#             # 这里被坑了一下，必须判断是否为空
#             if url:
#                 next_url = 'http://www.tzuqiu.cc' + url
#             # write写函数原型 sheet.write(i,j,'...')
#             # i 行号，j 列号，''里面是要写的内容
#             if game_properties == '英超':             # 英超赛事
#                 if home_team == mpage_team:
#                     sheet.write(0,0,"英超-"+mpage_team+"-主")
#                     sheet.write(tr_list.index(i)+1, 0, next_url)
#                     sheet.col(0).width = 10000       # 设置一下单元格宽度（没什么卵用
#                 else:
#                     sheet.write(0,1,"英超-"+mpage_team+"-客")
#                     sheet.write(tr_list.index(i)+1, 1, next_url)
#                     sheet.col(1).width = 10000
#
#             elif game_properties == '欧冠':           # 欧冠赛事
#                 if home_team == mpage_team:
#                     sheet.write(0,2,"欧冠-"+mpage_team+"-主")
#                     sheet.write(tr_list.index(i)+1, 2, next_url)
#                     sheet.col(2).width = 10000
#                 else:
#                     sheet.write(0,3,"欧冠-"+mpage_team+"-客")
#                     sheet.write(tr_list.index(i)+1, 3, next_url)
#                     sheet.col(3).width = 10000
#
#             else:                                    # 其他赛事
#                 if home_team == mpage_team:
#                     sheet.write(0,4,"其他赛事-"+mpage_team+"-主")
#                     sheet.write(tr_list.index(i)+1, 4, next_url)
#                     sheet.col(4).width = 10000
#                 else:
#                     sheet.write(0,5,"其他赛事-"+mpage_team+"-客")
#                     sheet.write(tr_list.index(i)+1, 5, next_url)
#                     sheet.col(5).width = 10000
#
#         os.remove(filepath)
#         wb.save(filepath)
