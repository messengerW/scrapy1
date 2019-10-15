#   2019.04.22

import scrapy
from scrapy1.items import DoubanItem


class DoubanSpider(scrapy.Spider):
    name = 'spider_douban'

    allowed_domains = ['movie.douban.com']

    start_urls = ['https://movie.douban.com/top250']

    #   这个可以直接在settings里面修改
    # 如果网站设置有防爬措施，需要添加上请求头信息，不然会爬取不到任何数据
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'
    }

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
            yield scrapy.Request("https://movie.douban.com/top250" + next_link, callback=self.parse, headers=self.header)
