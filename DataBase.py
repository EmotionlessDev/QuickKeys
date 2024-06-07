import sqlite3


class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        self.cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_name} ({columns})')
        self.conn.commit()

    def insert_data(self, table_name, data):
        self.cursor.execute(f'INSERT INTO {table_name} VALUES ({",".join(["?"] * len(data))})', data)
        self.conn.commit()

    def fetch_data(self, table_name):
        self.cursor.execute(f'SELECT * FROM {table_name}')
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.conn.close()