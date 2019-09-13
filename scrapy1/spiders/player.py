# 2019.04.22
#   这个爬虫是个测试的例子，写的时候遇到了点困难：
#   第一个是可能网站由反爬，但是像之前一样 F12 -> Network -> Request Header -> User-Agent，
# copy到 settings.py 中并不管用，然后看网上教程设置了一个随机 U-A （下载包->修改middlewares
# ->修改settings）；
#   第二个问题就是xpath的问题，由于这个网站比豆瓣复杂，嵌套了更多的div，所以手动找元素的时候就很
# 容易出错，然后下载了一个 chrome xpath 的插件，直接 copy 标签的 xpath 然后再稍微修改就可以了。

import scrapy
from scrapy1.items import PlayerItem
from selenium import webdriver
import time


class PlayerSpider(scrapy.Spider):
    name = 'spider_player'

    allowed_domains = ['tzuqiu.cc']

    start_urls = ['http://www.tzuqiu.cc/stats.do']

    def parse(self, response):
        player_list = response.xpath("//*[@id='playerStatSummary']/tbody/tr")
        for i_item in player_list:
            player_item = PlayerItem()
            player_item['no'] = i_item.xpath(".//td[1]/text()").extract()
            player_item['name'] = i_item.xpath(".//td[2]/a/div[2]/text()").extract()
            player_item['club'] = i_item.xpath(".//td[2]/span/a/text()").extract()
            player_item['age'] = i_item.xpath(".//td[2]/span/span[1]/text()").extract()
            player_item['position'] = i_item.xpath(".//td[2]/span/span[2]/text()").extract()
            # 获取 games（上场次数） 信息时需要处理这个 text
            str = i_item.xpath(".//td[3]/text()").extract_first()
            player_item['games'] = "".join(str.split())
            player_item['goals'] = i_item.xpath(".//td[5]/text()").extract()

            yield player_item

        # # 处理翻页（其实不是翻页，因为地址栏url未改变）
        # browser = webdriver.Chrome()
        # browser.get('http://www.tzuqiu.cc/stats.do')
        # # 找到翻页的按钮
        # btn = browser.find_element_by_id('playerStatSummary_next')
        # # 获取按钮的class属性
        # flag = btn.get_attribute("class")
        #
        # if flag != 'paginate_button next disabled':
        #     btn.click()
        #     time.sleep(5)
        #
        # browser.close()

        # next_link = response.xpath("//span[@class='next']/link/@href").extract()
        # if next_link:
        #     next_link = next_link[0]
        #     yield scrapy.Request("https://movie.douban.com/top250" + next_link, callback=self.parse)
