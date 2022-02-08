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
        self.pomo = np.nan
        self.task = np.nan
        self.duration = np.nan
        self.state = 0



    def start_record(self):

        print(self.pomo, 'starts recording')

        today = pd.to_datetime('today').replace(hour=0, minute=0, second=0, microsecond=0)
        start = pd.to_datetime('today').time().replace(microsecond=0)

        self.row = [today, self.pomo, np.nan, start, np.nan]
        self.state = 1

    def end_record(self):
        print(self.pomo, 'stops recording')

        hour = self.duration // 3600
        minutes = (self.duration - hour * 3600) // 60
        seconds = self.duration - hour * 3600 - (minutes * 60)
        time_string = "{:02}:{:02}:{:02}".format(int(hour), int(minutes), int(seconds))

        self.row[2] = self.task
        self.row[4] = pd.to_datetime(time_string).time()

        self.state = 0

    def save_record(self):
        self.df = pd.read_excel(file_dir)
        row = pd.DataFrame([self.row],columns=columns)
        self.df = pd.concat((row,self.df), ignore_index=True)

        self.df.to_excel(file_dir, index=False)

        self.row = [np.nan, np.nan, np.nan, np.nan, np.nan]
        print(self.df)


    def create_excel(self, overwrite=False):
        self.df = pd.DataFrame()
        if not os.path.exists(file_dir) or overwrite:
            self.df.to_excel(file_dir, index=False)
            print('-----file created-----')
        else:
            print('file exists')



if __name__ == '__main__':
    Pomo = Record()



