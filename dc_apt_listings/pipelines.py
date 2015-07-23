# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import datetime
import logging
import psycopg2


logger = logging.getLogger('pg_pipeline')

# class DcAptListingsPipeline(object):
#     def process_item(self, item, spider):
#         return item


class PostgresPipeline(object):
    def __init__(self, user='dcapa', password='dcapa', dbname='dc_apa_scraping',
                 host='localhost'):
        self.user = user
        self.password = password
        self.dbname = dbname
        self.host = host

    def open_spider(self, spider):
        self.conn = psycopg2.connect(
            user=self.user,
            dbname=self.dbname,
            host=self.host,
            password=self.password
        )

    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item, spider):
        sql = """
            insert into raw_data ( title, url, price, bedrooms, maplink,
              longitude, latitude, updated_on, content, image_links,
               attributes, size, parsed_on         )
            values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        params = [
            item['title'],
            item['url'],
            item['price'],
            item['bedrooms'],
            item['maplink'],
            item['longitude'],
            item['latitude'],
            item['updated_on'],
            item['content'],
            item['image_links'],
            item['attributes'],
            item['size'],
            datetime.datetime.now()
        ]

        with self.conn.cursor() as cur:
            logger.debug("attempting insert")
            cur.execute(sql, params)
            self.conn.commit()
            logger.debug("status: {}".format(self.conn.status))

        return item
