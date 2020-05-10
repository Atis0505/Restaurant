import os
import sqlite3 as sql
from enum import Enum
from typing import List, Optional, Dict

from model.config import Config
from model.default_database import InitSqlCommands
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
        self.message_box = Messagebox()
        if self.__db_path:
            self.__open(self.__db_path)
        else:
            self.message_box.window_execution('Database path is missing!', MessageBoxType.ERROR)

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
            self.message_box.window_execution(f'Hiba az adatbázisban\n{e}!', MessageBoxType.ERROR)

    def __create_default_db(self):
        for command in InitSqlCommands:
            self.cursor.execute(command.value)
            self.__conn.commit()
        admin_params = ('Admin', '12345')
        self.cursor.execute("INSERT INTO User (UserName, Password) VALUES (?,?)", admin_params)
        self.__conn.commit()

    def execute_command(self, operation: Operation, main_table_name: str, column_names: List[str] = None,
                        where_condition: Dict[str, str] = None, order_by: str = None,
                        insertion_value_dict: Dict[str, str] = None, update_value_dict: Dict[str, str] = None,
                        set_delete_id: int = None) -> List[str]:
        try:
            if operation is Operation.SELECT:
                if column_names:
                    column_name_string = ", ".join([column for column in column_names])
                else:
                    column_name_string = '*'
                if where_condition:
                    where_condition_string = " WHERE "
                    flag = len(where_condition) - 1
                    for key, value in where_condition.items():
                        where_condition_string += f"{key} = '{value}'"
                        if flag:
                            where_condition_string += " AND "
                        flag -= 1
                else:
                    where_condition_string = ''
                if order_by:
                    order_by_string = f" ORDER BY {order_by}"
                else:
                    order_by_string = ''
                select_query_string = f"SELECT {column_name_string} FROM {main_table_name}{where_condition_string}{order_by_string}"
                print(select_query_string)
                c = self.cursor.execute(select_query_string)
                rows = c.fetchall()
                return rows
            elif operation is Operation.INSERT:
                insertion_columns_string = ', '.join([key for key in insertion_value_dict.keys()])
                insert_query_string = f"INSERT INTO {main_table_name} ({insertion_columns_string}) VALUES ({', '.join([' ?'] * len(insertion_value_dict.keys()))})"
                print(insert_query_string)
                self.cursor.execute(insert_query_string, tuple([value for value in insertion_value_dict.values()]))
                self.__conn.commit()
            elif operation is Operation.UPDATE:
                for key, value in update_value_dict.items():
                    update_query_string = f"UPDATE {main_table_name} SET {key} = '{value}' WHERE {main_table_name + 'ID'} = '{str(set_delete_id)}'"
                    self.__conn.commit()
            elif operation is Operation.DELETE:
                delete_query_string = f"DELETE FROM {main_table_name} WHERE {main_table_name + 'ID'} = '{str(set_delete_id)}'"
                self.__conn.commit()
        except sql.Error as e:
            self.message_box.window_execution(f'Operation hiba!\n{e}', MessageBoxType.ERROR)

    def execute_command_2(self, operation: Operation, table_name: str, datas: List[Dict[str, str]]) -> Optional[
        List[str]]:
        try:
            if operation is Operation.INSERT:
                columns_srting = ', '.join([key for key in datas[0].keys()])
                query = f"INSERT INTO {table_name} ({columns_srting}) VALUES ({', '.join([' ?'] * len(datas[0]))})"
                self.cursor.execute(query, tuple([value for value in datas[0].values()]))
            elif operation is Operation.SELECT:
                column_string = "*"
                condition_string = ''
                for data in datas:
                    if type(data) is list:
                        column_string = ", ".join([column for column in data])
                    if type(data) is dict:
                        condition_string = f" WHERE "
                        flag = len(data) - 1
                        for key, value in data.items():
                            condition_string += f"{key} = '{value}'"
                            if flag:
                                condition_string += " AND "
                            flag -= 1
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
            self.message_box.window_execution(f'Operation hiba!\n{e}', MessageBoxType.ERROR)
        # self.__close_db()

    def __close_db(self):
        self.__conn.commit()
        self.__conn.close()
