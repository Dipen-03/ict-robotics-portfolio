import paho.mqtt.client as mqtt
import json

BROKER = "10.10.200.15"
PORT = 1883
TOPICS = [("melli/sensor/value", 0), ("melli/sensor/status", 0)]

def on_connect(client, userdata, flags, reason_code, properties=None):
    print("Connected with result code:", reason_code)
    for t, q in TOPICS:
        client.subscribe(t)
        print(f"Subscribed to topic: {t}")

def on_message(client, userdata, msg):
    raw_payload = msg.payload.decode()
    print("\n==== NEW MESSAGE ====")
    print("Raw message:", raw_payload)

    try:
        data = json.loads(raw_payload)
        print("As dictionary:", data)

        # Safely access label & confidence
        label = data.get("label")
        confidence = data.get("confidence")

        print("Label:", label)
        print("Confidence:", confidence)

    except json.JSONDecodeError:
        print("Could not decode JSON! Payload might not be JSON.")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, keepalive=60)
print("Starting MQTT loop. Press Ctrl+C to stop.")
client.loop_forever()