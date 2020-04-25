import os
import sqlite3 as sql
from enum import Enum
from typing import List, Optional

from controller.config import Config
from controller.default_database import InitSqlCommands
from view.messagebox_window_class import Messagebox, MessageBoxType


class Operation(Enum):
    SELECT = 0
    DELETE = 1
    UPDATE = 2
    INSERT = 3


class SqliteController:
    def __init__(self):
        config = Config()
        self.__db_path = config.get_db_path() + r'\RMsystem.db'
        self.__conn = None
        self.cursor = None
        if self.__db_path:
            self.__open(self.__db_path)
        else:
            Messagebox('Database path is missing!', MessageBoxType.ERROR)

    def __open(self, path):
        try:
            if os.path.isfile(self.__db_path):
                self.__conn = sql.connect(self.__db_path)
                self.cursor = self.__conn.cursor()
            else:
                self.__conn = sql.connect(self.__db_path)
                self.cursor = self.__conn.cursor()
                self.__create_default_db()
        except sql.Error as e:
            Messagebox(f'Hiba az adatbázisban\n{e}!', MessageBoxType.ERROR)

    def __create_default_db(self):
        for command in InitSqlCommands:
            self.cursor.execute(command.value)
            self.__conn.commit()
        admin_params = ('Admin', '12345')
        self.cursor.execute("INSERT INTO User (UserName, Password) VALUES (?,?)", admin_params)
        self.__conn.commit()

    def execute_command(self, operation: Operation, table_name: str, datas) -> Optional[List[str]]:
        try:
            if operation is Operation.INSERT:
                values_string = ', '.join(value if type(value) is not str else f"'{value}'" for value in datas)
                query = f"INSERT INTO {table_name} ({', '.join(['?'] * len(datas))}) VALUES ({values_string})"
                self.cursor.execute(query)
            elif operation is Operation.SELECT:
                column_string = "*"
                condition_string = ''
                for data in datas:
                    if type(data) is list:
                        column_string = ", ".join([column for column in data])
                    if type(data) is dict:
                        condition_string = f" WHERE "
                        first_flag = True
                        for key, value in data.items():
                            condition_string += f"{key} = '{value}'"
                            if first_flag:
                                condition_string += " AND "
                            first_flag = False
                query = f"SELECT {column_string} FROM {table_name}{condition_string}"
                print(query)
                c = self.cursor.execute(query)
                rows = c.fetchall()
                return rows
            elif operation is Operation.UPDATE:
                query = f"UPDATE {table_name} SET {datas[0]} = {datas[1]} WHERE {table_name + 'ID'} = {datas[2]}"
                self.cursor.execute(query)
            elif operation is Operation.DELETE:
                query = f"DELETE FROM {table_name} WHERE {table_name + 'ID'} = {datas[0]}"
        except sql.Error as e:
            Messagebox('Operation hiba!\n{e}', MessageBoxType.ERROR)
        self.__close_db()

    def __close_db(self):
        self.__conn.commit()
        self.__conn.close()
