# LAB 4: MOTOR DRIVER & PWM

**University:** HAMK University of Applied Sciences  
**Course:** Controllers and Electronics  
**Group Members:** Dipen Gaihre and Lotus Nyaupane  
**Date:** 13.11.2025

---

## 1. Objectives
The purpose of this lab was to learn how to control a DC motor using the Raspberry Pi and a **Cytron MD13S** motor driver. We used **PWM (Pulse Width Modulation)** to change the motor speed and a direction pin to change the rotation direction. Later, we added buttons to control the motor manually. 

This lab helped us understand how PWM, H-bridges, and motor drivers work together.

## 2. Equipment
The following equipment was used:
* **Raspberry Pi Zero 2W**
* **Cytron MD13S Motor Driver**
* **12V DC Motor** and **External 12V Power Supply**
* **Grove Dual Button**
* **Breadboard and Jumper Wires**
* **Python** with the `pigpio` library

## 3. Wiring and Setup
We connected the Raspberry Pi to the Cytron MD13S motor controller using one GPIO pin for Direction and one for PWM speed control. 

* **PWM_PIN:** 13 (Hardware PWM)
* **DIR_PIN:** 12
* **BTN_ACCEL:** 16 (Button A)
* **BTN_DIR:** 17 (Button B)



---

## 4. Tasks and Python Code
Below are the links to the exact code used for each task as documented in the report:

* **[Task 1: Basic PWM Control](./code/task1_basic_pwm.py)** – Sending a constant duty cycle signal to the motor.
* **[Task 2: Direction Control](./code/task2_direction_control.py)** – Driving the motor forward and backward at different speeds.
* **[Task 3: Acceleration](./code/task3_motor_acceleration.py)** – Using a loop to slowly increase the duty cycle from 0 to 100%.
* **[Task 4: Manual Button Control](./code/task4_button_control.py)** – Implementing real-time acceleration and direction switching via buttons.

---

## 5. Results and Observations

### Task 3: Terminal Output
The acceleration loop successfully increased the duty cycle step-by-step from 0.0% to 100.0%.

![Task 3 Terminal Screenshot](media/task3_terminal.jpg)  
*Fig: Terminal screenshot showing duty cycle increments.*

### Task 4: Manual Control Output
We successfully used buttons to change direction and increase speed. The terminal logged direction changes and debouncing events.

![Task 4 Terminal Screenshot](media/task4_terminal.jpg)  
*Fig: Terminal screenshot showing button-triggered events.*

**Key Observations:**
* **Hardware PWM** was significantly smoother than software PWM for motor speed stability.
* The **direction pin** correctly reversed the motor rotation by switching the H-bridge state.
* **Safety:** Direction must be changed only at low speeds (duty < 100,000) to avoid sudden mechanical force on the motor gears.

---

## 6. Conclusion
In this lab, we learned how to control a motor using PWM, a direction pin, and a motor driver. We practiced changing speed, reversing direction, and using buttons to interact with the motor. Working on previous labs made it much easier to complete these tasks because we already understood the equipment.

---

### 📂 Project Structure
* **[code/](./code/)**: Contains the `requirements.txt` and all task scripts.
* **[media/](./media/)**: Contains images of hardware wiring and terminal logs.
* **[report/](./report/)**: Contains the full [lab4.pdf](./report/lab4.pdf) document.
