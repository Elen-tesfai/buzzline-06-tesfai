import logging
from kafka import KafkaConsumer
import json
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import numpy as np

# Step 1: Create a logger for debugging purposes
def create_logger():
    logger = logging.getLogger(__name__)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger

# Step 2: Create Kafka consumer
def create_consumer():
    logger = create_logger()  # Get the logger instance
    logger.info('Creating Kafka consumer...')
    try:
        consumer = KafkaConsumer(
            'test_topic',  # Kafka topic to consume messages from
            bootstrap_servers='localhost:9092',  # Kafka broker address
            value_deserializer=lambda x: json.loads(x.decode('utf-8')),  # Deserializer for messages
            group_id='test_group'  # Consumer group ID
        )
        logger.info('Kafka consumer created successfully.')
        return consumer
    except Exception as e:
        logger.error(f'Error creating Kafka consumer: {e}')
        raise

# Step 3: Function to process and visualize messages from Kafka topic
def process_and_visualize_messages(consumer):
    logger = create_logger()  # Get the logger instance
    
    sentiment_scores = []  # List to hold sentiment scores
    categories = {}  # Dictionary to hold category counts
    
    try:
        logger.info('Starting message consumption...')
        for message in consumer:
            logger.info(f'Received message: {message.value}')
            
            # Process message: extract sentiment score and category
            sentiment_score = message.value.get('sentiment_score')
            category = message.value.get('category')

            # Collect data for visualization
            if sentiment_score is not None:
                sentiment_scores.append(sentiment_score)
            
            if category:
                categories[category] = categories.get(category, 0) + 1  # Count messages per category

            # Plot visualization after every 10 messages
            if len(sentiment_scores) >= 10:  # Plot after receiving a batch of 10 messages
                plot_sentiment_scores(sentiment_scores)  # Bar chart for sentiment scores
                plot_category_distribution(categories)   # Pie chart for category distribution
                sentiment_scores.clear()  # Clear for the next batch

    except Exception as e:
        logger.error(f'Error consuming message: {e}')

# Step 4: Function to plot sentiment scores (Bar Chart)
def plot_sentiment_scores(sentiment_scores):
    plt.figure(figsize=(10, 6))
    plt.hist(sentiment_scores, bins=10, color='blue', edgecolor='black')
    plt.title('Sentiment Scores Distribution')
    plt.xlabel('Sentiment Score')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

# Step 5: Function to plot category distribution (Pie Chart)
def plot_category_distribution(categories):
    categories_list = list(categories.items())
    labels = [cat[0] for cat in categories_list]
    values = [cat[1] for cat in categories_list]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig.update_layout(title='Category Distribution')
    fig.show()

# Step 6: Main function to run the consumer and visualize data
def main():
    logger = create_logger()
    
    # Create Kafka consumer
    consumer = create_consumer()
    
    # Process and visualize messages from the Kafka topic
    process_and_visualize_messages(consumer)

if __name__ == "__main__":
    main()