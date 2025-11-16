"""Minimal Scrapy spider used in the lectures."""

import scrapy


class BrickSetSpider(scrapy.Spider):
    """Fetch the Brickset 2016 page and let other callbacks do the heavy lifting."""

    name = "brickset_spider"
    start_urls = ["http://brickset.com/sets/year-2016"]

    def parse(self, response):
        """Yield the raw response so follow-up spiders can inspect it."""

        yield {"url": response.url, "status": response.status}
