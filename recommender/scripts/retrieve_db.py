import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/recommender")
db = client["database"]
articles = db["articles"]

# myquery = { "id": { "$gt": 17500 } }

myquery = { "id": 100 }
mydoc = articles.find(myquery)

for x in mydoc:
  print(x)

print(articles.estimated_document_count())