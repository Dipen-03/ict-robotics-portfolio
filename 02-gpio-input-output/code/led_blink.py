import pigpio
import time

pi = pigpio.pi()
LED_PIN = 23

pi.set_mode(LED_PIN, pigpio.OUTPUT)

for i in range(5):
    pi.write(LED_PIN, 1)
    print("LED ON")
    time.sleep(1)
    
    pi.write(LED_PIN, 0)
    print("LED OFF")
    time.sleep(1)

pi.stop()
print("LED blinking finished automatically.")