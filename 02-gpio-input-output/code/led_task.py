import pigpio
import time

pi = pigpio.pi()
if not pi.connected:
    print("NOT CONNECTED")
    exit()

BUTTON_PIN = 16
LED_PIN = 23

pi.set_mode(BUTTON_PIN, pigpio.INPUT)
pi.set_pull_up_down(BUTTON_PIN, pigpio.PUD_UP)
pi.set_mode(LED_PIN, pigpio.OUTPUT)

led_state = 0
pi.write(LED_PIN, led_state)

prev_button_state = pi.read(BUTTON_PIN)

try:
    while True:
        button_state = pi.read(BUTTON_PIN)
        if prev_button_state == 1 and button_state == 0:
            led_state = 0 if led_state else 1
            pi.write(LED_PIN, led_state)
            print(f"Button pressed! LED {'ON' if led_state else 'OFF'}")
            time.sleep(0.2) # simple debounce
        
        prev_button_state = button_state
        time.sleep(0.01)

except KeyboardInterrupt:
    pi.write(LED_PIN, 0)
    pi.stop()
    print("\nExiting program...")