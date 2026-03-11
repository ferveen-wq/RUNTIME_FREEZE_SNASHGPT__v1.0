import sqlite3


class ConversationDB:

    def __init__(self):

        self.conn = sqlite3.connect("snash_conversations.db")
        self.cursor = self.conn.cursor()

        self.create_tables()

    def create_tables(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversations (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            timestamp TEXT,
            customer_message TEXT,
            detected_service TEXT,
            detected_vehicle TEXT,
            phase TEXT,
            response TEXT

        )
        """)

        self.conn.commit()

    def save_conversation(self,
                          timestamp,
                          message,
                          service,
                          vehicle,
                          phase,
                          response):

        self.cursor.execute("""

        INSERT INTO conversations
        (timestamp, customer_message, detected_service,
        detected_vehicle, phase, response)

        VALUES (?, ?, ?, ?, ?, ?)

        """, (timestamp, message, service, vehicle, phase, response))

        self.conn.commit()

    def show_all(self):

        for row in self.cursor.execute("SELECT * FROM conversations"):
            print(row)
