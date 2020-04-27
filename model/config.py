import locale
import os
from os import path

class Config:
    def __init__(self):
        self.__user_name = os.getlogin()
        self.__pc_default_language = locale.getdefaultlocale()[0]
        self.__user_folder_name = next(folder for folder in os.listdir('C:\\') if ('User' or 'Felhasználó') in folder)
        self.__default_db_path = f'C:\\{self.__user_folder_name}\\{self.__user_name}\\RMSystem'
        self.check_db_folder_exist()
        self.__default_sqlite_manager_path = r'C:\Program Files (x86)\SQLabs\SQLiteManager\SQLiteManager.exe'

    def check_db_folder_exist(self):
        if not path.exists(self.__default_db_path):
            os.makedirs(self.__default_db_path)

    def get_db_path(self):
        return self.__default_db_path
