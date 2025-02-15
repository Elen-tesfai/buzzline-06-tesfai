"""
producer.py - Real-Time Data Streaming Producer to Kafka

This script simulates the real-time streaming of data by generating random messages
and sending them to a Kafka topic. Each message contains the following fields:
- timestamp: The time the message was generated.
- author: The author of the message.
- content: The content of the message (a simple trend description).
- category: The category of the message (e.g., Technology, Sports, etc.).
- sentiment_score: A randomly generated sentiment score ranging from -1 (negative) to 1 (positive).
- message_length: The length of the message content.

Kafka Configuration:
- Kafka server: 'localhost:9092'
- Kafka topic: 'trending_topics'

Dependencies:
- kafka-python: To interface with Kafka.
- json: To format data as JSON.
- random: To generate random message content.
- time: To simulate real-time streaming by adding delays.
- datetime: To generate the timestamp for each message.

Instructions:
1. Ensure Kafka is running on localhost:9092.
2. Install the necessary dependencies from the 'requirements.txt' file.
3. Run the script to start producing messages to the Kafka topic.

Created by: Elen Tesfai
"""
import json
import time
import random
from kafka import KafkaProducer
from datetime import datetime

# Configure the Kafka producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',  # Kafka server address
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Serialize data to JSON
)

# Define the Kafka topic
topic = 'trending_topics'

# Simulate real-time message streaming
def generate_message():
    categories = ['Technology', 'Sports', 'Health', 'Entertainment']
    authors = ['Author1', 'Author2', 'Author3']
    sentiments = ['positive', 'neutral', 'negative']
    
    # Sample data
    message = {
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'author': random.choice(authors),
        'content': f'Trending now in {random.choice(categories)}!',
        'category': random.choice(categories),
        'sentiment_score': random.uniform(-1, 1),  # Random sentiment score
        'message_length': random.randint(10, 200)
    }

    return message

def produce_messages():
    while True:
        message = generate_message()
        print(f"Sending message: {message}")
        producer.send(topic, message)
        time.sleep(2)  # Simulate message every 2 seconds

if __name__ == "__main__":
    try:
        print("Starting producer...")
        produce_messages()
    except KeyboardInterrupt:
        print("Producer stopped.")
    finally:
        producer.close()