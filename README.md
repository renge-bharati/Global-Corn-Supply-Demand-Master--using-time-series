# 🌽 Global Corn Supply & Demand Forecasting App

## 📘 Project Submission (For Teacher / Examiner)

**Student Name:** Bharati Renge
**Project Title:** Global Corn Supply & Demand Forecasting Using Time Series Analysis
**Technology:** Python, Prophet, Streamlit
**Dataset Period:** 1975 – 2026

---

## 🎯 Objective of the Project

The objective of this project is to analyze historical global corn supply data and **forecast future values** using a **time series forecasting approach**. This project demonstrates the practical application of data science concepts such as:

* Data preprocessing
* Time series modeling
* Model evaluation
* Visualization
* Deployment using Streamlit

---

## 📊 Dataset Description

The dataset is sourced from **Kaggle** and contains historical global corn supply and demand information from **1975 to 2026**.

Typical columns include:

* Year / Market_Year
* Total Supply
* Total Demand
* Production
* Ending Stocks

> Note: Column names may vary; the application automatically detects the required columns.

---

## 🧠 Algorithm Used

### Prophet (Time Series Forecasting)

**Reason for Selection:**

* Suitable for yearly time series data
* Automatically handles trends and seasonality
* Easy to interpret
* Widely used in industry

The model predicts future corn supply for the next 5 years based on historical trends.

---

## ⚙️ Methodology

1. Load and explore the dataset
2. Identify year and supply-related columns
3. Convert data into time series format
4. Split data into training and testing sets
5. Train Prophet forecasting model
6. Generate future predictions
7. Evaluate performance using MAE and RMSE
8. Visualize results
9. Deploy using Streamlit

---

## 📈 Model Evaluation Metrics

The model is evaluated using:

* **MAE (Mean Absolute Error)**
* **RMSE (Root Mean Squared Error)**

These metrics help measure prediction accuracy and reliability.

---

## 🖥️ Application Interface

The Streamlit application allows the user to:

* Upload the dataset (CSV)
* View dataset preview
* Train the forecasting model
* Visualize forecast results
* View model evaluation metrics

---

## 📁 Project Structure

```
├── app.py                  # Streamlit application code
├── corn_forecast_model.pkl # Trained forecasting model
├── requirements.txt        # Required libraries
├── README.md               # Project documentation
└── data.csv                # Dataset (optional)
```

---

## ▶️ How to Run the Project

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Run the Application

```bash
streamlit run app.py
```

---

## 🌐 Deployment

The project can be deployed using **Streamlit Cloud** by connecting the GitHub repository.

---

## ✅ Conclusion

This project successfully demonstrates the use of **time series forecasting** for real-world agricultural data. The results provide meaningful insights into future corn supply trends and showcase practical implementation of data science techniques.

---

## 📜 Declaration

I hereby declare that this project is my original work and has been completed for academic purposes.

---

**Submitted By:** Bharati Renge
