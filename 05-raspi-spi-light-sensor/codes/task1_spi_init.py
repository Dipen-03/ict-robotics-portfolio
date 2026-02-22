import pigpio
import time

pi = pigpio.pi()

if not pi.connected:
    print("Pigpio daemon not running!")
    exit()

# --- Open SPI ---
SPI_CHANNEL = 0         #(CE0 / Pin 24)
SPI_SPEED = 1000000     #(Required for PmodALS ADC)
SPI_FLAGS = 0           #(Default settings, SPI mode 0)

handle = pi.spi_open(SPI_CHANNEL, SPI_SPEED, SPI_FLAGS)
print("SPI opened. Handle:", handle)

time.sleep(1)

# --- Close SPI ---
pi.spi_close(handle)
print("SPI closed.")

pi.stop()