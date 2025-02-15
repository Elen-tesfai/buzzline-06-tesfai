# buzzline-06-tesfai

This project processes real-time messages using a Kafka producer-consumer system. The producer generates and sends messages, while the consumer processes those messages and stores sentiment analysis results in an SQLite database for further insights.

## Overview

The **buzzline-06-tesfai** project aims to handle real-time data streams using Kafka. It includes a custom producer that sends messages, a consumer that processes and analyzes these messages, and stores the results in an SQLite database. The sentiment analysis helps to categorize and understand the tone of the incoming messages.

## Project Structure

Here is an overview of the folders and their contents:

- `producers/`: Contains scripts that generate and send messages to Kafka or other storage.
- `consumers/`: Handles processing of incoming messages and storing results into a database.
- `data/`: Contains data files used for input or output during the project.
- `utils/`: Utility functions that support the main processes, such as Kafka connections or sentiment analysis.
- `logs/`: Stores logs related to the producers and consumers for debugging and monitoring.

## Prerequisites

1. **Python 3.11** (or higher)
2. **Kafka** (running locally or remotely)
3. **Zookeeper** (used for managing Kafka's cluster)
4. **SQLite** (for storing processed results)

## Setup Instructions

Follow these steps to get your environment ready:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/buzzline-06-tesfai.git
   cd buzzline-06-tesfai
2. Set up a Python virtual environment:
```shell
python3 -m venv .venv
source .venv/bin/activate  # For Mac/Linux
.venv\\Scripts\\activate     # For Windows
```
3. Install dependencies from requirements.txt:
```shell
pip install -r requirements.txt
```
4. Set up the environment variables in .env as needed for your project configuration.

## Start Zookeeper and Kafka
1. Start Zookeeper:
```shell
cd /path/to/kafka/bin
./zookeeper-server-start.sh ../config/zookeeper.properties
```
2. Start Kafka:
cd /path/to/kafka/bin
```shell
./kafka-server-start.sh ../config/server.properties
Running the Project
```
## Producer (Sending Messages)

1. Open a terminal, navigate to your project folder, and activate your virtual environment.
2. Run the producer script to begin sending messages:
```shell
python -m producers.producer_tesfai
```
## Consumer (Processing Messages)
1. Open another terminal and activate your virtual environment again.
2. Run the consumer script to process the incoming messages
```shell
python -m consumers.consumer_tesfai
```
## License
This project is licensed under the MIT License. See the LICENSE.txt file for details.

---
### Explanation of Structure:
1. **Project Title (`# buzzline-06-tesfai`)**: This is the heading at the top of the file.
2. **Project Overview**: This section introduces what the project is about.
3. **Project Structure**: Lists and describes the folders in your project.
4. **Prerequisites**: Requirements for the system to run the project, including Python version and other tools.
5. **Setup Instructions**: A step-by-step guide to setting up the environment, including cloning the repository, setting up the virtual environment, and installing dependencies.
6. **Running the Project**: Instructions on how to run both the producer and the consumer, which are the core of the system.
7. **License**: A section about the MIT License for the project.

This is the kind of content you would typically see in a well-structured `README.md` file, and you can copy-paste this directly into your file.


