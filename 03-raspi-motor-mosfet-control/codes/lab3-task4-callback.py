import pigpio
import time

BUTTON_PIN = 20
MOTOR_PIN = 12

pi = pigpio.pi()

pi.set_mode(BUTTON_PIN, pigpio.INPUT)
pi.set_mode(MOTOR_PIN, pigpio.OUTPUT)
pi.write(MOTOR_PIN, 0)

# Callback function: runs only when button is pressed
def button_pressed(gpio, level, tick):
    print("Button pressed!")
    pi.write(MOTOR_PIN, 1)
    time.sleep(1)          # Motor runs for 1 second
    pi.write(MOTOR_PIN, 0)

# Register callback to trigger on Falling Edge (Button Press)
cb = pi.callback(BUTTON_PIN, pigpio.FALLING_EDGE, button_pressed)

try:
    print("Callback active. Press the button to start motor.")
    while True:
        time.sleep(1) # Main loop stays idle, saving CPU resources

except KeyboardInterrupt:
    print("Program stopped.")

finally:
    cb.cancel()    # Stop the callback listener
    pi.write(MOTOR_PIN, 0)
    pi.stop()