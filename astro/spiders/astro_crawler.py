import scrapy
import urllib.parse
from ..items import AstroItem 


class AstroSpider(scrapy.Spider):
    name = 'astro'
    start_urls = [
        'http://astro.click108.com.tw/'
    ]

    def parse(self, response):

        for href in response.xpath('//div[@class="STAR12_BOX"]/ul/li/a/@href').extract():
            href = urllib.parse.unquote(href.split('To=')[1])
            yield scrapy.Request(url=href, callback=self.parse_content)
            
    
    def parse_content(self, response):
        astro_item = AstroItem()
        astro_item['day'] = response.xpath('//select[@id="iAcDay"]/option[@selected="selected"]/text()').get()
        astro_item['constellation'] = response.css('div.TODAY_CONTENT h3::text').get()[2:5]
        astro_item['overall'] = response.css('span.txt_green::text').get() + response.css('div.TODAY_CONTENT p::text').getall()[0]
        astro_item['love'] = response.css('span.txt_pink::text').get() + response.css('div.TODAY_CONTENT p::text').getall()[1]
        astro_item['carrer'] = response.css('span.txt_blue::text').get() + response.css('div.TODAY_CONTENT p::text').getall()[2]
        astro_item['money'] = response.css('span.txt_orange::text').get() + response.css('div.TODAY_CONTENT p::text').getall()[3]

        return astro_item


