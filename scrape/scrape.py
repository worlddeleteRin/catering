import scrapy
from urllib.parse import urljoin
import os

PATH = os.getcwd()

main_path = 'https://catering-krym.ru/nashe-menyu/'


class Cosmetics(scrapy.Spider):
    name = 'catering'
    start_urls = [main_path]

    def parse(self, r):
        menu_item = r.css('.bt-menu-item')
        for item in menu_item:
            name = item.css('h4::text').extract_first()
            price = item.css('.bt-menu-itemPrice::text').extract_first()
            imgurl = item.css('.bt-menu-itemThumb a ::attr(href)').extract_first()
            category = item.css('div')[0].xpath('@class').extract()
            context = {
                'name': name,
                'price': price,
                'imgurl': imgurl,
                'category': category,
            }
            yield context


        

