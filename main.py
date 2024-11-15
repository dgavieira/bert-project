import logging
import json
from mqtt.mqtt_subscriber import MQTTSubscriber
from mqtt.mqtt_publisher import MQTTPublisher
from payload_standardizer.standardizer import PayloadStandardizer
from payload_standardizer.config import AGENT_LANGUAGES
from utils.database import DatabaseManager


# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


def subscribe_and_process():
    """
    Subscribes to MQTT subtopics, standardizes received messages, and processes them.
    """
    db_manager = DatabaseManager()
    publisher = MQTTPublisher(broker_host="localhost", broker_port=1883)

    # Connect the publisher to the broker
    publisher.connect()

    def on_message(client, userdata, msg):
        try:
            # Decode the payload
            payload = json.loads(msg.payload.decode())
            subtopic = msg.topic

            # Extract the agent identifier from the subtopic
            agent = subtopic.split("/")[-1]
            source_lang = AGENT_LANGUAGES.get(agent, "en")

            # Standardize the payload
            standardizer = PayloadStandardizer(source_lang=source_lang)
            standardized_payload = standardizer.standardize_payload(payload)

            # Convert standardized payload to JSON string
            standardized_payload_json = json.dumps(standardized_payload, indent=2)

            # Log and save the standardized payload
            logger.info(f"Standardized Payload from {subtopic}: {standardized_payload_json}")
            db_manager.save_payload(topic=subtopic, payload=standardized_payload_json)

            # Forward standardized payload to a new subtopic
            new_subtopic = f"standardized/{agent}"
            publisher.publish(topic=new_subtopic, payload=standardized_payload)

        except Exception as e:
            logger.error(f"Error processing message from {msg.topic}: {e}")

    # Initialize the subscriber
    subscriber = MQTTSubscriber(broker_host="localhost", broker_port=1883)

    # Define agent subtopics
    agent_subtopics = [f"agents/{agent}" for agent in AGENT_LANGUAGES.keys()]

    # Set the custom on_message handler
    subscriber.client.on_message = on_message

    # Subscribe to topics
    subscriber.subscribe(agent_subtopics)


if __name__ == "__main__":
    subscribe_and_process()

