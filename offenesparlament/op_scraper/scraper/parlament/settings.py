# -*- coding: utf-8 -*-

# Scrapy settings for laws project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'scraper'

SPIDER_MODULES = ['parlament.spiders']
NEWSPIDER_MODULE = 'parlament.spiders'

BASE_HOST = "http://www.parlament.gv.at"

LOG_LEVEL = 'INFO'
DOWNLOADER_STATS = False
STATS_ENABLED = False
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'laws (+http://www.yourdomain.com)'


# CONCURRENT_REQUESTS_PER_DOMAIN = 4
# CONCURRENT_REQUESTS = 8

AUTOTHROTTLE_ENABLED = False
