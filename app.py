import streamlit as st
import pandas as pd
import joblib


model = joblib.load("linear_model.pkl")
feature_columns = joblib.load("feature_columns.pkl")

st.title("Movie Success Prediction")

budget = st.number_input("Budget ($ Millions)", min_value=1.0, value=50.0)
director_pop = st.slider("Director Popularity", 0.0, 10.0, 5.0)
cast_pop = st.slider("Cast Popularity", 0.0, 10.0, 5.0)
marketing = st.number_input("Marketing Spend ($ Millions)", min_value=0.0, value=20.0)
trailer_views = st.number_input("Trailer Views", min_value=0, value=10_000_000)
month = st.slider("Release Month", 1, 12, 6)
genre = st.selectbox("Genre", ['Action','Comedy','Drama','Horror','Romance','Sci-Fi','Thriller'])

if st.button("PREDICT"):

    # Prepare input row
    input_data = {
        'budget': budget,
        'director_popularity': director_pop,
        'cast_popularity': cast_pop,
        'release_month': month,
        'marketing_spend': marketing,
        'trailer_views': trailer_views
    }

    for col in feature_columns:
        if col.startswith("genre_"):
            g = col.replace("genre_", "")
            input_data[col] = 1 if genre == g else 0

    input_df = pd.DataFrame([input_data])[feature_columns]


    predicted_revenue = model.predict(input_df)[0]


    roi = predicted_revenue / budget

    st.divider()
    st.write(f"💰 **Predicted Revenue:** ${predicted_revenue:.2f}M")
    st.write(f"📊 **ROI:** {roi:.2f}x")


    if roi >= 2.5:
        st.success("🎉 STATUS: HIT 🚀")

    elif roi >= 2.0:
        st.warning("🍿 STATUS: AVERAGE")

    else:
        st.error("📉 STATUS: FLOP")
