import os
import sys


class Config:
    BASE_URL = 'https://www.ebi.ac.uk/biomodels/'
    BASE_MODEL_IDENTIFIER = 'BIOMD0000000'
    MODEL_ID_START = 1
    MODEL_ID_END = 831
    MODEL_ID_EXCLUDE = [649,694,701]
    HEADERS = {
        'Host': 'www.ebi.ac.uk',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Cache-Control': 'no-cache',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1'
        }
    DOWNLOAD_DIRECTORY = 'C:\\Users\\gmarupilla\\Downloads\\bmdb_scraper'
    SELENIUM_DRIVER_BASE_PATH = 'chromedriver'
    SELENIUM_DRIVER_CHROME_EXEC_PATH = \
        os.path.join(SELENIUM_DRIVER_BASE_PATH, 'chromedriver_'+sys.platform)
    SELENIUM_DRIVER_FIREFOX_EXEC_PATH = \
        os.path.join(SELENIUM_DRIVER_BASE_PATH, 'geckodriver_'+sys.platform)