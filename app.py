import streamlit as st
import pandas as pd

st.title("Pokémon Data Viewer")

# Load your filtered CSV
df = pd.read_csv("output/filtered_pokemon.csv")

# Simple filter
min_exp = st.slider("Minimum Base Experience", 0, 300, 100)
filtered = df[df["base_experience"] >= min_exp]

st.write(f"Showing Pokémon with base_experience ≥ {min_exp}")
st.dataframe(filtered)
