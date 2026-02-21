import pigpio
import time

PWM_PIN = 13
DIR_PIN = 12
PWM_FREQ = 10000

pi = pigpio.pi()
pi.set_mode(DIR_PIN, pigpio.OUTPUT)

# ---------- FORWARD 100% ----------
pi.write(DIR_PIN, 1)
pi.hardware_PWM(PWM_PIN, PWM_FREQ, 1000000) # 100%
time.sleep(3)

# Stop before reversing
pi.hardware_PWM(PWM_PIN, PWM_FREQ, 0)
time.sleep(1)

# ---------- BACKWARD 50% ----------
pi.write(DIR_PIN, 0)
pi.hardware_PWM(PWM_PIN, PWM_FREQ, 500000) # 50%
time.sleep(3)

# Stop
pi.hardware_PWM(PWM_PIN, PWM_FREQ, 0)
pi.stop()