# Movie-Revenue-Prediction-using-Machine-Learning
Developed a machine learning solution to predict movie revenue using key production and performance attributes such as genre, runtime, ratings, votes, and metascore. The project focused on building a robust regression pipeline covering data preprocessing, feature engineering, model training, and evaluation.
# 🎬 Movie Revenue & Success Prediction using Machine Learning

This repository contains an end-to-end Machine Learning project that predicts a movie’s expected box-office revenue using pre-release attributes and determines whether the movie will be a **Hit**, **Average**, or **Flop** based on a simple business rule. The system also includes an interactive **Streamlit web application** for real-time predictions and visualization.

---

## 🚀 Project Overview

The project uses a regression-based Machine Learning approach to estimate movie revenue from factors such as:

* Budget
* Director popularity
* Cast popularity
* Release month
* Marketing spend
* Trailer views
* Genre (one-hot encoded)

A trained model is then integrated into a Streamlit application where users can enter movie details and instantly receive:

* Predicted revenue
* Visual comparison with market distribution
* Movie success status (Hit / Average / Flop)

---

## 🧠 Machine Learning Model

* Algorithm Used: Random Forest Regressor / Linear Regression (baseline)
* Task Type: Regression
* Target Variable: Revenue (in millions)

### Evaluation Metrics

* R² Score ≈ 92%
* Mean Absolute Percentage Error (MAPE)

Random Forest is well-suited for capturing non-linear relationships and complex feature interactions, making it ideal for this problem.

---

## 🎯 Movie Success Classification (2.5x Rule)

After predicting revenue, the movie is classified using the following logic:

* If Revenue ≥ 2.5 × Budget → **HIT**
* If Revenue ≥ 2.0 × Budget → **AVERAGE**
* Else → **FLOP**

This provides a simple but practical business-oriented interpretation of model output.

---

## 🗂️ Project Structure

```
movie-revenue-prediction/
│
├── project1.ipynb                  # Model training notebook
├── app.py                          # Streamlit application
├── linear_model.pkl                # Saved trained model
├── feature_columns.pkl             # Feature list used during training
├── pre_release_movie_revenue_dataset_2decimals.csv
├── requirements.txt
└── README.md
```

---

## 🖥️ Streamlit Application Features

* Sidebar inputs for movie attributes
* Revenue prediction button
* Revenue distribution visualization
* Feature impact visualization
* Movie success classification

### App Interface Sections

1. Movie Revenue Prediction
2. Visualization Panel
3. Movie Success Prediction (2.5x Rule)

---

## ⚙️ Installation & Setup

1. Clone the repository

```
git clone https://github.com/yourusername/movie-revenue-prediction.git
cd movie-revenue-prediction
```

2. Install dependencies

```
pip install -r requirements.txt
```

3. Run the Streamlit app

```
streamlit run app.py
```

---

## 📦 Required Libraries

* Python 3.10+
* pandas
* numpy
* scikit-learn
* streamlit
* joblib
* matplotlib
* seaborn

---

## 📊 Example Input Features

* Budget ($M)
* Director Popularity (0–10)
* Cast Popularity (0–10)
* Release Month (1–12)
* Marketing Spend ($M)
* Trailer Views
* Genre

---

## 🔮 Future Improvements

* Hyperparameter tuning
* More features (social media trends, reviews, franchise info)
* Deep Learning models
* Cloud deployment
* API-based prediction service

---

## 👨‍💻 Author

Joel Pradeep Abraham

---

⭐ If you found this project useful, consider starring the repository!

