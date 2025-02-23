
import logging
from kafka import KafkaConsumer
import json

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

# Step 3: Function to consume messages from Kafka topic
def consume_messages(consumer):
    logger = create_logger()  # Get the logger instance
    try:
        logger.info('Starting message consumption...')
        for message in consumer:
            logger.info(f'Received message: {message.value}')
    except Exception as e:
        logger.error(f'Error consuming message: {e}')

# Step 4: Main function to run the consumer
def main():
    logger = create_logger()
    
    # Create Kafka consumer
    consumer = create_consumer()
    
    # Consume messages from the Kafka topic
    consume_messages(consumer)

if __name__ == "__main__":
    main()
    