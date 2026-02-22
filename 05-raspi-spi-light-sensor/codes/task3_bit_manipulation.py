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

def byte_to_bit(data):
    # The PmodALS sends data in two bytes [cite: 170]
    b1 = data[0]
    b2 = data[1]
    
    # Print raw binary for verification [cite: 204]
    print(format(b1, '08b')) # b1 as 8-bit binary
    print(format(b2, '08b')) # b2 as 8-bit binary
    
    # Combine bits based on datasheet layout [cite: 203]
    cleaned_bit1 = b1 << 4
    cleaned_bit2 = b2 >> 4
    combined = cleaned_bit1 | cleaned_bit2
    
    print(f"Combined binary: {combined:08b}")
    print(f"Decimal Value: {combined}")

try:
    pi = init_pi()
    spi = pi.spi_open(SPI_CHANNEL, SPI_SPEED, SPI_FLAGS)
    
    while True:
        count, data = pi.spi_read(spi, 2) # Read 2 bytes [cite: 244]
        if count > 0:
            byte_to_bit(data)
        time.sleep(0.5)

except KeyboardInterrupt:
    pass
finally:
    pi.spi_close(spi)
    pi.stop()