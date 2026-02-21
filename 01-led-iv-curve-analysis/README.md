# FIRST EXPERIMENT WITH BREADBOARD (LAB 1)

**University:** HAMK University of Applied Sciences, Riihimäki Campus 🇫🇮  
**Course:** Controllers and Electronics  
**Group Members:** Dipen Gaihre and Lotus Nyaupane  
**Date:** 30.10.2025

---

## Objectives
The purpose of this first lab was to learn how to use a breadboard and make a basic LED circuit. We connected a red LED and a 100 Ω resistor on the breadboard and attached it to the ADALM1000 (M1K). Using the PixelPulse2 program, we slowly increased the voltage and measured the current. This allowed us to draw the LED’s I–V curve.

## Theory
A LED is a diode that only turns on when current goes in the forward direction. At low voltage, almost no current flows. When the voltage reaches the LED’s forward voltage (about 1.6–2.0 V for a red LED), the current increases quickly.

The ADALM1000 can give voltage and read current at the same time. PixelPulse2 can make a sawtooth signal, which slowly increases the voltage. This makes it easier to measure the LED’s I–V curve.



## Equipment, Materials, and Methods
### Equipment:
* ADALM1000 (M1K)
* PixelPulse2 software
* Breadboard
* Red LED
* 100 Ω resistor
* Jumper wires
* USB cable
* Excel

### Breadboard Setup:
We made the LED circuit like this:
1. The long leg of the LED (anode) was connected to the resistor.
2. The other side of the resistor was connected to Channel A of the M1K.
3. The short leg of the LED (cathode) was connected to Ground (GND).

![Circuit Setup](media/setup_photo.jpg)

## Results and Observations
### Shape of the I–V Curve
The graph we created in Excel showed the typical LED shape:
* The current stays basically flat (almost zero) at low voltages.
* Once the forward voltage is reached, the current rises quickly.
* The curve makes a clear “knee” shape where the LED starts to conduct.

### Data Analysis
The highest current we saw was around **23–24 mA**, which is fine because we used a 100 Ω resistor to keep the current safe. Our results showed that the red LED turns on around **1.7–2.0 V**, which is exactly what theory says.

### Possible Sources of Small Error
* Loose or imperfect breadboard connections
* Noise from the PixelPulse2 measurement
* Tiny differences between LEDs from the factory
* Small changes in the USB power supply

## Conclusions
In this first lab, we learned how to build a simple LED circuit on a breadboard and how to use the ADALM1000 with PixelPulse2 to sweep voltage and measure current. After exporting the data to Excel, we created I-V graphs and analyzed how the LED behaves. 

Our results showed that the red LED turns on around 1.7–2.0 V, which is exactly what theory says. Overall, this lab gave us good hands-on experience with basic electronics and data analysis.

---

## 📂 Project Files
* [Full Report Document](./docs/FIRST_EXPERIMENT_WITH_BREADBOARD_1.docx)
* [Data Analysis Excel Sheet](./data/lab1_data.xlsx)

## References
We took help from AI tools like ChatGPT, our friends, and our teacher for this project.
