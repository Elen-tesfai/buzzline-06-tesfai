import json
import os
from kafka import KafkaConsumer
from dotenv import load_dotenv
from utils.utils_logger import logger

# Load environment variables from .env file
load_dotenv()

# Function to get Kafka configuration from environment variables
def get_kafka_topic() -> str:
    return os.getenv("PROJECT_TOPIC", "buzzline-topic")

def get_kafka_server() -> str:
    return os.getenv("KAFKA_SERVER", "localhost:9092")

# Function to create Kafka consumer
def create_consumer():
    kafka_server = get_kafka_server()
    topic = get_kafka_topic()
    
    try:
        consumer = KafkaConsumer(
            topic,
            bootstrap_servers=kafka_server,
            value_deserializer=lambda x: json.loads(x.decode("utf-8")),
            group_id="buzzline-consumer-group"  # Unique group ID for this consumer
        )
        logger.info(f"Kafka consumer connected to {kafka_server} for topic {topic}")
        return consumer
    except Exception as e:
        logger.error(f"Failed to connect to Kafka: {e}")
        return None

# Function to consume and process messages
def consume_messages():
    consumer = create_consumer()
    if not consumer:
        logger.error("Kafka consumer not created. Exiting.")
        return

    try:
        for message in consumer:
            # Log the message consumed
            logger.info(f"Received message: {message.value}")
            
            # You can add specific processing logic here for your project
            process_message(message.value)

    except KeyboardInterrupt:
        logger.warning("Consumer interrupted by user.")
    except Exception as e:
        logger.error(f"Error while consuming message: {e}")
    finally:
        consumer.close()
        logger.info("Kafka consumer closed.")

# Function to process the consumed message based on project-specific needs
def process_message(message):
    """
    Custom logic for processing messages based on your project's needs.
    For example, saving the message to a database or performing data analysis.
    """
    logger.info(f"Processing project message: {message}")

# Run the consumer when executed directly
if __name__ == "__main__":
    consume_messages()