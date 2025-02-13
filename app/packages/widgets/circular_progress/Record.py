import datetime
# from directory import BASE_DIR
import pandas as pd
import openpyxl
import os
import datetime
import numpy as np

BASE_DIR = os.getcwd()

file_name = 'record.csv'
file_dir = os.path.join(BASE_DIR,'data',file_name)
columns = ['Start', ' End', 'Pomo',  'Task']
class Record:
    def __init__(self):
        if not os.path.exists(file_dir):
            print("file does not exists. create one.")
            self.create_csv()

        self.pomo = np.nan
        self.task = ""
        self.duration = np.nan
        self.recording = False


    def start_record(self, pomo):
        if pomo == 1:
            pomo = 'focus'
            print(pomo, 'starts recording')

            start = pd.to_datetime('today').replace(microsecond=0)
            self.row = [start, np.nan, pomo, np.nan]

            self.recording = True
        elif pomo == 2:
            pomo = 'rest'


    def end_record(self, subtract_sec = 0):
        if self.recording == True:
            print('stops recording')

            end = pd.to_datetime('today').replace(microsecond=0)
            #subtract seconds

            end = end - datetime.timedelta(seconds = subtract_sec)

            self.row[1] = end
            self.row[3] = self.task

            self.recording = False
            self._save_record()

    def _save_record(self):
        self.df = pd.read_csv(file_dir)
        row = pd.DataFrame([self.row],columns=columns)
        self.df = pd.concat((row,self.df), ignore_index=True)

        self.df.to_csv(file_dir, index=False)

        self.row = [np.nan, np.nan, np.nan, np.nan]
        print(self.df.iloc[:1])


    def create_csv(self, overwrite=False):
        data_dir = os.path.join(BASE_DIR,"data")
        if not os.path.exists(data_dir):
            os.mkdir(data_dir)
        self.df = pd.DataFrame(columns=columns)
        self.df.to_csv(file_dir, index=False)
        print('-----file created-----')

    # def check_empty(self):




if __name__ == '__main__':
    Pomo = Record()



