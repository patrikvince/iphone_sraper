import requests
from bs4 import BeautifulSoup

class IPhoneScraper:
    def __init__(self, settings):
        self.settings = settings

    def paginate_links(self, url: str):
        req = requests.get(url, timeout=self.settings.timeout, headers={'User-Agent': self.settings.user_agent})
        req.raise_for_status()
        
        soup = BeautifulSoup(req.text, 'html.parser')
        pag_class = soup.find_all("div", { "class": "pagination hidden-xs"})

        links = []
        for page in pag_class:
            pages = page.find_all("a")
            for p in pages:
                links.append(p.get('href'))
        
        return links[:-1]
    

    def scrape(self, links: list):
        names = []
        prices = []

        for link in links:
            req = requests.get(link, timeout=self.settings.timeout, headers={'User-Agent': self.settings.user_agent})
            req.raise_for_status()
            
            soup = BeautifulSoup(req.text, 'html.parser')
            
            names.append(self.IphoneNames(soup))
            prices.append(self.IphonePrices(soup))

        return names, prices


    def IphoneNames(self, soup: BeautifulSoup):
        names = []
        name_divs = soup.find_all('div', {'class': 'name ulined-link'})
    
        for name in name_divs:
            name = name.text
            name = name.replace('Apple ', '')
            name = name.replace(' Mobiltelefon', '')
            names.append(name.strip())
    
        return names
    

    def IphonePrices(self, soup: BeautifulSoup):
        prices = []
        price_divs = soup.find_all('div', {'class': 'price'})
       
        for price in price_divs:
            price = price.text
            price = price.replace(' Ft-tól', '')
            price = price.replace(' ', '')
            prices.append(price.strip())
        
        return prices