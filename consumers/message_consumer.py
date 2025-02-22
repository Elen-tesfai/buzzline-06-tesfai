import json
import logging
from kafka import KafkaConsumer
from utils.utils_config import KAFKA_BROKER, KAFKA_TOPIC

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_consumer():
    # Create Kafka consumer
    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_BROKER,
        group_id="your_group_id",  # Ensure this matches your producer
        auto_offset_reset="earliest",  # This ensures that we read all messages from the beginning
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
    return consumer

def consume_messages(consumer):
    try:
        for message in consumer:
            # Extract message value and log it
            message_value = message.value
            logger.info(f"Received message: {message_value}")
    except KeyboardInterrupt:
        logger.info("Consumer interrupted, shutting down...")
    finally:
        consumer.close()

def main():
    # Create the consumer and start consuming messages
    consumer = create_consumer()
    logger.info("Consumer started. Waiting for messages...")
    consume_messages(consumer)

if __name__ == "__main__":
    main()