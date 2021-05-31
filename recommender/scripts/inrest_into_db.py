import pymongo
import gensim
import gensim.downloader as api
import re

def get_topic(document):
    topic_pattern = '(?s)(?<=Subject:).*?(?=Organization)'
    try:
        topic = re.findall(topic_pattern , document.replace("\n", " "))[0]
    except:
        return 0

    topic = topic.replace("Re:", "").strip()
    return topic

client = pymongo.MongoClient("mongodb://localhost:27017/recommender")
db = client["database"]
articles = db["articles"]
articles.drop()


# mydict = { "name": "John", "address": "Highway 37" }

# x = mycol.insert_one(mydict)

dataset = api.load("20-newsgroups")
# data = [d["data"].split() for d in dataset]
docs = 0
for number, d in enumerate(dataset): 
    document = d["data"]
    document.replace("\n", " ")   
    # document = re.sub("\>|\^|\*|\<|\\|\/|\-|\?|\$|\%|\(\|\)|\#\@|\&", '', document)
    # document = re.sub(r"[^a-zA-Z0-9]+", ' ', document)
    text = "\n".join(document.split("\n")[4:])
    topic = get_topic(document)
    if topic == 0:
        continue
    if len(text) < 500:
        continue
    list_of_words = []
    for word in text.split():
        cleared_word =  re.sub(r"[^a-zA-Z0-9]+", ' ', word)
        list_of_words.append(word)
    # head_pattern = '(?<=From:).*?(?=Line:)'


    article = {"id": number, "topic": topic, "content": list_of_words}
    articles.insert_one(article)
    docs += 1

print(f"Valid document: {docs}")

