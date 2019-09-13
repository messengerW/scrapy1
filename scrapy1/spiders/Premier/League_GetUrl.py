# 好吧，试了好多次，暂时还不会直接在别的类里面使用这个类爬到的 urls，没办法只能通过先把
# 这个类爬到的 urls 写进 excel 里面 然后再在需要的类里面读取
# 使用的话，只需要把目录下的原来的urls.xls清空，然后把 下面 start_urls 地址的数字改一下就可以了
# 还在不断完善中···
# 我宣布...xlrd 还有 xlwt 淘汰辽
# 注意，这个 xlwings 下标从1开始，第一个单元格 (1,1)
import scrapy
import xlwings as xw

filepath = "C:/Users/mushr/Desktop/433/urls.xlsx"  # 要保存的地址及文件名

class GetUrl(scrapy.Spider):
    name = 'spider_geturls'

    allowed_domains = ['tzuqiu.cc']

    start_urls = ['http://www.tzuqiu.cc/teams/3/fixture.do', ]

    def parse(self, response):
        # 打开一个workbook
        app = xw.App(visible=False, add_book=False)
        wb = app.books.open(filepath)
        sheet = wb.sheets['sheet1']
        sheet.clear()

        # 获取当前页面的球队，即打开的是哪个球队的赛程板
        mpage_team = response.xpath(
            "//div[@class='container mainfdb']/div[1]/div[1]/div[1]/div[1]/h1/text()").extract_first()
        mpage_team = "".join(mpage_team.split())

        # 获取到当前页面 table 下面所有的 tr，存入列表
        tr_list = response.xpath("//table[@class='fiture team-fixture']//tbody[@id='fixture-body']/tr")
        print("========>>>> %s 一共有 %d 条比赛信息" % (mpage_team, len(tr_list)))
        for i in tr_list:  # 注意这里的 i 可不是数字 而是一个个的 xpath
            # 获取到比赛性质（欧冠、联赛、足总杯...）
            game_properties = i.xpath(".//td[3]/a/@title").extract_first()
            # 获取 tr 中主队那一栏的球队名称，与之前获取的整个页面的球队名称比较
            home_team = i.xpath(".//td[5]/a/@title").extract_first()
            url = i.xpath(".//td[10]/a/@href").extract_first()
            # 这里被坑了一下，必须判断是否为空
            if url:
                next_url = 'http://www.tzuqiu.cc' + url
            # write写函数原型 sheet.write(i,j,'...')
            # i 行号，j 列号，''里面是要写的内容
            if game_properties == '英超':  # 英超赛事
                if home_team == mpage_team:
                    sheet.range(1, 1).value = "英超主场"
                    # 5.28修改一个bug,此处应该是+2，否则第一条信息会被覆盖
                    sheet.range(tr_list.index(i) + 2, 1).value = next_url
                else:
                    sheet.range(1, 2).value = "英超客场"
                    sheet.range(tr_list.index(i) + 2, 2).value = next_url

            elif game_properties == '欧冠':  # 欧冠赛事
                if home_team == mpage_team:
                    sheet.range(1, 3).value = "欧冠主场"
                    sheet.range(tr_list.index(i) + 2, 3).value = next_url
                else:
                    sheet.range(1, 4).value = "欧冠客场"
                    sheet.range(tr_list.index(i) + 2, 4).value = next_url

            else:  # 其他赛事
                if home_team == mpage_team:
                    sheet.range(1, 5).value = "其他赛事主场"
                    sheet.range(tr_list.index(i) + 1, 5).value = next_url
                else:
                    sheet.range(1, 6).value = "其他赛事客场"
                    sheet.range(tr_list.index(i) + 1, 6).value = next_url

        wb.save()
        app.kill()
