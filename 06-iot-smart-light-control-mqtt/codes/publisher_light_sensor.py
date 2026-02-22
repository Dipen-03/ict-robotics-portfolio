import paho.mqtt.client as mqtt
import pigpio
import time

# MQTT Broker configuration
# LabRobotics network broker IP
BROKER = "10.10.200.15"
TOPIC = "hamk/light/brightness"

# Initialize pigpio and SPI
pi = pigpio.pi()
# Open SPI channel 0, 1MHz, flags 0
h = pi.spi_open(0, 1000000, 0)

# Create MQTT Client
client = mqtt.Client()
client.connect(BROKER, 1883, 60)

print("Team 1: Publishing light data to Broker...")

try:
    while True:
        # Read 2 bytes from Pmod ALS sensor via SPI
        count, data = pi.spi_read(h, 2)
        
        # Exact bit manipulation logic from your report
        # Extracts 8-bit brightness from the 16-bit stream
        brightness = ((data[0] & 0x0F) << 4) | ((data[1] & 0xF0) >> 4)
        
        # Publish to the shared topic
        client.publish(TOPIC, brightness)
        print(f"Published Brightness: {brightness}")
        
        time.sleep(1)

except KeyboardInterrupt:
    print("\nStopping Publisher...")
finally:
    pi.spi_close(h)
    pi.stop()