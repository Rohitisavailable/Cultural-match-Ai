# CultureMatch AI 🌍✨

CultureMatch AI is a powerful AI-driven application that helps you discover and compare cultural compatibility between countries using data and insights from Qloo and OpenAI APIs.

## 🔍 What It Does

- 🌐 Compare two countries on cultural traits like food, music, fashion, and entertainment
- 🤖 Leverages Qloo’s cultural graph API and OpenAI's natural language understanding
- 🧠 Provides insights into cultural similarities and differences

## 🚀 Live Demo

Coming soon or [host your own on Streamlit](https://streamlit.io/)

## 📦 Built With

- [Streamlit](https://streamlit.io/) – for building interactive web apps in Python
- [OpenAI API](https://platform.openai.com/) – for language understanding
- [Qloo API](https://qloo.com/) – for cultural data and recommendations
- [python-dotenv](https://pypi.org/project/python-dotenv/) – for environment variable management (for local dev)

## 📁 Project Structure

culturematch-ai/
├── culturematch_ai.py # Main Streamlit app
├── requirements.txt # Python dependencies
├── .env (or Streamlit secrets) # API keys (not committed)
└── README.md # You're here!
## 🧪 Setup & Run Locally

1. **Clone the repo**
   git clone https://github.com/Rohitisavailable/Cultural-match-Ai.git
   cd culturematch-ai

   
2. **Install dependencies**

  pip install -r requirements.txt

3. **Run the app**
   streamlit run culturematch_ai.py


🌟 Inspiration
We wanted to build something that bridges cultural gaps using AI. CultureMatch AI was inspired by the idea of discovering how seemingly different countries may share surprising similarities.

🤯 Challenges
Understanding Qloo’s API data structure

Managing multiple async API responses in real-time

Handling deployment secrets on Streamlit Cloud

💡 What's Next
🌍 Support for more than two countries

📊 Graph-based visualizations

🧑‍🤝‍🧑 Community-based culture similarity voting
