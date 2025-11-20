# Energy Consumption Forecasting — Time Series Modeling

## Overview
This project develops a baseline forecasting model for daily energy consumption using synthetic time-series data with realistic seasonal patterns. It demonstrates core time-series concepts such as trend modeling, seasonality analysis, and evaluation with MAPE.

---

## Objectives
- Generate synthetic energy load data
- Explore trend, weekly cycles, and annual seasonality
- Implement a naive seasonal forecast baseline
- Produce forecast visualizations and accuracy metrics

---

## Project Structure
```
energy-consumption-forecasting/
│
├── data/
│   └── synthetic/              # Generated energy time series
│
├── src/
│   ├── data/
│   │   └── generate.py         # Synthetic load generator
│   └── models/
│       └── train.py            # Naive seasonal forecast + plots
│
└── reports/
    └── figures/                # Forecast charts
```

---

## Methods

### **1. Synthetic Data**
Combines:
- Linear upward trend  
- Weekly cycle  
- Annual seasonality  
- Gaussian noise  

### **2. Train/Test Split**
80/20 chronological split to mimic real forecasting constraints.

### **3. Baseline Model**
A naive seasonal forecast repeats the previous week’s pattern:
```
forecast[t] = load[t - 7]
```

### **4. Evaluation**
Metric:
- **MAPE** (Mean Absolute Percentage Error)

Plot:
- Actual vs. forecasted load

---

## How to Run

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Generate Data
```bash
python src/data/generate.py
```

### Train & Forecast
```bash
python src/models/train.py
```

---

## Key Results
- Baseline model establishes expected forecast accuracy  
- Seasonal patterns visually explain predictability  
- Provides a foundation for ARIMA, Prophet, or LSTM models  

---

## Future Improvements
- Add ARIMA/Prophet forecasting models  
- Perform decomposition (trend/seasonal/residual)  
- Add weather covariates  
- Build multi-step forecasts with confidence intervals  

---

## License
MIT License

