from scrapy.spiders import CrawlSpider


class GoogleCustomSpider(CrawlSpider):
    name = "test_google_play"
    allowed_domains = ["play.google.com"]
    start_urls = [
        'https://play.google.com/'
    ]

    def __init__(self, *a, **kw):
        super(GoogleCustomSpider, self).__init__(*a, **kw)

    def parse_app(self, response):
        return response
