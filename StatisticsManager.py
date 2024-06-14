import sqlite3


class StatisticsManager:
    def __init__(self, db_name="bd.db"):
        self.db_name = db_name
        self.init_db()

    def init_db(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS statistics (
                            id INTEGER PRIMARY KEY,
                            user_id INTEGER,
                            cpm REAL,
                            wpm REAL,
                            errors INTEGER,
                            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                          )''')
        conn.commit()
        conn.close()

    def record_statistics(self, user_id, cpm, wpm, errors):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO statistics (user_id, cpm, wpm, errors)
                          VALUES (?, ?, ?, ?)''', (user_id, cpm, wpm, errors))
        conn.commit()
        conn.close()

    def fetch_statistics(self, user_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''SELECT cpm, wpm, errors, timestamp FROM statistics WHERE user_id = ?''', (user_id,))
        results = cursor.fetchall()
        conn.close()
        return results
