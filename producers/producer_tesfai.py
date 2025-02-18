import json
import time
import random
import logging
from kafka import KafkaProducer
from utils.utils_config import KAFKA_BROKER, KAFKA_TOPIC
from datetime import datetime

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Example categories to simulate (replace with your own relevant categories)
CATEGORIES = ["category_1", "category_2", "category_3"]  # Replace with real categories you want to use

def generate_random_message():
    # Simulate generating a random message
    message = {
        "timestamp": datetime.utcnow().isoformat() + "Z",  # Current UTC timestamp
        "author": f"User{random.randint(1, 100)}",
        "content": f"Sample message content about {random.choice(CATEGORIES)}.",
        "category": random.choice(CATEGORIES),
        "sentiment_score": random.uniform(-1, 1),  # Random sentiment between -1 and 1
        "message_length": random.randint(50, 200)  # Random message length
    }
    return message

def create_producer():
    # Create Kafka producer
    producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER,
                             value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    return producer

def send_messages(producer):
    # Simulate real-time message generation and sending
    while True:
        message = generate_random_message()
        logger.info(f"Sending message: {message}")
        producer.send(KAFKA_TOPIC, value=message)
        time.sleep(1)  # Send every 1 second (you can adjust this)

def main():
    # Create producer and start sending messages
    producer = create_producer()
    send_messages(producer)
    producer.close()

if __name__ == "__main__":
    main()