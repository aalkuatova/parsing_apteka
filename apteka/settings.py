
BOT_NAME = 'apteka'

SPIDER_MODULES = ['apteka.spiders']
NEWSPIDER_MODULE = 'apteka.spiders'
ROTATING_PROXY_LIST = [
    "https://0Bb7Tp:KGUFPk@45.129.7.7:8000",
    "https://0Bb7Tp:KGUFPk@45.129.7.156:8000",
    "https://0Bb7Tp:KGUFPk@45.129.7.178:8000",
    "https://0Bb7Tp:KGUFPk@45.129.6.155:8000",
    "https://0Bb7Tp:KGUFPk@45.129.6.101:8000",
    "https://0Bb7Tp:KGUFPk@45.129.5.7:8000"
]

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'apteka (+http://www.yourdomain.com)'
USER_AGENT = [
  # 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15',
              'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36']
# Obey robots.txt rules
ROBOTSTXT_OBEY = False 

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 5

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.2
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'apteka.middlewares.AptekaSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'apteka.middlewares.AptekaDownloaderMiddleware': 543,
#}
DOWNLOADER_MIDDLEWARES = {
  #  'veter.middlewares.VeterDownloaderMiddleware': 543,
  'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
  'rotating_proxies.middlewares.BanDetectionMiddleware': 620}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'apteka.pipelines.AptekaPipeline': 1
}
IMAGES_STORE = 'images_folder/test' 

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
FEED_EXPORT_ENCODING = 'utf-8'
FEED_EXPORT_FIELDS = ['high_category','small_category', 'name', 'price','sku','description',
'specification','image_urls','prod_link','image_link']
