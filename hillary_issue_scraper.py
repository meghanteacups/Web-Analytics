import scrapy
from scrapy.crawler import CrawlerProcess

class HillaryIssueScraper(scrapy.Spider):
    """ scrape the text from the issues sub-pages for Hillary
    start at this page: https://www.hillaryclinton.com/issues/ """
    name = "HillaryIssueScraper"
    start_urls = ["https://www.hillaryclinton.com/issues/"]

    def parse(self, response):
        # find the issue type and the links to the sub-pages
        # no useful structure or formatting; need to count by p-style lines
        # the title [0] and subtitle [1] are the issue details
        # the link is [2]
        issue = None
        stance = None
        for index,p in enumerate(response.css('div.rich-text p[style]')):
            if index % 3 == 0:
                issue = p.css('::text').extract()[0]
            if index % 3 == 1:
                stance = p.css('::text').extract()[0]
            if index % 3 ==2:
                href = p.css('a::attr(href)').extract()[0]
                yield scrapy.Request(href, callback=self.parse_issues, meta = {"issue": issue, "stance": stance})

    def parse_issues(self, response):
        # get the policy statement from the sub-pages and the header/topic
        policy_goal = response.css("div.p-content p ::text")
        policy_goal_text = "\n".join(t.strip() for t in policy_goal.extract() if t.strip())
        yield {'issue': response.request.meta["issue"], 'stance': response.request.meta["stance"], "policy": policy_goal_text}

def main():
    crawlerProcess = CrawlerProcess()
    crawlerProcess.crawl(HillaryIssueScraper)
    crawlerProcess.start()


if __name__ == "__main__":
    main()

