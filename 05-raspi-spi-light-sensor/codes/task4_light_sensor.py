import time
import pigpio

SPI_CHANNEL = 0
SPI_SPEED = 1000000
SPI_FLAGS = 0

def init_pi():
    pi = pigpio.pi()
    if pi.connected:
        return pi
    else:
        raise Exception("Failed to connect to pigpio daemon.")

def byte_to_lux(data):
    b1 = data[0]
    b2 = data[1]
    
    # Combined logic: (b1 & 0x0F) << 4 | (b2 >> 4)

    combined = ((b1 & 0x0F) << 4) | (b2 >> 4)
    
    # Optional scaling if needed for specific lux conversion
    lux = (combined / 255) * 100 
    print(lux)

try:
    pi = init_pi()
    spi = pi.spi_open(SPI_CHANNEL, SPI_SPEED, SPI_FLAGS)
    
    print("Reading light levels... Press Ctrl+C to stop.")
    while True:
        count, data = pi.spi_read(spi, 2)
        if count == 2:
            byte_to_lux(data)
        time.sleep(0.5)

except KeyboardInterrupt:
    print("\nProgram stopped.")
finally:
    pi.spi_close(spi)
    pi.stop()