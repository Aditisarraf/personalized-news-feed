"""
database.py
------------
This file sets up the database connection and session management 
for the Personalized News Feed project using SQLAlchemy ORM.

- Defines the database URL (PostgreSQL in this case).
- Creates a connection engine.
- Creates a Session factory for queries.
- Provides a Base class for ORM models to inherit from.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# ------------------------------
# 1. Database connection URL
# ------------------------------
# Format: "dialect+driver://username:password@host:port/database_name"
# Example for PostgreSQL running locally:
# "postgresql://postgres:mysecretpassword@localhost:5432/newsfeed"
SQLALCHEMY_DATABASE_URL = "postgresql://username:password@localhost/newsfeed"


# ------------------------------
# 2. Create database engine
# ------------------------------
# The engine manages the connection pool between SQLAlchemy and the database.
# echo=True → logs SQL queries for debugging (can enable if needed).
engine = create_engine(SQLALCHEMY_DATABASE_URL)


# ------------------------------
# 3. Session factory
# ------------------------------
# Each instance of SessionLocal will be an independent database session.
# autocommit=False → changes are not auto-committed (must commit manually).
# autoflush=False → changes are not auto-flushed until commit() or query().
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# ------------------------------
# 4. Base class for models
# ------------------------------
# All ORM models (e.g., Article, User) will inherit from this Base.
# It stores metadata about tables and mappings.
Base = declarative_base()
