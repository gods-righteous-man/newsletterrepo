from config import db

subscribers_collection = db["subscribers"]
newsletters_collection = db["newsletters"]

def add_subscribers(email: str):

    if subscribers_collection.find_one({"email": email}):
        return {"error": "Email already subscribed."}

    subscribers_collection.insert_one({"email": email})
    return {"message" : "Subscriber added successfully."}

# to get all subscribers
def get_subscribers():
    return list(subscribers_collection.find({}, {"_id": 0, "email": 1}))


# to save the newsletters 
def log_newsletter(content: str):
    newsletters_collection.insert_one({"content": content})
    return {"message": "Newsletter logged successfully."}

# to get all newsletters
def get_newsletters():
    return list(newsletters_collection.find({}, {"_id": 0, "content": 1}))