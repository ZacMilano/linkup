from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Replace the placeholder with your Atlas connection string
uri = "mongodb+srv://zacAdmin:Oig2jRWi9iix1sgL@linkmeupscotty.3uavg9y.mongodb.net/?retryWrites=true&w=majority&appName=LinkMeUpScotty"

# Set the Stable API version when creating a new client
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.link_me_up_scotty
                          
# Send a ping to confirm a successful connection
try:
  ping = client.link_me_up_scotty.command('ping')
  print('ping successful!' if ping['ok'] else 'ping failed.')
except Exception as e:
  print(e)
