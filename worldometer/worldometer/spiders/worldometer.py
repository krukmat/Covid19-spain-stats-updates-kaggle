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
                'totalcases': float(country.css('td')[1].css('td::text').get().replace('"','').replace(',','')),
                'newcases':float(country.css('td')[2].css('td::text').get().replace('"','').replace(',','')),
                'totaldeath':float(country.css('td')[3].css('td::text').get().replace('"','').replace(',','')),
                'newdeath':float(country.css('td')[4].css('td::text').get().replace('"','').replace(',','')),
                'totalrecovered':float(country.css('td')[5].css('td::text').get().replace('"','').replace(',','')),
                'activecases':float(country.css('td')[6].css('td::text').get().replace('"','').replace(',','')),
                'criticalcases':float(country.css('td')[7].css('td::text').get().replace('"','').replace(',','')),
                'totaltests':float(country.css('td')[10].css('td::text').get().replace('"','').replace(',','')),
                'totaltestsOver1M':float(country.css('td')[11].css('td::text').get().replace('"','').replace(',','')),
            }