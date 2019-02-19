import scrapy


class VotesSpider(scrapy.Spider):
    name = "votes"

    def __init__(self, *args, **kwargs):
        subs_concat = kwargs.pop('subs', [])

        if subs_concat:
            subs = subs_concat.split(',')

        self.urls = ["https://old.reddit.com/r/" + sub + "/top?sort=top&t=week" for sub in subs]

        print(self.urls)

        super(VotesSpider, self).__init__(*args, **kwargs)

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        titles = self.__get_all_titles(response)
        scores = self.__get_all_scores(response)
        links = self.__get_all_links(response)


        for i in range(0, len(scores)):
            if int(scores[i]) >= 5000:
                print(titles[i])
                print(scores[i])
                print(links[i])
                print(" ")

    def __get_all_titles(self, response):
        titles_xpath = response.xpath('//div//div//p//a[contains(@class, "title may-blank")]/text()')
        return [title_xpath.get() for title_xpath in titles_xpath]

    def __get_all_scores(self, response):
        scores_xpath = response.xpath('//div//div[@class="score likes"]')
        return [score_xpath.xpath("@title").get() for score_xpath in scores_xpath]

    def __get_all_links(self, response):
        links_xpath = response.xpath('//div//div//div//div//p//a[contains(@class, "title may-blank")]/@href')
        return [link_xpath.get() for link_xpath in links_xpath]
