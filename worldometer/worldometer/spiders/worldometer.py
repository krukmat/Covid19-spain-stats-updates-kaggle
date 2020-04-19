import scrapy


class WorldometerSpider(scrapy.Spider):
    name = "worldometer"
    start_urls = [
        'https://www.worldometers.info/coronavirus/#countries'
    ]

    def evaluate_col(self, country, index):
        return country.css('td')[index].css('td::text').get()!=None and (country.css('td')[index].css('td::text').get()!=None and  country.css('td')[index].css('td::text').get().strip() != 'N/A' and country.css('td')[index].css('td::text').get().strip() !='')

    def parse(self, response):
        for country in response.xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[@style=""]'):
            yield {
                'name': country.css('td a::text').get(),
                'totalcases': float(country.css('td')[1].css('td::text').get().replace('"','').replace(',','')) if  self.evaluate_col(country, 1)  else 0,
                'newcases':float(country.css('td')[2].css('td::text').get().replace('"','').replace(',','')) if self.evaluate_col(country, 2) else 0,
                'totaldeath':float(country.css('td')[3].css('td::text').get().replace('"','').replace(',','')) if self.evaluate_col(country, 3)  else 0,
                'newdeath':float(country.css('td')[4].css('td::text').get().replace('"','').replace(',','')) if self.evaluate_col(country, 4) else 0,
                'totalrecovered':float(country.css('td')[5].css('td::text').get().replace('"','').replace(',','')) if self.evaluate_col(country, 5) else 0,
                'activecases':float(country.css('td')[6].css('td::text').get().replace('"','').replace(',','')) if self.evaluate_col(country, 6)  else 0,
                'criticalcases':float(country.css('td')[7].css('td::text').get().replace('"','').replace(',','')) if self.evaluate_col(country, 7)  else 0,
                'totaltests':float(country.css('td')[10].css('td::text').get().replace('"','').replace(',','')) if self.evaluate_col(country, 10) else 0,
                'totaltestsOver1M':float(country.css('td')[11].css('td::text').get().replace('"','').replace(',','')) if self.evaluate_col(country, 11) else 0,
            }