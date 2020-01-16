import requests
from config import Config
from bs4 import BeautifulSoup
import re
from util import SeleniumDispatcher
from selenium.webdriver.common.keys import Keys




class BioModelsInfoScraper:
    def __init__(self):
        self.models = None
        self.model_list = None

    def generate_biomodels_list(self):
        model_list = list()
        for counter in range(Config.MODEL_ID_START, Config.MODEL_ID_END + 1):
            if counter not in Config.MODEL_ID_EXCLUDE:
                counter_str = str(counter)
                if len(counter_str) == 3:
                    model_list.append(Config.BASE_MODEL_IDENTIFIER + counter_str)
                else:
                    num_zeroes = 3 - len(counter_str)
                    zeros = ''
                    for zero_count in range(0,num_zeroes):
                        zeros = zeros + '0'
                    counter_str = zeros + counter_str
                    model_list.append(Config.BASE_MODEL_IDENTIFIER + counter_str)
        self.model_list = model_list
        return model_list


    def scrape_data(self):

        # selenium = SeleniumDispatcher(headless=False, selenium_wire=True)
        # driver = selenium.get_driver()
        # driver.get('https://www.ebi.ac.uk/biomodels/BIOMD0000000001')
        # username_elem = driver.find_element_by_xpath("//input[@id='username']")
        # password_elem = driver.find_element_by_xpath("//input[@id='password']")
        # password_elem.send_keys(Keys.ENTER)
        # driver.get('https://www.ebi.ac.uk/biomodels/search?query=*%3A*%20AND%20curationstatus%3A%22Manually%20curated%22&domain=biomodels&offset=0&numResults=10')
        # driver.find_element_by_xpath("//a[@href='/biomodels/BIOMD0000000740']").click()
        # driver.get('https://www.ebi.ac.uk/biomodels/BIOMD00000000001')

        self.models = dict()
        for model_name in self.model_list:
            self.models[model_name] = dict()
            url = Config.BASE_URL + model_name
            res = requests.get(url, headers=Config.HEADERS)
            soup = BeautifulSoup(res.content, 'html.parser')
            # selenium = SeleniumDispatcher(headless=False, selenium_wire=True)
            # driver = selenium.get_driver()
            # driver.get(url)
            # username_elem = driver.find_element_by_xpath("//input[@id='username']")
            # username_elem.send_keys('gmarupilla')
            # password_elem = driver.find_element_by_xpath("//input[@id='password']")
            # password_elem.send_keys('TGMEF5')
            # password_elem.send_keys(Keys.ENTER)
            # selenium = SeleniumDispatcher(headless=False).get_driver()
            # selenium.get(url)
            
            # open('file.html', 'w').write(str(res.content))
            self.get_and_save_file_info(soup, model_name)
            self.get_and_save_pubmed_id(soup, model_name)
            print(model_name)
            
    def get_and_save_pubmed_id(self, soup, model_name):
        item = soup.find('abbr', text='isDescribedBy')
        pub_id = item.parent.find_next('div').a.get_text()
        
        # available_finds = soup.find(text=re.compile('PubMed ID'))
        # pubmed_id = available_finds.split(':')[-1]
        # pubmed_id = re.findall(r'\d+', pubmed_id)[0]
        pubmed_id = pub_id
        self.models[model_name]['pubMedId'] = pubmed_id

    def get_and_save_file_info(self, soup, model_name):
        # Get description
        item = soup.find('td', text=model_name+'_url.xml')
        if item is not None:
            item_desc = item.find_next('td').contents[0]
            self.models[model_name]['desc'] = item_desc

        # Check cps
        cps_results = soup.find('td', text=re.compile('.cps'))
        if cps_results is not None:
            cps_desc = cps_results.find_next('td').contents[0]
            self.models[model_name]['cps'] = cps_desc
        else:
            self.models[model_name]['cps'] = ''
        # Check sedml
        sedml_results = soup.find('td', text=re.compile('.sedml'))
        if sedml_results is not None:
            sedml_desc = sedml_results.find_next('td').contents[0]
            self.models[model_name]['sedml'] = sedml_desc
        else:
            self.models[model_name]['sedml'] = ''

        



    def get_scraped_data(self):
        pass