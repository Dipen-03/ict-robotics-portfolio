import paho.mqtt.client as mqtt
import json
import RPi.GPIO as GPIO
import time

# -------- GPIO SETUP --------
GPIO.setmode(GPIO.BCM)

GREEN = 17   # no person
RED = 27     # high confidence
YELLOW = 22  # low confidence
BLUE = 23    # connection lost (optional)

LEDS = [GREEN, RED, YELLOW, BLUE]

for pin in LEDS:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

def all_off():
    for pin in LEDS:
        GPIO.output(pin, GPIO.LOW)

# -------- MQTT SETTINGS --------
BROKER = "10.10.200.15"
PORT = 1883
TOPIC = "melli/sensor/value"

# -------- MQTT CALLBACKS --------
def on_connect(client, userdata, flags, reason_code, properties=None):
    print("Connected to MQTT")
    client.subscribe(TOPIC)
    GPIO.output(BLUE, GPIO.LOW)  # connection OK

def on_disconnect(client, userdata, reason_code, properties=None):
    print("MQTT disconnected!")
    all_off()
    GPIO.output(BLUE, GPIO.HIGH) # blue LED ON for disconnect

def handle_detection(label, confidence):
    all_off()

    if confidence <= 0.40:
        GPIO.output(GREEN, GPIO.HIGH)
        print("GREEN -> No person detected")
        return

    if confidence >= 0.90:
        GPIO.output(RED, GPIO.HIGH)
        print("RED -> High confidence person detected")
    else:
        GPIO.output(YELLOW, GPIO.HIGH)
        print("YELLOW -> Low confidence person detected")

def on_message(client, userdata, msg):
    print("\nMQTT Message:", msg.payload.decode())

    try:
        data = json.loads(msg.payload.decode())
        label = data.get("label")
        confidence = data.get("confidence")

        print("Label:", label)
        print("Confidence:", confidence)

        handle_detection(label, confidence)

    except Exception as e:
        print("Error parsing message:", e)

# -------- MAIN --------
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

try:
    client.connect(BROKER, PORT)
    print("Listening for detections...")
    client.loop_forever()

except KeyboardInterrupt:
    print("Exiting...")

finally:
    all_off()
    GPIO.cleanup()