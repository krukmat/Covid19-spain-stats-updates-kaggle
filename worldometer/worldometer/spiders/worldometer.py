import scrapy


class WorldometerSpider(scrapy.Spider):
    name = "worldometer"
    start_urls = [
        'https://www.worldometers.info/coronavirus/#countries'
    ]

    def parse(self, response):
        for country in response.xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[@style=""]'):
            yield {
                'name': country.css('td a::text').get(),
                'totalcases': country.css('td')[1].css('td::text').get(),
                'newcases':country.css('td')[2].css('td::text').get(),
                'totaldeath':country.css('td')[3].css('td::text').get(),
                'newdeath':country.css('td')[4].css('td::text').get(),
                'totalrecovered':country.css('td')[5].css('td::text').get(),
                'activecases':country.css('td')[6].css('td::text').get(),
            }