import scrapy


class VotesSpider(scrapy.Spider):
    name = "votes"

    def start_requests(self):
        urls = ['https://old.reddit.com/r/cats/top/?sort=top&t=week']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        titles = self.__get_all_titles(response)
        scores = self.__get_all_scores(response)
        links = self.__get_all_links(response)

        print(titles)
        print(scores)
        print(links)

    def __get_all_titles(self, response):
        titles_xpath = response.xpath('//div//div//p//a[contains(@class, "title may-blank")]/text()')
        return [title_xpath.get() for title_xpath in titles_xpath]

    def __get_all_scores(self, response):
        scores_xpath = response.xpath('//div//div[@class="score likes"]/text()')
        return [score_xpath.get() for score_xpath in scores_xpath]

    def __get_all_links(self, response):
        links_xpath = response.xpath('//div//div//p//a[contains(@class, "title may-blank")]/@href')
        return [link_xpath.get() for link_xpath in links_xpath]
