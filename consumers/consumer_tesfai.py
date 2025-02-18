import logging
import time
import matplotlib.pyplot as plt
from kafka import KafkaConsumer
import json
from utils.utils_config import KAFKA_BROKER, KAFKA_TOPIC  # Ensure you import the right values

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
    retries = 5  # Max number of retries
    for attempt in range(retries):
        try:
            consumer = KafkaConsumer(
                KAFKA_TOPIC,  # Kafka topic to consume messages from
                bootstrap_servers=KAFKA_BROKER,  # Kafka broker address
                value_deserializer=lambda x: json.loads(x.decode('utf-8')),  # Deserializer for messages
                group_id='test_group'  # Consumer group ID
            )
            logger.info(f'Kafka consumer created successfully. Connected to {KAFKA_BROKER}.')
            return consumer
        except Exception as e:
            logger.error(f'Error creating Kafka consumer: {e}. Retrying... ({attempt + 1}/{retries})')
            time.sleep(5)  # Wait before retrying
    logger.error('Max retries reached. Could not connect to Kafka broker.')
    raise Exception("Kafka broker connection failed.")

# Step 3: Function to consume messages from Kafka topic
def consume_messages(consumer):
    logger = create_logger()  # Get the logger instance
    logger.info('Starting message consumption...')
    
    sentiment_scores = []  # Store sentiment scores for visualization
    message_lengths = []  # Store message lengths for visualization
    
    try:
        for message in consumer:
            logger.info(f'Received message: {message.value}')
            
            # Extract sentiment_score and message_length from the message
            sentiment_score = message.value.get('sentiment_score')
            message_length = message.value.get('message_length')
            
            if sentiment_score is not None:
                sentiment_scores.append(sentiment_score)
            if message_length is not None:
                message_lengths.append(message_length)

            # Optionally, you can trigger the plot display every n messages
            if len(sentiment_scores) % 10 == 0:  # Update every 10 messages
                plot_data(sentiment_scores, message_lengths)

    except Exception as e:
        logger.error(f'Error consuming message: {e}')
    finally:
        consumer.close()  # Close the consumer gracefully
        logger.info('Consumer closed gracefully.')

# Step 4: Function to plot bar charts for sentiment scores and message lengths
def plot_data(sentiment_scores, message_lengths):
    logger = create_logger()

    # Scale sentiment scores to make them more visible
    max_message_length = max(message_lengths) if message_lengths else 1
    sentiment_scaling_factor = max_message_length / max(sentiment_scores) if sentiment_scores else 1

    scaled_sentiment_scores = [score * sentiment_scaling_factor for score in sentiment_scores]

    # Create a bar chart to visualize sentiment scores and message lengths
    plt.figure(figsize=(10, 6))
    
    # Adjust the width of the bars so they don't overlap
    bar_width = 0.6  # Width of bars
    x_sentiment = range(len(scaled_sentiment_scores))  # x-values for sentiment scores
    x_lengths = [x + bar_width for x in x_sentiment]  # x-values for message lengths (shifted to the right)

    # Plotting sentiment scores (blue bars)
    plt.bar(x_sentiment, scaled_sentiment_scores, width=bar_width, color='blue', alpha=0.7, label='Sentiment Scores')

    # Plotting message lengths (green bars)
    plt.bar(x_lengths, message_lengths, width=bar_width, color='green', alpha=0.7, label='Message Lengths')
    
    # Adding labels and title
    plt.xlabel('Messages')  # X-axis label
    plt.ylabel('Values')  # Y-axis label
    plt.title('Sentiment Scores and Message Lengths')  # Title

    # Adding a legend
    plt.legend()

    # Show the plot
    plt.tight_layout()
    plt.show()

# Step 5: Main function to run the consumer
def main():
    logger = create_logger()

    # Create Kafka consumer (you can add your Kafka consumption logic here)
    consumer = create_consumer()

    # Consume messages from the Kafka topic
    consume_messages(consumer)

if __name__ == "__main__":
    main()