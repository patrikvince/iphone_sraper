import pandas as pd
from datetime import datetime

class MakeExcel():
    def __init__(self, path, dictionary=None, data_frame=None, header=None):
        self.path = path
        self.dictionary = dictionary
        self.data_frame = data_frame
        self.header = header

    def df_to_excel(self, data_frame=None, header=None):
        try:
            if data_frame is None:
                raise ValueError("Data frame cannot be None")
            if header is None:
                raise ValueError("Header cannot be None") 
            if not self.path.endswith('.csv'):
                raise ValueError("The file path must end with .csv")
        except ValueError as ve:
            print(ve)
            return
        self.data_frame = data_frame
        self.header = header
        data_frame.to_csv(self.path, sep=';', index=False, header=header)
        print(f"Data saved to {self.path}")

        

        
        