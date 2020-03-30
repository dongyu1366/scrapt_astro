# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3


class AstroPipeline(object):
	def open_spider(self, spider):
		self.conn = sqlite3.connect('astro.sqlite')
		self.cur = self.conn.cursor()
		self.cur.execute('''create table if not exists astro(
                            day TEXT, 
                            constellation TEXT, 
                            overall TEXT, 
                            love TEXT, 
                            carrer TEXT, 
                            money TEXT)''')
	
	def close_spider(self, spider):
		self.conn.commit()
		self.conn.close()
	
	def process_item(self, item, spider):
		col = ','.join(item.keys())
		placeholders = ','.join(len(item) * '?')
		sql = 'insert into astro({}) values({})'
		self.cur.execute("insert into astro values(?,?,?,?,?,?)",(
            item['day'], 
            item['constellation'], 
            item['overall'],
            item['love'],
            item['carrer'],
            item['money'],
            ))
		return item