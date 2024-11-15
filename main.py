import json

from mqtt.mqtt_subscriber import MQTTSubscriber
from payload_standardizer.config import AGENT_LANGUAGES
from payload_standardizer.standardizer import PayloadStandardizer


def subscribe_and_process():
    """
    Subscribes to MQTT subtopics, standardizes received messages, and processes them.
    """

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

            # Process the standardized payload
            print(f"Standardized Payload from {subtopic}: {json.dumps(standardized_payload, indent=2)}")

        except Exception as e:
            print(f"Error processing message from {msg.topic}: {e}")

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
