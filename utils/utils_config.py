import os
KAFKA_BOOTSTRAP_SERVERS = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')
DB_NAME = os.getenv('DB_NAME', 'sentiment_analysis.db')
SENTIMENT_ANALYSIS_MODEL = 'textblob'
