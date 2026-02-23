# LAB 7: AI PERSON DETECTION & MQTT INTEGRATION

**University:** HAMK University of Applied Sciences 🇫🇮  
**Course:** Controllers and Electronics  
**Group Members:** Dipen Gaihre, Milan Khadka and Udit Bhattarai 
**Date:** December 15, 2025  

---

## 1. Introduction
This project explores the integration of **Edge AI** with the **IoT ecosystem**. 

A Raspberry Pi 5 equipped with a **Hailo-8L AI accelerator** performs real-time person detection using an AI inference pipeline. The detection results are published as structured JSON data via MQTT. A Raspberry Pi Zero 2W subscribes to this data and provides physical feedback through a multi-state LED indicator system.

**The objective:** To demonstrate real-time AI inference integrated with IoT communication and hardware-level actuation.

---

## 2. System Architecture
The system follows a low-latency publish–subscribe communication model:



* **AI Node (Publisher):** Processes camera frames using YOLOv8 via Hailo accelerator.
* **MQTT Broker:** Routes detection data (IP: `10.10.200.15`).
* **Actuator Node (Subscriber):** Interprets JSON payloads and controls GPIO pins.

### Logical Flow
1. AI detects person in camera frame.
2. Detection result is formatted as JSON.
3. JSON message is published to MQTT broker.
4. Subscriber receives message.
5. LEDs indicate detection confidence and connection status.

---

## 3. Hardware Integration

### 3.1 Actuator Node (Raspberry Pi Zero 2W)
The actuator node uses four LEDs to represent detection confidence and system health.

| Component | GPIO Pin | Logic / System State |
| :--- | :---: | :--- |
| **Green LED** | 17 | System Active / No Person Detected |
| **Red LED** | 27 | High Confidence Detection (> 60%) |
| **Yellow LED** | 22 | Low Confidence Detection (< 60%) |
| **Blue LED** | 10 | Connection Error / MQTT Disconnected |

---

## 4. Implementation

### 4.1 JSON Data Format
Detection results are transmitted in structured JSON format:

    ```json
    {
      "label": "person",
      "confidence": 0.85
    }

The label identifies the detected object, and confidence represents the probability score (0–1).

### 4.2 AI Node (Publisher) – Raspberry Pi 5

This script handles AI inference and MQTT publishing.

   # Save as: codes/ai_node_publisher.py

   # [Insert your Raspberry Pi 5 Python inference + MQTT publishing code here]

Responsibilities:

Run Hailo AI inference pipeline

Extract label and confidence

Format JSON message

Publish to MQTT topic

### 4.3 Actuator Node (Subscriber) – Raspberry Pi Zero 2W

This script subscribes to MQTT topics, parses JSON data, and controls LEDs.

# Save as: codes/actuator_subscriber.py

# [Insert your Raspberry Pi Zero 2W MQTT subscriber + LED control code here]

Responsibilities:

Connect to MQTT broker

Parse JSON using json.loads()

Apply threshold logic

Control GPIO pins using pigpio

## 5. Results & Testing

The system successfully demonstrated real-time detection alerts.

Observations

When no person was detected → Green LED ON

When person detected with high confidence (> 60%) → Red LED ON

When person detected with lower confidence (< 60%) → Yellow LED ON

When MQTT connection was lost → Blue LED ON

Verification

AI detection output was visible in terminal.

Subscriber log confirmed JSON reception.

Physical LEDs responded immediately to detection changes.

Minor latency was observed due to network conditions, but overall performance was stable.

## 6. Real-World Application

This system serves as a prototype for AI-Enhanced Smart Buildings.

Unlike traditional PIR motion sensors, AI-based detection can:

Distinguish humans from pets

Reduce false positives

Improve building security

Optimize energy usage (HVAC & lighting)

Enable intelligent occupancy-based automation

This demonstrates practical Edge AI deployment in IoT systems.


4.2 AI Node (Publisher) – Raspberry Pi 5

This script handles AI inference and MQTT publishing.

# Save as: codes/ai_node_publisher.py

# [Insert your Raspberry Pi 5 Python inference + MQTT publishing code here]

Responsibilities:

Run Hailo AI inference pipeline

Extract label and confidence

Format JSON message

Publish to MQTT topic

4.3 Actuator Node (Subscriber) – Raspberry Pi Zero 2W

This script subscribes to MQTT topics, parses JSON data, and controls LEDs.

# Save as: codes/actuator_subscriber.py

# [Insert your Raspberry Pi Zero 2W MQTT subscriber + LED control code here]

Responsibilities:

Connect to MQTT broker

Parse JSON using json.loads()

Apply threshold logic

Control GPIO pins using pigpio

5. Results & Testing

The system successfully demonstrated real-time detection alerts.

Observations

When no person was detected → Green LED ON

When person detected with high confidence (> 60%) → Red LED ON

When person detected with lower confidence (< 60%) → Yellow LED ON

When MQTT connection was lost → Blue LED ON

Verification

AI detection output was visible in terminal.

Subscriber log confirmed JSON reception.

Physical LEDs responded immediately to detection changes.

Minor latency was observed due to network conditions, but overall performance was stable.

6. Real-World Application

This system serves as a prototype for AI-Enhanced Smart Buildings.

Unlike traditional PIR motion sensors, AI-based detection can:

Distinguish humans from pets

Reduce false positives

Improve building security

Optimize energy usage (HVAC & lighting)

Enable intelligent occupancy-based automation

This demonstrates practical Edge AI deployment in IoT systems.4.2 AI Node (Publisher) – Raspberry Pi 5

This script handles AI inference and MQTT publishing.

# Save as: codes/ai_node_publisher.py

# [Insert your Raspberry Pi 5 Python inference + MQTT publishing code here]

Responsibilities:

Run Hailo AI inference pipeline

Extract label and confidence

Format JSON message

Publish to MQTT topic

4.3 Actuator Node (Subscriber) – Raspberry Pi Zero 2W

This script subscribes to MQTT topics, parses JSON data, and controls LEDs.

# Save as: codes/actuator_subscriber.py

# [Insert your Raspberry Pi Zero 2W MQTT subscriber + LED control code here]

Responsibilities:

Connect to MQTT broker

Parse JSON using json.loads()

Apply threshold logic

Control GPIO pins using pigpio

5. Results & Testing

The system successfully demonstrated real-time detection alerts.

Observations

When no person was detected → Green LED ON

When person detected with high confidence (> 60%) → Red LED ON

When person detected with lower confidence (< 60%) → Yellow LED ON

When MQTT connection was lost → Blue LED ON

Verification

AI detection output was visible in terminal.

Subscriber log confirmed JSON reception.

Physical LEDs responded immediately to detection changes.

Minor latency was observed due to network conditions, but overall performance was stable.

6. Real-World Application

This system serves as a prototype for AI-Enhanced Smart Buildings.

Unlike traditional PIR motion sensors, AI-based detection can:

Distinguish humans from pets

Reduce false positives

Improve building security

Optimize energy usage (HVAC & lighting)

Enable intelligent occupancy-based automation

This demonstrates practical Edge AI deployment in IoT systems.

## 7. Installation & Execution
Dependencies

Install required Python libraries:

pip install paho-mqtt pigpio
Start pigpio daemon
sudo pigpiod
Execution Order

Run actuator_subscriber.py on Raspberry Pi Zero 2W.

Start AI inference and publisher script on Raspberry Pi 5.

Observe real-time LED responses.

## 8. Conclusion

This lab successfully integrated:

Edge AI inference (Hailo accelerator)

MQTT publish–subscribe communication

JSON data processing

GPIO-based real-time visualization

The project demonstrated how AI-generated data can be processed at the edge and translated into meaningful physical outputs in an IoT system.

It strengthened our understanding of distributed systems, edge computing, and AI-driven automation.
