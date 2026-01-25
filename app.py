import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# Load the trained model and feature list
model = joblib.load('linear_model.pkl')
feature_columns = joblib.load('feature_columns.pkl')

# Load dataset for visualization purposes
@st.cache_data
def load_data():
    return pd.read_csv('pre_release_movie_revenue_dataset_2decimals.csv')

df = load_data()

st.set_page_config(page_title="Movie Revenue Predictor", layout="wide")

st.title("🎬 Movie Revenue Prediction App")
st.write("Predict movie revenue based on pre-release metrics using your Linear Regression model.")

# Sidebar for user inputs
st.sidebar.header("Input Movie Details")

budget = st.sidebar.number_input("Budget ($M)", min_value=0.0, value=100.0)
director_pop = st.sidebar.slider("Director Popularity", 0.0, 10.0, 5.0)
cast_pop = st.sidebar.slider("Cast Popularity", 0.0, 10.0, 5.0)
release_month = st.sidebar.slider("Release Month", 1, 12, 6)
marketing_spend = st.sidebar.number_input("Marketing Spend ($M)", min_value=0.0, value=20.0)
trailer_views = st.sidebar.number_input("Trailer Views", min_value=0, value=50000000)

# Genre selection (handles Action as baseline automatically)
genre = st.sidebar.selectbox("Genre", ['Action', 'Comedy', 'Drama', 'Horror', 'Romance', 'Sci-Fi', 'Thriller'])

# Prepare input data for prediction
input_data = {
    'budget': budget,
    'director_popularity': director_pop,
    'cast_popularity': cast_pop,
    'release_month': release_month,
    'marketing_spend': marketing_spend,
    'trailer_views': trailer_views
}

# Add dummy variables for genre (logic matches drop_first=True)
for col in feature_columns:
    if col.startswith('genre_'):
        genre_name = col.replace('genre_', '')
        input_data[col] = 1 if genre == genre_name else 0

# Convert to DataFrame with correct column order
input_df = pd.DataFrame([input_data])[feature_columns]

# Prediction and Output
if st.button("Predict Revenue"):
    prediction = model.predict(input_df)[0]
    
    st.success(f"### Predicted Revenue: ${prediction:,.2f} Million")
    
    # Graphs Section
    st.divider()
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("### Prediction vs Market Distribution")
        fig, ax = plt.subplots()
        sns.histplot(df['revenue'], kde=True, ax=ax, color='gray')
        ax.axvline(prediction, color='red', linestyle='--', label='Your Prediction', linewidth=2)
        ax.set_title("Where your movie sits in the dataset")
        plt.legend()
        st.pyplot(fig)
        
    with col2:
        st.write("### Model Coefficients (Impact)")
        coef_df = pd.DataFrame({
            'Feature': feature_columns,
            'Impact': model.coef_
        }).sort_values(by='Impact', ascending=True)
        
        fig2, ax2 = plt.subplots()
        sns.barplot(data=coef_df, x='Impact', y='Feature', ax=ax2, palette='coolwarm')
        st.pyplot(fig2)

else:
    st.info("👈 Enter details in the sidebar and click 'Predict' to see results.")

#..................................................................................................


st.title("🎬 Movie Success Prediction (2.5x Rule)")

# User inputs
budget = st.number_input("Budget ($ Millions)", min_value=1.0, value=50.0)
predicted_revenue = st.number_input(
    "Predicted Revenue ($ Millions)", min_value=0.0, value=120.0
)

# Button
if st.button("PREDICT STATUS"):

    break_even = 2.5 * budget
    roi = predicted_revenue / budget

    st.write(f"ROI: **{roi:.2f}x**")

    # ---- SIMPLE IF ELSE ----
    if predicted_revenue >= break_even:
        st.success("🎉 STATUS: HIT 🚀")

    elif predicted_revenue >= (2.0 * budget):
        st.warning("🍿 STATUS: AVERAGE")

    else:
        st.error("📉 STATUS: FLOP")