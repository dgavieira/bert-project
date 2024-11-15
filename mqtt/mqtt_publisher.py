import paho.mqtt.client as mqtt
import json


class MQTTPublisher:
    def __init__(self, broker_host="localhost", broker_port=1883):
        """
        Initializes the MQTT publisher.
        :param broker_host: Hostname of the MQTT broker (default is localhost).
        :param broker_port: Port of the MQTT broker (default is 1883).
        """
        self.broker_host = broker_host
        self.broker_port = broker_port
        self.client = mqtt.Client()

    def connect(self):
        """
        Connects to the MQTT broker.
        """
        self.client.connect(self.broker_host, self.broker_port)
        print(f"Connected to MQTT broker at {self.broker_host}:{self.broker_port}")

    def publish(self, topic: str, payload: dict):
        """
        Publishes a payload to the specified MQTT topic.
        :param topic: MQTT topic to publish to.
        :param payload: Dictionary payload to send.
        """
        message = json.dumps(payload)
        self.client.publish(topic, message)
        print(f"Published to topic '{topic}': {message}")

    def disconnect(self):
        """
        Disconnects from the MQTT broker.
        """
        self.client.disconnect()
        print("Disconnected from MQTT broker.")
