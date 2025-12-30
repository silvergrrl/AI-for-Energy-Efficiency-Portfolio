
# ⚡ Predictive Maintenance for Grid Components

## 🌍 Overview
This project focuses on predicting failures and detecting anomalies in grid infrastructure components such as transformers and substations using IoT sensor data and machine learning. By enabling proactive maintenance, utilities can reduce downtime, improve reliability, and optimise energy efficiency.

---

## 🏗 Architecture
images/predictive-maintenance-architecture.png

### **Workflow**
1. **Data Sources**
   - IoT Sensor Data: Vibration, temperature, load measurements.
   - Historical Maintenance Logs: Failure records and repair history.

2. **Data Preprocessing**
   - Time-series segmentation and normalisation.
   - Label anomalies and failure events for supervised learning.

3. **Model Training**
   - Anomaly Detection: Isolation Forest, Autoencoders.
   - Predictive Models: LSTM for failure prediction based on time-series data.

4. **Evaluation**
   - Metrics: Precision, Recall, F1-score for anomaly detection.
   - Compare anomaly detection vs predictive modelling approaches.

5. **Deployment**
   - Real-time streaming via **Azure IoT Hub**.
   - Alerts and dashboards using **Streamlit** or **Power BI**.

6. **User Interface**
   - Visual dashboard showing component health and failure predictions.
   - Automated alerts for maintenance teams.

---

## ✅ Features
- Real-time anomaly detection from IoT sensor streams.
- Predictive modelling for proactive maintenance scheduling.
- Integration with cloud IoT services for scalability.
- Interactive dashboard for actionable insights.

---

## 🛠 Tech Stack
- **Language:** Python  
- **Libraries:** Pandas, Scikit-learn, TensorFlow/PyTorch  
- **Cloud:** Azure IoT Hub, Azure Machine Learning  
- **Visualisation:** Streamlit, Power BI  

---

## 📈 Impact
- Reduces unexpected failures and downtime.
- Improves grid reliability and energy efficiency.
- Demonstrates advanced ML skills in anomaly detection and time-series analysis.

---

## 📂 Repository Structure
