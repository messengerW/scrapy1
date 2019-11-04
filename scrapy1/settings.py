# -*- coding: utf-8 -*-

# Scrapy settings for scrapy1 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
URLLENGTH_LIMIT = 20000         # 默认的GET请求长队最大值为 2083 个字节，这里扩大到 20000

BOT_NAME = 'scrapy1'

SPIDER_MODULES = ['scrapy1.spiders']
NEWSPIDER_MODULE = 'scrapy1.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent

# USER_AGENT = 'scrapy1 (+http://www.yourdomain.com)'
# USER_AGENT = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',]

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'scrapy1.middlewares.Scrapy1SpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html

# DOWNLOADER_MIDDLEWARES = {
#    'scrapy1.middlewares.Scrapy1DownloaderMiddleware': 543,
# }

# 使用随机User-Agent
DOWNLOADER_MIDDLEWARES = {
    'scrapy1.middlewares.RandomUserAgentMiddlware': 1000,
}


# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'scrapy1.pipelines.Scrapy1Pipeline': 300,
# }

COOKIES_ENABLED = True                  #禁止cookies,防止被ban

# 设置 MySQL 连接
MYSQL_HOST = 'localhost'				#Mysql连接名
MYSQL_PORT = 3306						#连接端口号
MYSQL_USER = 'root'						#Mysql用户名
MYSQL_PASSWORD = '232624'				#Mysql用户密码
MYSQL_DBNAME = '433'				    #Mysql数据库名
MYSQL_CHARSET = 'utf8'

# 设置 MongoDB 连接
MONGODB_HOST = 'localhost'                 # MONGODB 主机名
MONGODB_PORT = 27017                        # MONGODB 端口号
MONGODB_DBNAME = 'England'                  # 设置数据库名称
MONGODB_COLLECTION = 'club_history'          # 设置存放数据的表名称,可以在pipeline中自己设置


# 开通Pipeline
ITEM_PIPELINES = {
    #'scrapy1.pipelines.DoubanPipeline': 100,
    #'scrapy1.pipelines.PlayerPipeline': 200,
    #'scrapy1.pipelines.ClubPipeline': 100,
    # 'scrapy1.pipelines.MongoDBPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
