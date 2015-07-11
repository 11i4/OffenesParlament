from __future__ import absolute_import

import scrapy
from scrapy.crawler import CrawlerProcess

from celery import shared_task


DEFAULT_CRAWLER_OPTIONS = {
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
}


@shared_task
def scrape(spider):
    process = CrawlerProcess(DEFAULT_CRAWLER_OPTIONS)
    process.crawl(spider)
    # the script will block here until the crawling is finished
    process.start()
    return


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)
