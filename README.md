<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/a/a2/Logo_TU_Dresden_2025.svg" alt="TU Dresden Logo" width="400"/>
</p>

# Mikrorechentechnik I — Praktikum Projects

This repository contains the **Praktikum-2** and **Praktikum-3** projects developed during the **Mikrorechentechnik I** course at **TU Dresden**.  
All projects were implemented using **MicroPython** in the **Thonny IDE**, running on a **Raspberry Pi Pico / Pico W** microcontroller.

---

## 📁 Projects Overview

### Praktikum-2  
This project visualizes real-time motion sensor data from an **MPU6050 (accelerometer + gyroscope)** on a **Waveshare 1.14” LCD** connected to a **Raspberry Pi Pico W**.  
The system continuously reads the sensor values over the I²C bus and displays them as dynamic numerical data on the LCD screen using SPI. Two onboard buttons allow switching between different display modes (acceleration, gyroscope, combined). The code uses the `st7789` display driver and bitmap fonts for clear rendering.

### Praktikum-3  
This project implements a **labyrinth (maze) navigation algorithm**.  
A 2D maze is read from a file, the start and end points are identified, and an algorithm navigates through the maze.  
Focus is on algorithmic design, pathfinding, and structured programming under embedded or simulated conditions.

---

## ⚙️ Hardware & Tools Used

| Component | Purpose / Role |
|-----------|----------------|
| Raspberry Pi Pico / Pico W | Microcontroller platform running MicroPython |
| MPU6050 (6-axis IMU) | Accelerometer + Gyroscope for motion data |
| Waveshare Pico-LCD 1.14” (ST7789) | To visualize sensor data and UI |
| Buttons (GPIO) | Mode switching and user input |
| I/O peripherals / GPIO | Additional sensors or controls as needed |
| Thonny IDE | Development environment used for uploading, debugging, and testing MicroPython code |

---

## 🧠 Technical Details

- All firmware is written in **MicroPython**, and/or Python for simulation components  
- The code was edited, uploaded, and debugged via **Thonny IDE**  
- Projects involve interfacing with peripherals (LCD, GPIO, I²C) and algorithmic logic  
- Designed to be modular, readable, and educational in nature  

---

> ⚠️ Note: This repository does not include copyrighted teaching materials (e.g. assignment PDFs) from TU Dresden.  
> These projects are for educational purposes and demonstrate hands-on microcontroller programming with MicroPython.
