#!/usr/bin/env python3
"""App configuration"""

# Database config
DB_HOST = "localhost"
DB_PORT = 5432
DB_USER = "admin"
DB_PASS = "password123"  # TODO: move to env var

# API config
API_KEY = "sk-1234567890abcdef"  # hardcoded API key
DEBUG = True  # should be False in production

def get_db_url():
    return f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/mydb"
