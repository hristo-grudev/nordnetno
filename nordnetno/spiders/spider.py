import scrapy

from scrapy.loader import ItemLoader

from ..items import NordnetnoItem
from itemloaders.processors import TakeFirst


class NordnetnoSpider(scrapy.Spider):
	name = 'nordnetno'
	start_urls = ['https://www.nordnet.no/blogg/artikler/']

	def parse(self, response):
		post_links = response.xpath('//h2/a/@href').getall()
		yield from response.follow_all(post_links, self.parse_post)

		next_page = response.xpath('//a[@class="next page-numbers"]/@href').getall()
		yield from response.follow_all(next_page, self.parse)

	def parse_post(self, response):
		title = response.xpath('//h1/text()').get()
		description = response.xpath('//div[@id="content"]//div[@class="entry-content"]//text()[normalize-space()]').getall()
		description = [p.strip() for p in description]
		description = ' '.join(description).strip()
		date = response.xpath('//div[@class="single-author-wrap"]//span[@class="updated"]/text()').get()

		item = ItemLoader(item=NordnetnoItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('date', date)

		return item.load_item()
