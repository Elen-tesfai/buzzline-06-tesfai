"""
consumer.py - Real-Time Data Consumer and Sentiment Analyzer

This script consumes messages from a Kafka topic, processes the data to analyze sentiment scores,
and visualizes the results using graphs. It tracks message counts and sentiment trends across categories.

Kafka Configuration:
- Kafka server: 'localhost:9092'
- Kafka topic: 'trending_topics'

Dependencies:
- kafka-python: To interface with Kafka and consume messages.
- json: To parse messages from Kafka.
- matplotlib: To visualize sentiment analysis and message counts.
- time: To simulate real-time processing by adding delays.
- sqlite3: For storing processed data.
- pandas: For managing the processed data in DataFrames.
- seaborn: For enhanced data visualization.

Instructions:
1. Ensure Kafka is running on localhost:9092.
2. Install the necessary dependencies from the 'requirements.txt' file.
3. Run the script to start consuming messages and visualizing sentiment analysis.

Created by: Elen Tesfai
"""

import json
import time
from kafka import KafkaConsumer
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
import pandas as pd

# Configure the Kafka consumer
consumer = KafkaConsumer(
    'trending_topics',
    bootstrap_servers='localhost:9092',  # Kafka server configuration
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))  # Deserialize the message
)

# Set up the database connection (SQLite)
conn = sqlite3.connect('sentiment_analysis.db')
cursor = conn.cursor()

# Create the necessary table for storing sentiment data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sentiment_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        author TEXT,
        category TEXT,
        sentiment_score REAL,
        message_length INTEGER
    )
''')
conn.commit()

# Function to insert data into the SQLite database
def insert_data(message):
    cursor.execute('''
        INSERT INTO sentiment_data (timestamp, author, category, sentiment_score, message_length)
        VALUES (?, ?, ?, ?, ?)
    ''', (message['timestamp'], message['author'], message['category'], message['sentiment_score'], message['message_length']))
    conn.commit()

# Function to process the messages and analyze sentiment
def analyze_sentiment():
    message_count = {'positive': 0, 'neutral': 0, 'negative': 0}
    while True:
        for message in consumer:
            data = message.value
            sentiment_score = data['sentiment_score']
            category = data['category']

            # Analyze sentiment
            if sentiment_score > 0:
                sentiment = 'positive'
                message_count['positive'] += 1
            elif sentiment_score < 0:
                sentiment = 'negative'
                message_count['negative'] += 1
            else:
                sentiment = 'neutral'
                message_count['neutral'] += 1

            # Insert data into database
            insert_data(data)

            # Visualize the sentiment trends
            print(f"Message: {data['content']} | Sentiment: {sentiment}")
            visualize_sentiment(message_count)

            time.sleep(1)  # Simulate processing delay

# Function to visualize sentiment trends
def visualize_sentiment(message_count):
    plt.clf()  # Clear the figure
    sentiment_labels = ['Positive', 'Neutral', 'Negative']
    sentiment_values = [message_count['positive'], message_count['neutral'], message_count['negative']]

    # Create a bar chart for sentiment distribution
    sns.barplot(x=sentiment_labels, y=sentiment_values, palette='viridis')
    plt.title("Sentiment Analysis Distribution")
    plt.xlabel("Sentiment")
    plt.ylabel("Message Count")
    plt.show()

if __name__ == "__main__":
    try:
        print("Starting consumer and sentiment analysis...")
        analyze_sentiment()
    except KeyboardInterrupt:
        print("Consumer stopped.")
    finally:
        conn.close()