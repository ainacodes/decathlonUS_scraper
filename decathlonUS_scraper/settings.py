from shutil import which
import os

ROTATING_PROXY_LIST_PATH = 'proxy-list.txt'


def get_proxies():
    proxies = []
    if os.path.exists(ROTATING_PROXY_LIST_PATH):
        with open(ROTATING_PROXY_LIST_PATH, 'r') as file:
            for line in file:
                proxy = line.strip()
                if proxy:
                    proxies.append(f"http://{proxy}")
    return proxies


# Set the formatted proxy list as a Scrapy setting
ROTATING_PROXY_LIST = get_proxies()

BOT_NAME = "decathlonUS_scraper"

SPIDER_MODULES = ["decathlonUS_scraper.spiders"]
NEWSPIDER_MODULE = "decathlonUS_scraper.spiders"

ROBOTSTXT_OBEY = True

CONCURRENT_REQUESTS = 8

SPIDER_MIDDLEWARES = {
    "decathlonUS_scraper.middlewares.DecathlonusScraperSpiderMiddleware": 543,
}

DOWNLOADER_MIDDLEWARES = {
    "decathlonUS_scraper.middlewares.DecathlonusScraperDownloaderMiddleware": 543,
    'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
    'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
}

ITEM_PIPELINES = {
    "decathlonUS_scraper.pipelines.DecathlonusScraperPipeline": 300,
}

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

FEEDS = {
    'products_details.csv': {
        'format': 'csv',
        'overwrite': True,
    },
}
