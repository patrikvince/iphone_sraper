import os
from settings import ScraperSettings
from scraper import IPhoneScraper
from excel import MakeExcel
from dotenv import load_dotenv
import pandas as pd
from datetime import datetime 

if __name__ == "__main__":
    settings = ScraperSettings(user_agent="MyScraperBot/1.0", timeout=10)
    print(f"User Agent: {settings.user_agent}, Timeout: {settings.timeout}")
    scraper = IPhoneScraper(settings)
    load_dotenv()
    link_base = os.getenv("LINK_BASE")

    names, prices = scraper.scrape(link=link_base)

    df = pd.DataFrame()
    df["Name"] = [name for sublist in names for name in sublist]

    time = datetime.now().strftime("%m/%d/%Y")
    df[time] = [price for sublist in prices for price in sublist]

    load_dotenv()
    path = os.getenv("DOWNLOAD_PATH")

    MakeExcel(path=path).df_to_excel(data_frame=df, header=['Name', time])