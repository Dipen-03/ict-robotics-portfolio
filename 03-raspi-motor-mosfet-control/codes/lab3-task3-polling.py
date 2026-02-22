import pigpio
import time

MOTOR_PIN = 12
BUTTON_PIN = 20

pi = pigpio.pi()

# Setup pins
pi.set_mode(MOTOR_PIN, pigpio.OUTPUT)
pi.write(MOTOR_PIN, 0) # Motor starts OFF
pi.set_mode(BUTTON_PIN, pigpio.INPUT)

try:
    while True:
        button_state = pi.read(BUTTON_PIN)
        if button_state == 0: # Button pressed (Low because of pull-up)
            pi.write(MOTOR_PIN, 1) # Turn motor ON
        else:
            pi.write(MOTOR_PIN, 0) # Turn motor OFF
        time.sleep(0.05) # Small delay to save CPU
        
except KeyboardInterrupt:
    print("Program stopped by user.")

finally:
    pi.write(MOTOR_PIN, 0) # Safety: Ensure motor is OFF
    pi.stop()