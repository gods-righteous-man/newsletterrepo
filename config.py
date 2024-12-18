from pymongo import MongoClient
from dotenv import load_dotenv
import os


load_dotenv() 

MONGO_URI= os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)

db = client["newsletter_app"]


EMAIL_HOST = "smtp.gmail.com"  # Example for Gmail
EMAIL_PORT = 587
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
