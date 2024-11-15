import sqlite3


class DatabaseManager:
    def __init__(self, db_path="payloads.db"):
        """
        Initializes the database manager.
        :param db_path: Path to the SQLite database file.
        """
        self.db_path = db_path
        self._create_table()

    def _create_table(self):
        """
        Creates the payloads table if it doesn't exist.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS payloads (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    topic TEXT NOT NULL,
                    payload TEXT NOT NULL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()

    def save_payload(self, topic, payload):
        """
        Saves a payload to the database.
        :param topic: MQTT topic of the payload.
        :param payload: Standardized payload as a JSON string.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO payloads (topic, payload)
                VALUES (?, ?)
            """, (topic, payload))
            conn.commit()
