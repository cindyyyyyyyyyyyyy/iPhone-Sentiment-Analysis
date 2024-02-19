import streamlit as st
import zipfile
import pickle
import smtplib
from email.message import EmailMessage

# Path to the zip file containing the .pkl file
zip_file_path = "sentiment_analysis_model.zip"
pkl_file_name = "sentiment_analysis_model.pkl"

# Extract the .pkl file from the zip archive
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extract(pkl_file_name)

# Load the sentiment analysis model from the extracted .pkl file
with open(pkl_file_name, 'rb') as model_file:
    model = pickle.load(model_file)

# Function to predict sentiment
def predict_sentiment(text):
    prediction = model.predict([text])
    return prediction[0]

# Function to send email
def send_email(review):
    sender_email = "your_email@gmail.com"
    receiver_email = "your_email@gmail.com"
    password = "your_email_password"

    message = EmailMessage()
    message['Subject'] = 'New Review for Your Dashboard'
    message['From'] = sender_email
    message['To'] = receiver_email
    message.set_content(review)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, password)
        smtp.send_message(message)

# Streamlit app
def main():
    st.title("Sentiment Analysis Dashboard")
    
    # Introduction tab
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Introduction", "Analysis", "Experiment", "Review"])

    if page == "Introduction":
        st.header("Introduction")
        st.write("Welcome to the Sentiment Analysis Dashboard! This dashboard allows you to analyze sentiment of text and provide feedback.")

    elif page == "Analysis":
        st.header("Analysis")
        st.write("This page is under construction.")

    elif page == "Experiment":
        st.header("Experiment")
        st.subheader("Predict Sentiment")
        text_input = st.text_area("Enter text to predict sentiment:")
        if st.button("Predict"):
            if text_input:
                sentiment = predict_sentiment(text_input)
                st.write("Predicted Sentiment:", sentiment)
            else:
                st.warning("Please enter some text.")

    elif page == "Review":
        st.header("Review")
        st.subheader("Submit Your Review")
        review_text = st.text_area("Write your review here:")
        if st.button("Submit"):
            if review_text:
                send_email(review_text)
                st.success("Thank you for your review! It has been submitted.")
            else:
                st.warning("Please write a review before submitting.")

if __name__ == "__main__":
    main()
