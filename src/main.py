from bio_models_scraper import BioModelsInfoScraper
from util import BioModelsCSVBuilder


bio_model_scraper = BioModelsInfoScraper()
bio_model_scraper.generate_biomodels_list()
bio_model_scraper.scrape_data()
BioModelsCSVBuilder(bio_model_scraper.models).build_csv('biomodel_info.csv')