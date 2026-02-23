# Raspberry Pi 5 Hailo AI Detection via MQTT  
### Lab 7 – Controllers and Electronics  

**Course:** Controllers and Electronics  
**Laboratory:** Lab 7  
**Platform:** Raspberry Pi 5 (Hailo AI Kit) & Raspberry Pi Zero 2W  
**Date:** 15.12.2025  

**Group Members:**  
- Dipen Gaihre 
- Milan Khadka  
- Udit Bhattarai  
 

---

## 1. Project Overview

This laboratory project demonstrates how AI-based person detection running on a Raspberry Pi 5 with a Hailo AI accelerator can transmit detection results using the MQTT protocol to a Raspberry Pi Zero 2W.  

The subscriber device processes the received JSON data and controls LED indicators based on detection confidence and connection status.

The project integrates:

- Edge AI inference  
- MQTT publish/subscribe communication  
- JSON data processing  
- GPIO-based actuator control  

---

## 2. System Architecture

### MQTT Communication Model

- **Publisher:** Raspberry Pi 5 (Hailo AI pipeline)  
- **Subscriber:** Raspberry Pi Zero 2W  
- **Broker IP:** 10.10.200.15  
- **Topics:**  
  - `melli/sensor/value`  
  - `melli/sensor/status`  

![MQTT Architecture](media/mqtt-architecture-diagram.jpg)

---

## 3. Detection Data Format

Detection results were transmitted in JSON format:

```json
{"label": "person", "confidence": 0.82}
```

- `label` → detected object class  
- `confidence` → probability value (0.0 – 1.0)  

This data was parsed on the subscriber side and used for decision-making logic.

---

## 4. LED Logic Implementation

The Raspberry Pi Zero 2W controlled four LEDs based on detection results:

| Condition | LED |
|------------|------|
| No person detected | Green |
| Person detected (confidence ≥ 0.75) | Red |
| Person detected (confidence < 0.75) | Yellow |
| MQTT connection lost | Blue |

### Hardware Setup

![Pi Zero Setup](media/pi-zero-led-setup.jpg)

### Real Circuit Output

![Circuit Output](media/real-circuit-output.jpg)

---

## 5. Implementation

### Publisher Node  
Raspberry Pi 5 running Hailo AI pipeline and publishing detection results via MQTT.

### Subscriber Node  
Raspberry Pi Zero 2W subscribing to MQTT topics, parsing JSON data, and controlling LEDs.

---

## 6. Repository Structure

```
WEEK7/
│
├── codes/
│   ├── ai_node_publisher.py
│   └── actuator_subscriber.py
│
├── media/        # Figures and system outputs
│
└── reports/
    └── Lab7_Final_Report.pdf
```

---

## 7. Results

- MQTT communication functioned reliably  
- JSON parsing was successfully implemented  
- LED indicators responded correctly to detection confidence  
- Minor latency was observed due to network delay  
- System remained stable during laboratory testing  

---

## 8. Real-World Applications

This type of Edge AI + IoT architecture can be applied in:

- Smart security systems  
- Occupancy monitoring  
- Industrial safety detection  
- Energy-efficient building automation  
- Privacy-preserving smart camera systems  

Running inference locally on the Raspberry Pi 5 reduces latency and minimizes dependency on cloud services.

---

## 9. Conclusion

This laboratory work demonstrated the integration of AI inference, MQTT communication, and embedded hardware control within a distributed IoT system.

The project strengthened practical understanding of:

- Publish/subscribe communication models  
- Edge AI deployment  
- JSON data handling  
- Real-time embedded system behavior  

The system operated as expected and fulfilled all laboratory objectives.

---
