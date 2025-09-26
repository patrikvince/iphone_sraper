import os
from settings import ScraperSettings
from scraper import IPhoneScraper
from excel import MakeExcel
from dotenv import load_dotenv
import pandas as pd


def list_to_df(list: list):
    df = pd.DataFrame(list)
    return df

if __name__ == "__main__":
    settings = ScraperSettings(user_agent="MyScraperBot/1.0", timeout=10)
    print(f"User Agent: {settings.user_agent}, Timeout: {settings.timeout}")
    scraper = IPhoneScraper(settings)

    links = scraper.paginate_links(url="https://www.arukereso.hu/mobiltelefon-c3277/apple/")

    names, prices = scraper.scrape(links=links)
    
    iphone_list = {'Name': [name for sublist in names for name in sublist],
               'Price': [price for sublist in prices for price in sublist]}

    df = list_to_df(iphone_list)
    
    load_dotenv()
    path = os.getenv("DOWNLOAD_PATH")

    MakeExcel(path=path).df_to_excel(data_frame=df, header=['Name', 'Price'])


    