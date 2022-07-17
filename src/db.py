import sqlite3
import os
from .utils import BASE_DIR


class DBPipeline():
    DB_FILE = os.path.join(BASE_DIR, "db.sqlite3")

    def __init__(self) -> None:
        self.connection = sqlite3.connect(self.DB_FILE)
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute("""DROP TABLE IF EXISTS news_urls""")
        self.cursor.execute(
            """CREATE TABLE news_urls(url TEXT)"""
        )

    def save_url(self, urls: str):
        self.cursor.executemany(
            """INSERT INTO news_urls VALUES (?)""", urls
        )
        self.connection.commit()