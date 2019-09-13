#   2019.04.22

import scrapy
from scrapy1.items import DoubanItem


class DoubanSpider(scrapy.Spider):
    name = 'spider_douban'

    allowed_domains = ['movie.douban.com']

    start_urls = ['https://movie.douban.com/top250']

    #   这个可以直接在settings里面修改
    # # 如果网站设置有防爬措施，需要添加上请求头信息，不然会爬取不到任何数据
    # header = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 '
    #                   'Safari/537.36',
    #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    # }
    #
    # # start_requests方法为scrapy的方法，我们对它进行重写。
    # def start_requests(self):
    #     # 将start_url中的链接通过for循环进行遍历。
    #     for url in self.start_urls:
    #         # 通过yield发送Request请求。
    #         # 这里的Request注意是scrapy下的Request类。注意不到导错类了。
    #         # 这里的有3个参数：
    #         #        1、url为遍历后的链接
    #         #        2、callback为发送完请求后通过什么方法进行处理，这里通过parse方法进行处理。
    #         #        3、如果网站设置了防爬措施，需要加上headers伪装浏览器发送请求。
    #
    #         yield scrapy.Request(url=url, callback=self.parse, headers=self.header)

    def parse(self, response):
        movie_list = response.xpath("//*[@id='content']/div/div[1]/ol/li")
        for i_item in movie_list:
            douban_item = DoubanItem()
            douban_item['no'] = i_item.xpath(".//div/div[1]/em/text()").extract()
            douban_item['name'] = i_item.xpath(".//div/div[2]/div[1]/a/span[1]/text()").extract()
            content = i_item.xpath(".//div/div[2]/div[2]/p[1]/text()").extract()
            #   注意! content 获取的是第1个 p 标签！ 没有 p[0]
            #   下面这个 for 循环就是处理 p 标签里的内容，.join() 和 .split() 都是字符串处理函数
            for i_content in content:
                content_s = "".join(i_content.split())
                #   把处理好的内容存入
                douban_item['info'] = content_s
            douban_item['star'] = i_item.xpath(".//div/div[2]/div[2]/div/span[2]/text()").extract()
            douban_item['num'] = i_item.xpath(".//div/div[2]/div[2]/div/span[4]/text()").extract()
            quote = i_item.xpath(".//div/div[2]/div[2]/p[2]/span/text()").extract()
            # 因为可能出现 quote 字段为空的情况，所以 if 判断一哈
            if quote:
                # strip()函数移除字符串头尾指定的字符（默认为空格或换行符），ps：对中间部分无效
                quote = quote[0].strip()
            else:
                quote = ' '
            douban_item['introduce'] = quote
            yield douban_item

        # 获取下一页地址
        next_link = response.xpath("//span[@class='next']/link/@href").extract()
        if next_link:
            next_link = next_link[0]
            yield scrapy.Request("https://movie.douban.com/top250" + next_link, callback=self.parse)
