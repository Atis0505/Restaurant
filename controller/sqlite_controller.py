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
    def __init__(self, operation, datas):
        config = Config()
        self.db_path = config.get_db_path() + r'\RMsystem.db'
        self.conn = None
        self.cursor = None
        self.operation = operation
        self.datas = datas
        if self.db_path:
            self.open(self.db_path)
        else:
            Messagebox('Database path is missing!', MessageBoxType.ERROR)

    def open(self, path):
        try:
            if os.path.isfile(self.db_path):
                self.conn = sql.connect(self.db_path)
                self.cursor = self.conn.cursor()
            else:
                self.conn = sql.connect(self.db_path)
                self.cursor = self.conn.cursor()
                self.create_default_db()
        except sql.Error as e:
            Messagebox(f'Hiba az adatbázisban\n{e}!', MessageBoxType.ERROR)

    def create_default_db(self):
        for command in InitSqlCommands:
            self.cursor.execute(command.value)
            self.conn.commit()
        admin_params = ('Admin', '12345')
        self.cursor.execute("INSERT INTO Users (UserName, Password) VALUES (?,?)", admin_params)
        self.conn.commit()

    def execute_command(self, operation: Operation, table_name: str, datas) -> Optional[List[str]]:
        if operation is Operation.INSERT:
            values_string = ', '.join(value if type(value) is not str else f"'{value}'" for value in datas)
            query = f"INSERT INTO {table_name} ({', '.join(['?'] * len(datas))}) VALUES ({values_string})"
            self.cursor.execute(query)
        elif operation is Operation.SELECT:
            column_string = '*'
            if datas:
                column_string = ', '.join([column for column in datas])
            query = f"SELECT {column_string} FROM {table_name}"
            return self.cursor.execute(query)
        elif operation is Operation.UPDATE:
            query = f"UPDATE {table_name} SET {datas[0]} = {datas[1]} WHERE {table_name + 'ID'} = {datas[2]}"
            self.cursor.execute(query)
        elif operation is Operation.DELETE:
            query = f"DELETE FROM {table_name} WHERE {table_name + 'ID'} = {datas[0]}"
        self.close_db()

    def close_db(self):
        self.conn.commit()
        self.conn.close()
