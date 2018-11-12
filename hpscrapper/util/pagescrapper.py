import requests

class PageScrapper: 
    def get_url_data(self, url=''):
        r = requests.get(url).text
        return r