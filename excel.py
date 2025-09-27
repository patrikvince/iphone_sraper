import os
import pandas as pd
from datetime import datetime

class MakeExcel():
    def __init__(self, path, dictionary=None, data_frame=None, header=None):
        self.path = path
        self.dictionary = dictionary
        self.data_frame = data_frame
        self.header = header

    def df_to_excel(self, data_frame=None, header=None):
        if os.path.exists(self.path):
            self.update_excel(data_frame=data_frame, header=header)
        else:

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


    def update_excel(self, data_frame=None, header=None):
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

        existing_df = pd.read_csv(self.path, sep=';')
        merged_df = pd.merge(existing_df, data_frame, how='outer')
        merged_df.to_csv(self.path, sep=';', index=False)
        print(f"Data updated in {self.path}")