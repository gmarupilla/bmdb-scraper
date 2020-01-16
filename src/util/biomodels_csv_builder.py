import csv

class BioModelsCSVBuilder:
    def __init__(self, model_info_dict):
        self.data_dict = model_info_dict

    def build_csv(self, filename: str):
        with open(filename,'w',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Mode Name','CPS', 'SEDML', 'Pub Med ID'])
            for model in self.data_dict.keys():
                writer.writerow([model, self.data_dict[model]['cps'], self.data_dict[model]['sedml'], self.data_dict[model]['pubMedId']])
            writer.writerow(['Total count:', len(self.data_dict.keys())])
