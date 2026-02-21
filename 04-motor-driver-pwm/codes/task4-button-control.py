import pigpio
import time

#Motor pins
PWM_PIN = 13    #Hardware PWM
DIR_PIN = 12    #Direction pin (free GPIO)



#Button pins
BTN_ACCEL = 16  #Button A
BTN_DIR = 17    #Button B

PWM_FREQ = 10000    #10 kHz PWM

pi = pigpio.pi()

if not pi.connected:
 print("pigpiod not running!")
 exit()

#Setup motor pins
pi.set_mode(DIR_PIN, pigpio.OUTPUT)

#Setup buttons
pi.set_mode(BTN_ACCEL, pigpio.INPUT)
pi.set_mode(BTN_DIR, pigpio.INPUT)

#Enable pull-ups (buttons active LOW)
pi.set_pull_up_down(BTN_ACCEL, pigpio.PUD_UP)
pi.set_pull_up_down(BTN_DIR, pigpio.PUD_UP)

#Motor state
direction = 1
duty = 0

pi.write(DIR_PIN, direction)

print("Motor control running... Press buttons.")

try:
 while True:
  accel_pressed = pi.read(BTN_ACCEL) == 0 # Active low
  dir_pressed = pi.read(BTN_DIR) == 0

  # ACCEL BUTTON (GPIO 16)
  if accel_pressed:
   duty = min(1000000, duty + 25000) # Increase duty
  else:
   duty = max(0, duty - 15000) # Natural slow-down

  # DIRECTION BUTTON (GPIO 17)
  if dir_pressed and duty < 100000: # Must be slow to switch direction
   direction = 1 - direction
   pi.write(DIR_PIN, direction)
   print("Direction changed:", direction)
   time.sleep(0.3) # Debounce

  # Apply PWM
  pi.hardware_PWM(PWM_PIN, PWM_FREQ, duty)
  time.sleep(0.02)

except KeyboardInterrupt:
 print("\nStopping motor...")

finally:
 pi.hardware_PWM(PWM_PIN, PWM_FREQ, 0)
 pi.stop()
