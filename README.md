# Smart Livestock Health Monitoring System 🐄📡

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

- 🌡️ **Body Temperature Monitoring** using DHT11  
- ❤️ **Heart Rate Monitoring** using MAX30102  
- 🐾 **Activity & Rumination Analysis** using MPU6050 accelerometer  
- 📩 **SMS Alerts** via Twilio API  
- ⚙️ **Local Data Processing** on Raspberry Pi (reduced cloud dependency)  
- ⏱️ Periodic alerts (configurable, default: every 60 minutes)  
- 🧩 Modular, scalable, and maintainable codebase  

---

## 🏗️ System Architecture

**Core Components:**
- Raspberry Pi 4B (Central Processing Unit)
- DHT11 Temperature Sensor
- MAX30102 Heart Rate Sensor
- MPU6050 Accelerometer + Gyroscope
- Wi-Fi (for Twilio-based SMS alerts)

**Functional Flow:**
1. Sensor initialization (GPIO & I2C)
2. Real-time data acquisition
3. Signal processing and classification
4. Normal/abnormal condition detection
5. SMS alert transmission

---

## 🛠️ Hardware Requirements

- Raspberry Pi 4B  
- DHT11 Temperature Sensor  
- MAX30102 Heart Rate Sensor  
- MPU6050 Accelerometer  
- Jumper wires & power supply  
- Stable Wi-Fi connection  

---

## 💻 Software Requirements

- Raspberry Pi OS
- Python 3.x
- Enabled I2C & GPIO interfaces
- Required Python libraries (see below)

---

## 📦 Python Dependencies

All dependencies are listed in `requirements.txt`.

```bash
pip install -r requirements.txt

Main libraries used:
  -RPi.GPIO
  -dht11
  -smbus
  -numpy
  -scipy  
  -twilio

---

##**⚙️ System Setup**

1️⃣ Enable I2C on Raspberry Pi
sudo raspi-config
→ Interface Options → I2C → Enable
2️⃣ Configure Twilio Credentials
Edit:
src/alerts/twilio_alert.py
and add:
  -Account SID
  -Auth Token
  -Sender & receiver phone numbers
▶️ Running the Project
python3 src/main.py

Once running, the system will:
  -Read sensor data
  -Classify health conditions
  -Detect abnormalities
  -Send SMS alerts if required

---

##**🚨 Alert Logic**

An SMS alert is triggered when:
  Body temperature exceeds normal threshold
  Heart rate falls outside safe range
  Abnormal activity or rumination pattern is detected

Alerts include:
  Temperature value
  Heart rate (BPM)
  Activity status

---

##**📄 Conference Publication**

This project has been presented in the **International Conference on Computing, Communication and Sustainable Energy Technolgies** organised by Department of Electronics and Communication Engineering By Galgotias College of Engineering on the title

**“IoT Enabled Smart Livestock Health Monitoring System”**

##**📊 Applications**
  -Smart agriculture
  -Precision livestock farming
  -Early disease detection
  -Remote cattle monitoring
  -Farm productivity optimization

##**🔮 Future Enhancements**
  -Machine learning–based disease prediction
  -Cloud dashboard for analytics
  -GPS-based cattle tracking
  -Multi-animal scalability
  -Additional health sensors (respiration, hydration)
## **👩‍💻 Author**

Priyadharshini V

##**📜 License**

This project is released under the MIT License.
Free to use for academic and research purposes with proper citation
