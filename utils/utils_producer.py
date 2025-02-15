import json
from kafka import KafkaProducer
from utils.utils_config import KAFKA_BOOTSTRAP_SERVERS, KAFKA_TOPIC
from utils.utils_logger import logger

# Create a Kafka producer instance
def create_kafka_producer():
    try:
        producer = KafkaProducer(
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        logger.info(f"Connected to Kafka at {KAFKA_BOOTSTRAP_SERVERS}")
        return producer
    except Exception as e:
        logger.error(f"Error creating Kafka producer: {e}")
        raise

# Send a message to the Kafka topic
def send_message(producer, message):
    try:
        producer.send(KAFKA_TOPIC, message)
        producer.flush()
        logger.info(f"Sent message: {message}")
    except Exception as e:
        logger.error(f"Error sending message: {e}")