import logging
from kafka import KafkaConsumer
import json
import sqlite3
import os

# Kafka configuration
KAFKA_BROKER = '127.0.0.1:9092'
TOPIC = 'your_topic'
GROUP_ID = 'your_group_id'

# Database configuration
DB_FILE = 'messages.db'

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Kafka Consumer
def create_consumer():
    consumer = KafkaConsumer(
        TOPIC,
        group_id=GROUP_ID,
        bootstrap_servers=KAFKA_BROKER,
        auto_offset_reset='earliest',
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )
    logger.info(f"Kafka consumer connected to {KAFKA_BROKER}")
    return consumer

# Store message in the SQLite database
def store_message_in_db(message):
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Ensure table exists
        cursor.execute('''CREATE TABLE IF NOT EXISTS messages
                          (category TEXT, sentiment_score REAL, message_length INTEGER)''')

        # Insert the data
        cursor.execute('''
            INSERT INTO messages (category, sentiment_score, message_length)
            VALUES (?, ?, ?)
        ''', (message['category'], message['sentiment_score'], message['message_length']))

        conn.commit()
        logger.info(f"Message stored: {message}")
    except Exception as e:
        logger.error(f"Error storing message in DB: {e}")
    finally:
        conn.close()

# Main loop to consume messages
def consume_messages():
    consumer = create_consumer()

    for message in consumer:
        try:
            # Get the message value
            message_value = message.value

            # Process the message and store in DB
            store_message_in_db(message_value)
        except Exception as e:
            logger.error(f"Error consuming message: {e}")

if __name__ == "__main__":
    consume_messages()