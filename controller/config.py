import locale
import os
from os import path


class Config:
    def __init__(self):
        self.user_name = os.getlogin()
        self.pc_default_language = locale.getdefaultlocale()[0]
        self.user_folder_name = next(folder for folder in os.listdir('C:\\') if ('User' or 'Felhasználó') in folder)
        self.default_db_path = f'C:\\{self.user_folder_name}\\{self.user_name}\\RMSystem\\rmsystem.db'
        self.db_actual_path = None
        self.check_db_folder_exist()

    def check_db_folder_exist(self):
        if path.exists(self.default_db_path):
            self.db_actual_path = self.default_db_path
        else:
            self.db_actual_path = r'C:\\'

    def get_db_path(self):
        return self.db_actual_path
