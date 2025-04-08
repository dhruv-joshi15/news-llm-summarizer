
# News Summarizer using GPT

This is a simple Streamlit app that scrapes or loads sample news and summarizes them using OpenAI's GPT-3.5 model.

## Features
- Loads dummy or live news articles
- Uses LLM (OpenAI) to summarize each news item in 2 lines
- Clean and simple UI built with Streamlit

## Setup Instructions

1. Clone the repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file using the template below:

```env
OPENAI_API_KEY=your-openai-key
```

4. Run the app:

```bash
streamlit run app.py
```

## Example Output

> **Title**: Scientists discover new species  
> **Summary**: A new species of frog has been discovered in the Amazon rainforest, showcasing biodiversity still being uncovered.

---

✅ Built by Dhruv Joshi
