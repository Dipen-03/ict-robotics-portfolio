import paho.mqtt.client as mqtt

BROKER = "10.10.200.15"
PORT = 1883
TOPICS = [("melli/sensor/value", 0), ("melli/sensor/status", 0)]

def on_connect(client, userdata, flags, reason_code, properties=None):
    print("Connected with result code:", reason_code)
    # Subscribe when connected
    for t, q in TOPICS:
        client.subscribe(t)
        print(f"Subscribed to topic: {t}")

def on_message(client, userdata, msg):
    print("---- MQTT MESSAGE ----")
    print("Topic:  ", msg.topic)
    print("Payload: ", msg.payload.decode())
    print("----------------------")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, keepalive=60)

print("Starting MQTT loop. Press Ctrl+C to stop.")
client.loop_forever()