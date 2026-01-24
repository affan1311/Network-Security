from pymongo import MongoClient
from urllib.parse import quote_plus
from pymongo.server_api import ServerApi

username = quote_plus("affanhyder6_db_user")
password = quote_plus("Affan321")  

uri = f"mongodb+srv://{username}:{password}@cluster0.vfyhdqn.mongodb.net/?appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command("ping")
    print("Connected successfully!")
except Exception as e:
    print("Error:", e)
