# 🐄📡 Smart Livestock Health Monitoring System

An IoT-based **real-time livestock health monitoring system** designed to continuously track critical health parameters of cattle using a **Raspberry Pi 4B**.  
The system monitors **body temperature, heart rate, physical activity, and rumination behavior**, and sends **SMS alerts** to farmers using the **Twilio API** for early disease detection and proactive livestock management.

---

## 📖 Project Overview

Livestock health plays a crucial role in agricultural productivity and animal welfare. Traditional monitoring methods rely heavily on manual observation, which is time-consuming and often fails to detect early signs of illness.

This project proposes a **Smart Livestock Health Monitoring System** that integrates IoT sensors with embedded processing to enable:

- Continuous health monitoring  
- Real-time abnormality detection  
- Automated alert generation  
- Remote monitoring without farmer presence  

The system is implemented as a **wearable neckband** for cattle and is suitable for both small- and medium-scale farms.

---

## ✨ Key Features

- 🌡️ Body Temperature Monitoring using DHT11  
- ❤️ Heart Rate Monitoring using MAX30102  
- 🐾 Activity and Rumination Analysis using MPU6050 accelerometer  
- 📩 SMS Alerts via Twilio API  
- ⚙️ Local Data Processing on Raspberry Pi (reduced cloud dependency)  
- ⏱️ Periodic alerts (configurable, default: every 60 minutes)  
- 🧩 Modular, scalable, and maintainable codebase  

---

## 🏗️ System Architecture

### Core Components

- Raspberry Pi 4B (Central Processing Unit)  
- DHT11 Temperature Sensor  
- MAX30102 Heart Rate Sensor  
- MPU6050 Accelerometer and Gyroscope  
- Wi-Fi for SMS alert transmission  

### Functional Flow

1. Sensor initialization using GPIO and I2C  
2. Real-time data acquisition  
3. Signal processing and classification  
4. Normal and abnormal condition detection  
5. SMS alert transmission to the farmer  

---

## 🛠️ Hardware Requirements

- Raspberry Pi 4B  
- DHT11 Temperature Sensor  
- MAX30102 Heart Rate Sensor  
- MPU6050 Accelerometer  
- Jumper wires and power supply  
- Stable Wi-Fi connection  

---

## 💻 Software Requirements

- Raspberry Pi OS  
- Python 3.x  
- I2C and GPIO interfaces enabled  
- Required Python libraries  

---

## 📦 Python Dependencies

All required dependencies are listed in the `requirements.txt` file.

### Main Libraries Used

- RPi.GPIO  
- dht11  
- smbus  
- numpy  
- scipy  
- twilio  

---

## ⚙️ System Setup

### Enable I2C on Raspberry Pi

Enable the I2C interface from Raspberry Pi configuration under Interface Options.

### Configure Twilio Credentials

Edit the following file:

src/alerts/twilio_alert.py  

Add the required Twilio credentials:
- Account SID  
- Auth Token  
- Sender phone number  
- Receiver phone number  

---

## ▶️ Running the Project

Run the main Python file from the project root directory.

Once executed, the system will:

- Read real-time sensor data  
- Classify livestock health conditions  
- Detect abnormal patterns  
- Send SMS alerts when necessary  

---

## 🚨 Alert Logic

An SMS alert is triggered when any of the following conditions are detected:

- Body temperature exceeds the normal threshold  
- Heart rate falls outside the safe range  
- Abnormal physical activity or rumination behavior  

### Alert Message Includes

- Body temperature value  
- Heart rate in BPM  
- Activity or rumination status  

---

## 📄 Conference Publication

This project was presented at the **International Conference on Computing, Communication and Sustainable Energy Technologies**, organized by the **Department of Electronics and Communication Engineering, Galgotias College of Engineering**.

### Paper Title

IoT Enabled Smart Livestock Health Monitoring System

---

## 📊 Applications

- Smart agriculture  
- Precision livestock farming  
- Early disease detection  
- Remote cattle monitoring  
- Farm productivity optimization  

---

## 🔮 Future Enhancements

- Machine learning based disease prediction  
- Cloud-based analytics dashboard  
- GPS-based cattle tracking  
- Multi-animal scalability  
- Additional health sensors such as respiration and hydration  

---

## 👩‍💻 Author

Priyadharshini V  

---

## 📜 License

This project is released under the **MIT License**.  
Free to use for academic and research purposes with proper citation.
