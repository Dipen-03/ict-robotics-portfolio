# Lab 5: Ambient Light Sensor (SPI)

**Date:** 27.11.2025  
**Group Members:** Dipen Gaihre and Lotus Nyaupane  
**Course:** Controllers and Electronics  

---

## 1. Objective

The objective of this lab was to learn how to use SPI communication on the Raspberry Pi and interface it with the PmodALS ambient light sensor. In this lab, we enabled SPI, read raw ADC data from the sensor, and converted it into meaningful light intensity values.

---

## 2. Equipment Used

- Raspberry Pi Zero 2W  
- PmodALS Ambient Light Sensor  
- Python with pigpio library  
- Breadboard  
- Jumper wires  
- 40-pin cable  

---

## 3. Wiring and Setup

The PmodALS sensor was connected to the Raspberry Pi using the SPI interface.

**Connections:**

- MISO → MISO  
- SCK → SCK  
- CS → CE0  
- 3.3V → 3.3V  
- GND → GND
  
SPI was enabled in the Raspberry Pi settings using:
    sudo raspi-config
    
### Wiring Diagram


[ Insert Wiring Diagram Image Here ]

### Wiring Diagram


[ Insert Wiring Diagram Image Here ]


---

## 4. Implementation

### Task 1: SPI Initialization

SPI communication was initialized in Python using the pigpio library. The SPI speed was set to 1 MHz to ensure stable communication with the sensor.
[ Insert SPI Initialization Code Here ]

---

### Task 2 & 3: Reading and Processing Data

The PmodALS sensor sends data in two bytes. The 8-bit ADC value is placed between leading and trailing zeros, so bit manipulation was required to extract the correct value.

We used bit shifting operators (`<<` and `>>`) to combine the two bytes and isolate the light intensity value.
[ Insert Bit Manipulation Code Here ]


---

### Task 4: Output

The program printed:

- Raw bytes received from the sensor  
- Combined binary value  
- Final decimal light intensity value (0–255)  


[ Insert Terminal Output Screenshot or Example Here ]


---

## 5. Results and Observations

- The sensor values increased when light was shone on it.  
- The values decreased when the sensor was covered.  
- The ADC produced values between 0 and 255.  
- SPI communication worked correctly after enabling it in the Raspberry Pi configuration.  

---

## 6. Conclusion

In this lab, we successfully interfaced the PmodALS ambient light sensor with the Raspberry Pi using SPI communication.
We learned how SPI works, how to read sensor data, and how to use bit manipulation to extract useful information from transmitted bytes.



