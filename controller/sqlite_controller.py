import sqlite3 as sql

from PyQt5.QtWidgets import QMessageBox

from controller.config import Config


class SqliteController:
    def __init__(self):
        self.conn = None
        self.cursor = None
        default_config = Config()
        self.default_path = default_config.get_db_path()

        if self.default_path:
            self.open(self.default_path)
        else:
            QMessageBox(title='Configuration Error', text='Database path is missing!')

    def open(self, path):
        try:
            self.conn = sql.connect(path)
            self.cursor = self.conn.cursor()
        except sql.Error as e:
            QMessageBox(title='Sqlite Error', text=e)

    def create_table(self, table_name, columns):
        query = f'"""CREATE TABLE {table_name}({columns})"""'
        self.cursor.execute(query)

    def edit(self, edit_query):
        self.cursor.execute(edit_query)
        self.conn.commit()

    def select(self, selection_query):
        c = self.cursor.execute(selection_query)
        return c.fetchall()

    def insert_new_item(self, item_insert_query):
        self.cursor.execute(item_insert_query)
        self.conn.commit()

    def delete(self, delete_query):
        self.cursor.execute(delete_query)
        self.conn.commit()

    def insert_new_row(self, column_insert_query):
        self.cursor.execute(column_insert_query)
        self.conn.commit()
