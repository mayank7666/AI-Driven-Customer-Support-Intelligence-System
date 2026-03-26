import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(page_title="Beastlife Dashboard", layout="wide")

# -------------------------------
# Load Data
# -------------------------------
df = pd.read_csv("data.csv")

# Load model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# -------------------------------
# Title
# -------------------------------
st.title("📊 Beastlife Customer Support Intelligence")
st.markdown("AI-powered dashboard to analyze customer issues and automate responses.")

# -------------------------------
# Metrics Section
# -------------------------------
col1, col2, col3 = st.columns(3)

total_queries = len(df)
top_issue = df['Category'].value_counts().idxmax()
unique_categories = df['Category'].nunique()

col1.metric("Total Queries", total_queries)
col2.metric("Top Issue", top_issue)
col3.metric("Categories", unique_categories)

st.markdown("---")

# -------------------------------
# Charts Section
# -------------------------------
col1, col2 = st.columns(2)

counts = df['Category'].value_counts()

# Pie Chart
with col1:
    st.subheader("Issue Distribution")
    fig, ax = plt.subplots()
    counts.plot(kind='pie', autopct='%1.1f%%', ax=ax)
    ax.set_ylabel("")
    st.pyplot(fig)

# Bar Chart
with col2:
    st.subheader("Most Frequent Issues")
    fig2, ax2 = plt.subplots()
    counts.plot(kind='bar', ax=ax2)
    ax2.set_xlabel("Category")
    ax2.set_ylabel("Count")
    plt.xticks(rotation=45)
    st.pyplot(fig2)

st.markdown("---")

# -------------------------------
# Insights Section
# -------------------------------
st.subheader("Key Insights")

st.write(f"- A large portion of queries are related to **{top_issue}**, indicating a need for better tracking visibility.")
st.write("- Delivery-related issues suggest gaps in communication and logistics updates.")
st.write("- Refund and product-related concerns highlight areas for process and quality improvement.")
st.write("- Many queries are repetitive and can be automated using AI-based responses.")

st.markdown("---")

# -------------------------------
# AI Query Section
# -------------------------------
st.subheader("🤖 AI Query Assistant")

st.info(" You can select a sample query or type your own.")

# Sample queries
sample_queries = [
    "Where is my order?",
    "I want a refund",
    "My delivery is late",
    "Payment failed",
    "Product is damaged",
    "How to use this product?"
]

# Dropdown
selected_query = st.selectbox("Choose a sample query:", ["-- Select --"] + sample_queries)

# Manual input
custom_query = st.text_input("Or type your own query:")

# Final query selection
query = custom_query if custom_query else selected_query

if query and query != "-- Select --":
    vec = vectorizer.transform([query])
    pred = model.predict(vec)[0]

    st.success(f"Predicted Category: {pred}")

    # Auto response system
    responses = {
        "Order Tracking": "You can track your order from your account dashboard.",
        "Delivery Delay": "We are checking your delivery status. It will be updated shortly.",
        "Refund Request": "Your refund request can be initiated from the orders section.",
        "Product Issue": "Please share product details/images for quick support.",
        "Payment Failure": "Kindly retry payment or use another method.",
        "Subscription Issue": "You can manage your subscription from settings.",
        "General Query": "Our support team will assist you soon."
    }

    st.info(f"Suggested Response: {responses.get(pred, 'Support team will contact you soon.')}")