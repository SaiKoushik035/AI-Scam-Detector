# AI Scam Message Detection Dashboard

An AI-powered system that detects scam or fraudulent SMS messages using Machine Learning and Natural Language Processing (NLP).

This application analyzes text messages and predicts whether the message is **Safe** or **Scam**.

## Live Demo
https://ai-scam-detector-wukyc9vywzt4jwrqdorq2j.streamlit.app

## Features
- Detects scam or spam SMS messages
- Real-time message analysis
- Fraud risk score visualization
- Suspicious keyword detection
- Interactive web dashboard

## Technologies Used
- Python
- Machine Learning
- Natural Language Processing (NLP)
- Scikit-learn
- Streamlit
- Pandas
- Matplotlib

## How It Works
1. User enters a message.
2. The text is converted into numerical features using **TF-IDF vectorization**.
3. A trained **machine learning model** analyzes the message.
4. The system predicts whether the message is **Safe** or **Scam**.
5. A fraud risk score and analysis are displayed.

## Project Structure
AI-Scam-Detector │ ├── app.py ├── requirements.txt ├── spam_model.pkl ├── vectorizer.pkl ├── python_train_model.py ├── python_prepare_dataset.py └── README.md
