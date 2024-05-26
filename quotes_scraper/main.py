from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from quotes_scraper.spiders.quotes_spider import QuotesSpider
from quotes_scraper.spiders.authors_spider import AuthorsSpider
from import_to_db import importtodb


def main():
    process = CrawlerProcess(settings=get_project_settings())
    process.crawl(AuthorsSpider)
    process.crawl(QuotesSpider)
    process.start()

    importtodb()
    
if __name__ == "__main__":
    main()