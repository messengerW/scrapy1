"""
    File   : top250.py
    Author : msw
    Date   : 2020/1/30 17:41
    Ps     : wzx ya wzx 放假回来躺尸半个月了！

"""
import scrapy
from scrapy1.items import DoubanItem

class Top250(scrapy.Spider):

    name = 'spider1'

    start_url = 'https://movie.douban.com/top250'

    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    }

    def start_requests(self):
        yield scrapy.Request(url=self.start_url, headers=self.header)

    def parse(self, response):
        li_list = response.xpath("//*[@id='content']/div/div[1]/ol/li")
        for li in li_list:
            movie_item = DoubanItem()
            movie_item['id'] = li.xpath(".//div/div[1]/em/text()").extract_first()
            movie_item['name'] = li.xpath(".//div/div[2]/div[1]/a/span[1]/text()").extract_first()
            content = li.xpath(".//div/div[2]/div[2]/p[1]/text()").extract()
            #   注意! content 获取的是第1个 p 标签！ 没有 p[0]
            #   下面这个 for 循环就是处理 p 标签里的内容，.join() 和 .split() 都是字符串处理函数
            for i_content in content:
                content_s = "".join(i_content.split())
                #   把处理好的内容存入
                movie_item['info'] = content_s
            movie_item['score'] = li.xpath(".//div/div[2]/div[2]/div/span[2]/text()").extract_first()
            movie_item['num'] = li.xpath(".//div/div[2]/div[2]/div/span[4]/text()").extract_first()
            quote = li.xpath(".//div/div[2]/div[2]/p[2]/span/text()").extract()
            # 因为可能出现 quote 字段为空的情况，所以 if 判断一哈
            if quote:
                # strip()函数移除字符串头尾指定的字符（默认为空格或换行符），ps：对中间部分无效
                quote = quote[0].strip()
            else:
                quote = ' '
            movie_item['introduce'] = quote
            yield movie_item

            # 获取下一页地址
            next_link = response.xpath("//span[@class='next']/link/@href").extract()
            if next_link:
                next_link = next_link[0]
                yield scrapy.Request(self.start_url + next_link, callback=self.parse,
                                     headers=self.header)
