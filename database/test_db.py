import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import datetime

from database.conversation_db import ConversationDB

db = ConversationDB()

db.save_conversation(
    timestamp=str(datetime.datetime.now()),
    message="How much PPF for Jetour T2",
    service="PPF",
    vehicle="Jetour T2",
    phase="Phase3",
    response="We offer two PPF options..."
)

db.show_all()
