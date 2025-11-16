"""Full spider that paginates through the Brickset catalogue."""

import scrapy


class BrickSetSpider(scrapy.Spider):
    name = "brick_spider"
    start_urls = ["http://brickset.com/sets/year-2016"]

    def parse(self, response):
        set_selector = ".set"
        for brickset in response.css(set_selector):
            name_selector = "h1 ::text"
            pieces_selector = './/dl[dt/text() = "Pieces"]/dd/a/text()'
            minifigs_selector = './/dl[dt/text() = "Minifigs"]/dd[2]/a/text()'
            image_selector = "img ::attr(src)"
            yield {
                "name": brickset.css(name_selector).get(),
                "pieces": brickset.xpath(pieces_selector).get(),
                "minifigs": brickset.xpath(minifigs_selector).get(),
                "image": brickset.css(image_selector).get(),
            }

        next_page_selector = ".next a ::attr(href)"
        next_page = response.css(next_page_selector).get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
