import streamlit as st
import pickle
import matplotlib.pyplot as plt

# Load trained model
model = pickle.load(open("model/spam_model.pkl", "rb"))
vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))

# Sidebar
st.sidebar.title("AI Scam Detector")
st.sidebar.write("This tool analyzes messages and detects possible scams.")

st.sidebar.write("### Instructions")
st.sidebar.write("1. Enter a message")
st.sidebar.write("2. Click Analyze")
st.sidebar.write("3. View scam risk analysis")

# Main title
st.title("🔍 AI Scam Message Detection Dashboard")

st.write("Analyze SMS or text messages to detect potential scams using Machine Learning.")

# Input
message = st.text_area("Enter the message to analyze")

# Suspicious keyword list
suspicious_words = [
    "free","win","winner","prize","click","money",
    "urgent","offer","claim","reward","lottery"
]

if st.button("Analyze Message"):

    if message.strip() == "":
        st.warning("Please enter a message.")
    else:

        # Convert message into features
        data = vectorizer.transform([message])

        # Prediction
        prediction = model.predict(data)[0]
        probability = model.predict_proba(data)[0][1]

        # Display result
        if prediction == 1:
            st.error("⚠ Scam Message Detected")
        else:
            st.success("✅ Safe Message")

        # Risk meter
        st.subheader("Fraud Risk Level")
        st.progress(probability)

        risk_percent = probability * 100
        st.write(f"Risk Score: {risk_percent:.2f}%")

        # Risk category
        if risk_percent < 30:
            st.success("Risk Level: LOW")
        elif risk_percent < 70:
            st.warning("Risk Level: MEDIUM")
        else:
            st.error("Risk Level: HIGH")

        # Suspicious words
        detected_words = [word for word in suspicious_words if word in message.lower()]

        if detected_words:
            st.subheader("Suspicious Words Detected")
            st.write(detected_words)

        # Message explanation
        st.subheader("Message Analysis")

        if prediction == 1:
            st.write("This message contains patterns commonly associated with scam or spam messages.")
        else:
            st.write("The message appears to be normal communication.")

        # Risk visualization chart
        st.subheader("Risk Visualization")

        safe_prob = 1 - probability

        labels = ["Safe", "Scam"]
        values = [safe_prob, probability]

        fig, ax = plt.subplots()
        ax.pie(values, labels=labels, autopct="%1.1f%%")
        ax.set_title("Scam Probability Distribution")

        st.pyplot(fig)