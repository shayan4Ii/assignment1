import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):





        
        title = response.xpath('//div[contains(@class, "col-md-8")]//h1//a/text()').get()
        quotes = response.xpath('//div[contains(@class, "quote")]')
        relative_url = response.xpath('//li[contains(@class, "next")]/a/@href').get()


        for quote in quotes:
            yield{
                'title' : title,
                'quote' : quote.xpath('.//span[contains(@class, "text")]/text()').getall(),
                'author' : quote.xpath('.//span//small[contains(@class, "author")]/text()').get(),
                'Tags' : quote.xpath('.//div[contains(@class, "tags")]//a[contains(@class, "tag")]/text()').getall()

            }
#            relative_url = response.xpath('//li[contains(@class, "next")]/a/@href').get()

            if relative_url:

                next_page_url = "https://quotes.toscrape.com" + relative_url
                yield response.follow(next_page_url, callback=self.parse)
            else:
                ("No more Page!")


