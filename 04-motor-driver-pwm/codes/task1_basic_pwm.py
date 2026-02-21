import pigpio
import time

PWM_PIN = 13       # Hardware PWM pin
DIR_PIN = 12
    # Motor direction pin
PWM_FREQ = 10000   # 10 kHz PWM signal

pi = pigpio.pi()
if not pi.connected:
    exit()

# Setup pins
pi.set_mode(DIR_PIN, pigpio.OUTPUT)

# Forward direction
pi.write(DIR_PIN, 1)

# Set PWM (Duty range 0-1,000,000)
pi.hardware_PWM(PWM_PIN, PWM_FREQ, 500000) # 50% duty

time.sleep(3)

# Stop motor
pi.hardware_PWM(PWM_PIN, PWM_FREQ, 0)

pi.stop()