import locale
import os
from os import path

class Config:
    def __init__(self):
        self.user_name = os.getlogin()
        self.pc_default_language = locale.getdefaultlocale()[0]
        self.user_folder_name = next(folder for folder in os.listdir('C:\\') if ('User' or 'Felhasználó') in folder)
        self.default_db_path = f'C:\\{self.user_folder_name}\\{self.user_name}\\RMSystem'
        self.check_db_folder_exist()
        self.default_sqlite_manager_path = r'C:\Program Files (x86)\SQLabs\SQLiteManager\SQLiteManager.exe'

    def check_db_folder_exist(self):
        if not path.exists(self.default_db_path):
            os.makedirs(self.default_db_path)

    def get_db_path(self):
        return self.default_db_path
