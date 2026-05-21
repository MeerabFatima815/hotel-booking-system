import psycopg2
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get Neon database URL from .env
DATABASE_URL = os.getenv("DATABASE_URL")

# Function to connect database
def get_connection():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        print("Database connected successfully!")
        return conn
    except Exception as e:
        print("Connection failed:", e)

# Run connection test
if __name__ == "__main__":
    get_connection()