import pigpio
import time

PWM_PIN = 13
DIR_PIN = 12
PWM_FREQ = 10000

pi = pigpio.pi()
pi.set_mode(DIR_PIN, pigpio.OUTPUT)

pi.write(DIR_PIN, 1) # Forward

for duty in range(0, 1000001, 50000): # 0 -> 100% in steps
    pi.hardware_PWM(PWM_PIN, PWM_FREQ, duty)
    print("Duty:", duty / 10000, "%")
    time.sleep(0.1)

# Stop
pi.hardware_PWM(PWM_PIN, PWM_FREQ, 0)
pi.stop()
