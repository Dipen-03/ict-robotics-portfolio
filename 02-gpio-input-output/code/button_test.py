import pigpio
import time

pi = pigpio.pi()
BUTTON_PIN = 16

pi.set_mode(BUTTON_PIN, pigpio.INPUT)
pi.set_pull_up_down(BUTTON_PIN, pigpio.PUD_UP)

print("Reading button state 10 times...")

for i in range(10):
    state = pi.read(BUTTON_PIN)
    if state == 0:
        print(f"Reading {i+1}: Button pressed!")
    else:
        print(f"Reading {i+1}: Button not pressed.")
    time.sleep(1)

pi.stop()
print("Done reading button.")