# 🌀 IMU Sensor Display — Raspberry Pi Pico W + MPU6050 + LCD

## 📘 Overview
This project visualizes real-time motion sensor data from an **MPU6050 (accelerometer + gyroscope)** on a **Waveshare 1.14” LCD** connected to a **Raspberry Pi Pico W**.  
The system continuously reads the sensor values over the I²C bus and displays them as dynamic numerical data on the LCD screen. Two onboard buttons allow switching between different display modes.

This project was developed as part of the **Software Engineering (Grundlagen)** course at **Technische Universität Dresden**.

---

## ⚙️ Hardware Components
| Component | Description |
|------------|--------------|
| 🧠 **Raspberry Pi Pico W** | Microcontroller with Wi-Fi, running MicroPython |
| 📟 **Waveshare Pico LCD 1.14”** | SPI-based LCD module for visualization |
| 🎛 **MPU6050** | 6-axis IMU sensor (3-axis accelerometer + 3-axis gyroscope) |
| 🔘 **Button A / Button B** | Used to switch between display modes |
| 🔌 **Connections** | I²C (SCL, SDA), SPI (for LCD), GPIO (for buttons) |

---

## 🧩 Features
- 📡 Real-time I²C communication with MPU6050  
- 🧭 Displays live acceleration and gyroscope data  
- 🔘 Button-controlled display modes:
  - **Mode 1:** Acceleration (X, Y, Z)
  - **Mode 2:** Gyroscope (X, Y, Z)
  - **Mode 3:** Combined data display  
- 🧮 Simple averaging & data smoothing  
- 🖥 Graphical LCD interface using Waveshare’s `st7789` driver and custom fonts  

---

## 🧠 System Architecture
     +--------------------------+
     |   Raspberry Pi Pico W    |
     |--------------------------|
     | I²C → MPU6050 Sensor     |
     | SPI → LCD Display (ST7789)|
     | GPIO → Buttons A / B      |
     +--------------------------+
                 |
     +--------------------------+
     |  Real-time Visualization |
     +--------------------------+
     
## ⚠️ Notes
- The code is written for educational purposes and optimized for clarity, not performance.  
- Some parts (e.g., fonts and display driver) are adapted from **Waveshare** example code under open license.  
- The assignment description belongs to TU Dresden’s LS-AT department and is **not redistributed** here due to copyright reasons.
