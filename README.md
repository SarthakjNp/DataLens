# 📊 DataLens  — Understand Your Data Instantly

DataLens is a lightweight, web-based data analysis tool that allows users to upload any CSV file and instantly explore, visualize, and clean their data — without writing a single line of code.

> Built as part of a "Build in Public" challenge to create real, usable AI-powered tools.

---

## 🚀 Features

### 📂 Upload & Preview

* Upload any CSV dataset
* Instant preview of rows, columns, and data types

### 📊 Automated EDA

* Dataset shape and column information
* Missing value detection (count + percentage)
* Statistical summary for numerical features

### 🔥 Correlation Analysis

* Heatmap for numerical relationships
* Helps identify strong feature dependencies

### 📈 Interactive Visualizations

* Select column dynamically
* Choose plot type:

  * Histogram
  * Box Plot
  * Count Plot

### 🧠 Smart Insights

* Detects:

  * High missing values
  * Skewed distributions
  * Strong correlations
* Provides human-readable observations

### 🧹 Data Cleaning Tools

* Drop missing values
* Fill missing values (mean / median / mode)
* Remove duplicates

### 📥 Export

* Download cleaned dataset instantly

---

## 🧱 Tech Stack

* **Frontend/UI:** Streamlit
* **Backend:** Python
* **Data Processing:** Pandas, NumPy
* **Visualization:** Matplotlib, Seaborn

---

## 📂 Project Structure

```
DataLens/
│── app.py                # Main Streamlit app
│── utils/
│   ├── eda.py           # Data analysis functions
│   ├── insights.py      # Rule-based insight engine
│   ├── cleaning.py      # Data cleaning utilities
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/your-username/DataLens.git
cd DataLens
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the application

```
streamlit run app.py
```

---

## 🌐 Deployment

This project can be deployed easily using:

* Streamlit Cloud
* Render / Railway (for scaling later)

---

## 🧠 Key Insight

Most machine learning projects fail not because of bad models,
but because of poor data understanding.

DataLens AI focuses on:

> **Clarity before complexity**

---

## 🔮 Future Improvements

* LLM-based dataset explanation ("Explain my data")
* Auto feature engineering suggestions
* API support for integration
* Large dataset handling (chunking / backend scaling)
* User authentication + saved sessions

---

## 🤝 Contributing

Contributions are welcome.
Feel free to fork, improve, and open a pull request.

---

## 📌 Author

**Sarthak Jain**
AI & Data Science Student | ML Engineer | AI Enthusiast

---

## 📢 License

This project is open-source and available under the MIT License.

---

## ⭐ Final Note

This is not just a project.
It is a step toward building **real, usable AI systems**.

If you find it useful, consider giving it a ⭐ on GitHub.
