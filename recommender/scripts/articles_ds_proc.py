import pymongo
import gensim
import gensim.downloader as api
import re
import csv
import sys, ctypes as ct
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import time

csv.field_size_limit(int(ct.c_ulong(-1).value // 2))

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

files = ["C:\\Main Contents\\Python progs\\crawl_gp\\datasets\\articles\\articles1.csv",
"C:\\Main Contents\\Python progs\\crawl_gp\\datasets\\articles\\articles2.csv",
"C:\\Main Contents\\Python progs\\crawl_gp\\datasets\\articles\\articles3.csv"]
url_counter = 0
long_counter = 0
article_text = ""
start = time.time()
for filename in files:
    with open(filename, "r", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for number, row in enumerate(csv_reader):
           
            is_long = False
            text = re.sub(r"[^a-zA-Z0-9]+", ' ', row["content"])
            tokens = []
            if (len(text) - text.count(" ")) > 9000:
                long_counter += 1
                is_long = True

            for word in text.split():   
                if len(word) < 2:
                    continue           
                tokens.append(word)
                
            # tokens_without_sw = [word for word in tokens if not word in stopwords.words()]
            article = {"id": str(number), "title": row["title"], 
            "publication": row["publication"],
            "pub_date": row["date"], "pub_year": row["year"], "pub_month": row["month"],
            "url": row["url"], "content": tokens, "is_long": is_long}
            if row["url"] != "":
                url_counter +=1
            article_text = row["content"]
            articles.insert_one(article)
           

end = time.time()
print("Время обработки одного текстов:", end-start)
print(url_counter)
print(f"Long articles: {long_counter}")
print(article_text)

# mydict = { "name": "John", "address": "Highway 37" }

# x = mycol.insert_one(mydict)

# dataset = api.load("20-newsgroups")
# # data = [d["data"].split() for d in dataset]
# docs = 0
# for number, d in enumerate(dataset): 
#     document = d["data"]
#     document.replace("\n", " ")   
#     # document = re.sub("\>|\^|\*|\<|\\|\/|\-|\?|\$|\%|\(\|\)|\#\@|\&", '', document)
#     # document = re.sub(r"[^a-zA-Z0-9]+", ' ', document)
#     text = "\n".join(document.split("\n")[4:])
#     topic = get_topic(document)
#     if topic == 0:
#         continue
#     if len(text) < 500:
#         continue
#     list_of_words = []
#     for word in text.split():
#         cleared_word =  re.sub(r"[^a-zA-Z0-9]+", ' ', word)
#         list_of_words.append(word)
#     # head_pattern = '(?<=From:).*?(?=Line:)'


#     article = {"id": number, "topic": topic, "content": list_of_words}
#     articles.insert_one(article)
#     docs += 1

# print(f"Valid document: {docs}")

