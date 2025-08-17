"""
models.py
----------
This file defines the database models (tables) for the Personalized News Feed project.
Each model class represents a table in the database using SQLAlchemy ORM.

- Article: stores information about news articles (title, URL, published date).
More models (e.g., User, Preferences, Events) can be added later.
"""

from sqlalchemy import Column, Integer, String, DateTime
from .database import Base


# ------------------------------
# Article Model
# ------------------------------
# Represents the "articles" table in the database.
# Each instance of Article corresponds to one row in the table.
class Article(Base):
    __tablename__ = "articles"   # Table name in the database

    # Primary key column (unique ID for each article)
    id = Column(Integer, primary_key=True, index=True)

    # Title of the news article (indexed for fast search/filtering)
    title = Column(String, index=True)

    # URL of the article (unique, ensures no duplicate articles are stored)
    url = Column(String, unique=True, index=True)

    # Published date of the article (helps in sorting by recency)
    published_at = Column(DateTime)
