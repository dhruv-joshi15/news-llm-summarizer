
import streamlit as st
import requests
import os

st.set_page_config(page_title="News Summarizer", layout="centered")

st.title("🗞️ News Summarizer using GPT")

# Load API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Dummy news for fallback
dummy_news = [
    {"title": "OpenAI launches new model", "content": "OpenAI has announced the release of a more powerful AI model today."},
    {"title": "Global markets rally", "content": "Stock markets around the world are surging amid economic optimism."},
    {"title": "Scientists discover new species", "content": "Researchers in the Amazon have discovered a previously unknown frog species."}
]

def fetch_news():
    # Replace with NewsAPI or real API if needed
    return dummy_news

def summarize(text):
    if OPENAI_API_KEY:
        try:
            import openai
            openai.api_key = OPENAI_API_KEY
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Summarize the following news article in 2 lines."},
                    {"role": "user", "content": text}
                ]
            )
            return response['choices'][0]['message']['content']
        except Exception as e:
            return f"Error: {str(e)}"
    else:
        return "Summary (dummy): " + text[:60] + "..."

news_list = fetch_news()

for news in news_list:
    st.subheader(news['title'])
    st.write("📰", news['content'])
    with st.spinner("Summarizing..."):
        summary = summarize(news['content'])
    st.success(summary)
    st.markdown("---")
