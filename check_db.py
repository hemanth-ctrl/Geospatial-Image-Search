from pymongo import MongoClient

try:
    client = MongoClient("mongodb://localhost:27017/")
    
    # This forces connection
    client.server_info()
    
    print("MongoDB connected successfully ")
    
except Exception as e:
    print("Connection failed ")
    print(e)