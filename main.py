import argparse
import logging
from producers.producer_tesfai import create_producer, send_message
from consumers.consumer_tesfai import create_consumer, consume_messages

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run_producer():
    producer = create_producer()
    if producer:
        message = "Test message from main script"
        send_message(producer, message)
        producer.close()  # Close the producer after sending the message

def run_consumer():
    consumer = create_consumer()
    if consumer:
        logger.info("Starting message consumption...")
        consume_messages(consumer)  # Continuously consume messages

def main():
    parser = argparse.ArgumentParser(description="Kafka Producer and Consumer")
    parser.add_argument(
        "--mode", choices=["producer", "consumer"], required=True,
        help="Choose whether to run the producer or the consumer"
    )
    args = parser.parse_args()

    if args.mode == "producer":
        run_producer()
    elif args.mode == "consumer":
        run_consumer()

if __name__ == "__main__":
    main()