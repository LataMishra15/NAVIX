# 🚗NAVIX

### AI-Powered Navigation During GNSS/GPS Outages

RoadSense Fusion AI is a hybrid navigation system designed to maintain reliable position and motion estimation when GNSS/GPS becomes unavailable, degraded, or unreliable.

Instead of depending on GPS alone, the system combines **smartphone IMU sensors, AI-based motion estimation, Kalman filtering, and map constraints** to reduce navigation drift during GNSS outages.

## 🎯 Problem

GNSS/GPS can become unreliable in:

* Tunnels
* Urban canyons
* Dense infrastructure
* Signal-blocked environments
* GNSS interference or outages

Traditional inertial dead reckoning works without GPS but accumulates error over time.

## 💡 Solution

RoadSense Fusion AI combines:

**IMU → Inertial Navigation → AI Motion Estimation → Adaptive EKF → Map Matching → Confidence-Aware Position**

The system can:

* Detect GNSS degradation
* Simulate GNSS outages
* Estimate motion using IMU
* Use AI to improve velocity estimation
* Fuse multiple measurements using Error-State EKF
* Constrain trajectories using road maps
* Estimate navigation confidence and uncertainty
* Detect rough-road events
* Recover smoothly when GNSS returns

## 🧠 Core Technologies

| Component       | Technology                       |
| --------------- | -------------------------------- |
| Language        | Python 3.11+                     |
| Data Processing | NumPy, Pandas, SciPy             |
| AI/ML           | PyTorch, Scikit-learn            |
| Navigation      | INS + Error-State EKF            |
| Geospatial      | PyProj, Shapely                  |
| Map Data        | OpenStreetMap / Local Road Graph |
| UI              | Streamlit                        |
| Visualization   | Plotly, Matplotlib               |
| Testing         | Pytest                           |
| Version Control | Git + GitHub                     |

## 🏗️ Architecture

```text
Sensor / Dataset
       ↓
Data Preprocessing
       ↓
GNSS Quality Monitor
       ↓
 ┌───────────────┐
 │ IMU → INS     │
 │ IMU → AI GRU  │
 └───────┬───────┘
         ↓
   Adaptive EKF
         ↓
   Map Matching
         ↓
Confidence & Uncertainty
         ↓
   Navigation UI
```

## 📊 Evaluation

The system compares:

1. GNSS-only
2. Classical INS
3. AI-assisted INS
4. EKF Fusion
5. EKF + Map Matching
6. Full RoadSense Fusion

Key metrics:

* Position Error
* RMSE
* Final Drift
* Drift %
* Velocity Error
* Heading Error
* Recovery Time
* AI Inference Latency

## 🚀 MVP

The first version is a **Python desktop prototype** that can load recorded sensor data, simulate GNSS outages, run the navigation pipeline, and visualize the resulting trajectory and performance.
