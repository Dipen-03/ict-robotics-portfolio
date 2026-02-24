# ICT & Robotics Portfolio | Dipen Gaihre

Welcome to my academic and project portfolio. I am currently a **2nd-year ICT and Robotics student** at **HAMK University of Applied Sciences**. This repository serves as a cumulative record of my laboratory work in the **Controllers and Electronics** course, documenting my transition from fundamental hardware logic to advanced **Edge AI** and **Industrial IoT** systems.

---

##  Portfolio Overview

This portfolio showcases a series of technical challenges designed to bridge the gap between software and the physical world. My journey progresses from simple GPIO manipulation to building a distributed AI-vision network.

###  Core Technical Toolkit
* **Platforms:** Raspberry Pi 5 (with Hailo-8L AI Kit), Raspberry Pi Zero 2W, Raspberry Pi 4.
* **Communication:** MQTT (TCP/IP), JSON serialization, SPI, I2C.
* **Software:** Python (pigpio, paho-mqtt, NumPy, OpenCV).
* **Models:** YOLOv8 real-time object detection.

---

##  Main Project Highlights

### [Lab 7: AI-Integrated Security System (Capstone)](./07-edge-ai-person-detection-mqtt/)
The most advanced project of my second year involved integrating Edge AI with a distributed IoT network. Working alongside Milan Khadka and Udit Bhattarai, I developed a system that uses computer vision to solve the issue of false alarms in security.

* **How it Works:** A Raspberry Pi 5 performs real-time person detection. Results are packaged into **JSON** strings (label + confidence) and sent via **MQTT** to a Raspberry Pi Zero 2W.
* **Hardware Feedback:** The remote node parses the data to drive a 4-LED status board (Green for clear, Red for alert, Yellow for low confidence, and Blue for system errors).
* **Key Learning:** Successfully managing network latency and data serialization in a multi-node environment.



### [Lab 6: Distributed IoT Communication](./06-iot-smart-light-control-mqtt/)
Before adding AI, I focused on the "Internet" part of IoT. This lab involved two Raspberry Pis communicating over a local network to share light intensity data using a publish-subscribe model.
* **Key Feature:** M2M (Machine-to-Machine) communication using an MQTT broker to bridge sensor data and remote actuators.

---

##  Laboratory Roadmap (Learning Day-by-Day)

While the AI projects are the highlights, they are built on the foundations I mastered in the following labs:

* **[Lab 5: SPI & Bit Manipulation](./05-raspi-spi-light-sensor/)** – Reading raw data from a Pmod ALS light sensor using high-speed serial communication.
* **[Lab 4: Digital Sensors (I2C)](./04-motor-driver-pwm/)** – Implementing master-slave communication to monitor climate and environmental data.
* **[Lab 3: PWM & Motion Control](./03-raspi-motor-mosfet-control/)** – Using Pulse Width Modulation to precisely control DC motor speed and LED brightness.
* **[Lab 2: Signal Conversion (ADC)](./02-gpio-input-output/)** – Interfacing an **MCP3008 ADC** to allow the Raspberry Pi to interpret analog signals from the physical world.
* **[Lab 1: Foundations of GPIO](./01-led-iv-curve-analysis/)** – Introduction to hardware-software synchronization and circuit safety.



---

##  Installation & Setup

To explore any project in this repository:

1.  **Clone the Repository:**
    ```bash
    ```bash
       git clone [https://github.com/Dipen-03/ict-robotics-portfolio.git](https://github.com/Dipen-03/ict-robotics-portfolio.git)
       cd ict-robotics-portfolio
    ```
2.  **Install Requirements:**
    ```bash
        pip install -r requirements.txt
    ```
3.  **Start Services:**
    ```bash
        udo pigpiod
    ```

---

##  About Me
I am passionate about how robotics can solve real-world problems. As a 2nd-year student, I am constantly exploring new ways to integrate intelligence into embedded systems to make them more autonomous and responsive.

* **Institution:** HAMK University of Applied Sciences, Riihimäki 🇫🇮
* **Degree:** ICT and Robotics (Bachelor of Engineering)
* **Connect:** [[LinkedIn Profile Link](https://www.linkedin.com/in/dipen-gaihre-a90297214/)

---
*This portfolio is maintained as a live document of my technical development.*
