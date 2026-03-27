# 🔐 AI-Powered SOC Alert Analysis System

## 📌 Overview
This project simulates a **Security Operations Center (SOC)** using AI to automate **log analysis, threat detection, and incident reporting**.

It demonstrates how **AI can transform cybersecurity operations** by reducing manual effort and improving response time.

---

## 🏗️ System Architecture
![Architecture](images/architecture.png)

---

## 🔄 Data Flow
![Data Flow](images/dataflow.png)

---

## 🚨 Sample Use Case
![Use Case](images/usecase.png)

---

## 🎯 Key Features
- 🔍 Log ingestion from system and network sources  
- 🚨 Threat detection using rules and anomaly patterns  
- 🤖 AI-based alert classification and prioritisation  
- 📝 Automated incident report generation  

---

## 🛠️ Tech Stack
- Python  
- Wireshark / tshark  
- Linux  
- LLM APIs (GPT / Claude)  

---

## 🌍 Real-World Relevance
- Simulates **actual SOC workflows**
- Covers **end-to-end security pipeline**
- Demonstrates **AI + Cybersecurity integration**

---

## 📄 Project Documentation
👉 [View Full Project (PDF)](docs/Lopamudra_AI_SOC_System.pdf)

---

## 👩‍💻 About Me
**Lopamudra Panigrahi**  
Software Test Engineer → Transitioning into AI & Cybersecurity  

---

## 🚀 What This Shows
- System design thinking  
- Real-world problem solving  
- Ability to apply AI in security workflows  
- End-to-end SOC pipeline simulation  

---

## 🔬 Demo — End-to-End Flow

### 📥 Sample Input Logs
```
Mar 27 10:01:12 Failed password from 192.168.1.105
Mar 27 10:01:15 Failed password from 192.168.1.105
Mar 27 10:01:18 Failed password from 192.168.1.105
```
👉 Full logs available in: data/sample_logs.txt

---

### 🚨 Detection Output
```json
{
  "event_type": "Brute Force Attack",
  "source_ip": "192.168.1.105",
  "severity": "HIGH"
}
```

👉 Full output available in: output/detection.json


---

### AI Incident Summary
```
Brute Force Attack detected from 192.168.1.105
Severity: CRITICAL
Recommendation: Block IP and review logs

```

