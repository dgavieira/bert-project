import paho.mqtt.client as mqtt


class MQTTSubscriber:
    def __init__(self, broker_host="localhost", broker_port=1883):
        """
        Initializes the MQTT subscriber.
        :param broker_host: Hostname of the MQTT broker (default is localhost).
        :param broker_port: Port of the MQTT broker (default is 1883).
        """
        self.broker_host = broker_host
        self.broker_port = broker_port
        self.client = mqtt.Client()

    def on_connect(self, client, userdata, flags, rc):
        """
        Callback for when the subscriber connects to the broker.
        :param client: The MQTT client instance.
        :param userdata: User-defined data.
        :param flags: Response flags sent by the broker.
        :param rc: The connection result.
        """
        if rc == 0:
            print("Connected to MQTT broker.")
        else:
            print(f"Failed to connect, return code {rc}")

    def subscribe(self, topics):
        """
        Subscribes to a list of topics.
        :param topics: List of MQTT topics to subscribe to.
        """
        self.client.on_connect = self.on_connect
        self.client.connect(self.broker_host, self.broker_port)

        # Subscribe to each topic
        for topic in topics:
            self.client.subscribe(topic)
            print(f"Subscribed to topic: {topic}")

        # Blocking call to process network traffic
        self.client.loop_forever()
