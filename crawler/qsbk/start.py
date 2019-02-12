
from scrapy import cmdline

cmdline.execute("scrapy crawl qsbk_spider".split())
#等价于
#cmdline.execute(["scrapy","crawl","qsbk_spider"])