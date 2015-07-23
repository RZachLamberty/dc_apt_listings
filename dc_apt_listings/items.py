# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class DcAptListingsItem(Item):
    title = Field()
    url = Field()
    price = Field()
    bedrooms = Field()
    maplink = Field()
    longitude = Field()
    latitude = Field()
    updated_on = Field()
    content = Field()
    image_links = Field()
    attributes = Field()
    size = Field()
