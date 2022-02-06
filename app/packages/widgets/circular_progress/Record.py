import datetime
from directory import BASE_DIR
import pandas as pd
import openpyxl
import os
import datetime
import numpy as np

file_name = 'record.xlsx'
file_dir = os.path.join(BASE_DIR,'data',file_name)
columns = ['Date', 'Pomo', 'Task', 'Start', 'Duration']
class Record:
    def __init__(self):
        if not os.path.exists(file_dir):
            print("file does not exists. create one.")
            self.create_excel()
        else:
            self.df = pd.read_excel(file_dir)
            self._initiate()
            print(self.df)


    def _initiate(self, pomo, task):
        today = pd.to_datetime('today').replace(hour=0, minute=0, second=0, microsecond=0)
        start = pd.to_datetime('today').time().replace(microsecond=0)

        self.row = [today,np.nan, np.nan, start, np.nan]




    def create_excel(self, overwrite=False):
        self.df = pd.DataFrame()
        if not os.path.exists(file_dir) or overwrite:
            self.df.to_excel(file_dir, index=False)
            print('-----file created-----')
        else:
            print('file exists')










if __name__ == '__main__':
    Pomo = Record()

    print(today)


