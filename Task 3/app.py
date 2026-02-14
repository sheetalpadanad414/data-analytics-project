import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page Title
st.title("Titanic Survival Analysis")

# Load dataset
df = pd.read_csv("titanic.csv")   # make sure file name matches exactly

# Show dataset
st.subheader("Dataset Preview")
st.write(df.head())

# Convert survived column to readable format
df["survived"] = df["survived"].map({0: "Not Survived", 1: "Survived"})

# Survival Count
st.subheader("Survival Count")
survival_count = df["survived"].value_counts()
st.write(survival_count)

# Plot survival chart
st.subheader("Survival Chart")
fig, ax = plt.subplots()
survival_count.plot(kind="bar", ax=ax)
plt.xlabel("Survival Status")
plt.ylabel("Count")
st.pyplot(fig)

# Survival by Gender
st.subheader("Survival by Gender")
gender_survival = pd.crosstab(df["sex"], df["survived"])
st.write(gender_survival)

fig2, ax2 = plt.subplots()
gender_survival.plot(kind="bar", ax=ax2)
plt.xlabel("Gender")
plt.ylabel("Count")
st.pyplot(fig2)
