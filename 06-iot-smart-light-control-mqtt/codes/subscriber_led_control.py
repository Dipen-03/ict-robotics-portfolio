import paho.mqtt.client as mqtt
import pigpio

# Hardware Setup
LED_PIN = 18
pi = pigpio.pi()
pi.set_mode(LED_PIN, pigpio.OUTPUT)

# MQTT Broker configuration
BROKER = "10.10.200.15"
TOPIC = "hamk/light/brightness"

# Callback function when a message is received from the broker
def on_message(client, userdata, msg):
    try:
        # Convert received payload to integer
        val = int(msg.payload.decode())
        print(f"Received Brightness: {val}")
        
        # Actuator logic: Turn LED ON if brightness > 500
        if val > 500:
            pi.write(LED_PIN, 1)
            print("Status: LED ON (Bright)")
        else:
            pi.write(LED_PIN, 0)
            print("Status: LED OFF (Dark)")
            
    except ValueError:
        print("Error: Could not decode message")

# Create MQTT Client and set the callback
client = mqtt.Client()
client.on_message = on_message

# Connect and subscribe to the specific topic
client.connect(BROKER, 1883, 60)
client.subscribe(TOPIC)

print("Team 2: Listening for data on topic 'hamk/light/brightness'...")

try:
    # Keeps the program running to listen for messages
    client.loop_forever()
except KeyboardInterrupt:
    print("\nStopping Subscriber...")
finally:
    pi.write(LED_PIN, 0) # Turn off LED on exit
    pi.stop()