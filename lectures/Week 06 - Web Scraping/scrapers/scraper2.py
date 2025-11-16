"""Second Scrapy example that extracts the set name with the modern API."""

import scrapy


class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider"
    start_urls = ["http://brickset.com/sets/year-2016"]

    def parse(self, response):
        set_selector = ".set"
        for brickset in response.css(set_selector):
            name_selector = "h1 ::text"
            yield {"name": brickset.css(name_selector).get()}
