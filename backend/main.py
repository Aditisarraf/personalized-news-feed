from fastapi import FastAPI
import requests

# Create FastAPI instance
app = FastAPI()

# Root route - just a welcome message
@app.get("/")
def read_root():
    return {"message": "Welcome to Personalized News Feed"}


# --------------------------
# NewsAPI Integration
# --------------------------

# 🔑 API key for NewsAPI (replace with your actual key)
NEWS_API_KEY = "17c61798ab5f4736b4b6ae19f723b7d1"

# 🌍 Endpoint to fetch top US headlines from NewsAPI
NEWS_URL = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"

# Route to fetch latest news articles
@app.get("/news")
def get_news():
    """
    Fetch top news headlines from NewsAPI and return articles.
    """
    response = requests.get(NEWS_URL)         # Call the external API
    data = response.json()                    # Convert response to JSON
    return {"articles": data.get("articles", [])}  # Return only articles
