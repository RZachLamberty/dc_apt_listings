# -*- coding: utf-8 -*-

# Scrapy settings for dc_apt_listings project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'dc_apt_listings'

SPIDER_MODULES = ['dc_apt_listings.spiders']
NEWSPIDER_MODULE = 'dc_apt_listings.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'dc_apt_listings (+http://www.yourdomain.com)'

LOG_FILE = "/tmp/dc_apt_listings.log"
ITEM_PIPELINES = {
    'dc_apt_listings.pipelines.PostgresPipeline': 100,
}
