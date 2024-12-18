# test_models.py

from models import add_subscribers, get_subscribers, log_newsletter, get_newsletters

# Test adding a subscriber
print("Adding subscriber...")
result = add_subscribers("makasare@usc.edu")
print(result)

# Test retrieving subscribers
print("Fetching subscribers...")
subscribers = get_subscribers()
print(subscribers)

# Test logging a newsletter
print("Logging a newsletter...")
result = log_newsletter("This is second newsletter.")
print(result)

# Test retrieving newsletters
print("Fetching newsletters...")
newsletters = get_newsletters()
print(newsletters)
