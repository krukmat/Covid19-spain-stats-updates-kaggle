import scrapy


class WorldometerSpider(scrapy.Spider):
    name = "worldometer"
    start_urls = [
        'https://www.worldometers.info/coronavirus/#countries'
    ]

    def _removeNonAscii(s): 
        return "".join(i for i in s if ord(i)<128)

    def evaluate_col(self, country, index):
        return country.css('td')[index].css('td::text').get()!=None and (country.css('td')[index].css('td::text').get()!=None and  country.css('td')[index].css('td::text').get().strip() != 'N/A' and country.css('td')[index].css('td::text').get().strip() !='')

    def parse(self, response):
        for country in response.xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[@style=""]'):
            yield {
                'name': _removeNonAscii(country.css('td a::text').get()),
                'totalcases': int(country.css('td')[1].css('td::text').get().replace('"','').replace(',','')) if  self.evaluate_col(country, 1)  else 0,
                'newcases':int(country.css('td')[2].css('td::text').get().replace('"','').replace(',','')) if self.evaluate_col(country, 2) else 0,
                'totaldeath':int(country.css('td')[3].css('td::text').get().replace('"','').replace(',','')) if self.evaluate_col(country, 3)  else 0,
                'newdeath':int(country.css('td')[4].css('td::text').get().replace('"','').replace(',','')) if self.evaluate_col(country, 4) else 0,
                'totalrecovered':int(country.css('td')[5].css('td::text').get().replace('"','').replace(',','')) if self.evaluate_col(country, 5) else 0,
                'activecases':int(country.css('td')[6].css('td::text').get().replace('"','').replace(',','')) if self.evaluate_col(country, 6)  else 0,
                'criticalcases':int(country.css('td')[7].css('td::text').get().replace('"','').replace(',','')) if self.evaluate_col(country, 7)  else 0,
                'totaltests':int(country.css('td')[10].css('td::text').get().replace('"','').replace(',','')) if self.evaluate_col(country, 10) else 0,
                'totaltestsOver1M':int(country.css('td')[11].css('td::text').get().replace('"','').replace(',','')) if self.evaluate_col(country, 11) else 0,
            }