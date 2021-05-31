import gensim
from gensim.test.utils import get_tmpfile

import pymongo
import numpy
import random

client = pymongo.MongoClient("mongodb://localhost:27017/recommender")
db = client["database"]
articles = db["articles"]

test_article = articles.find()[20000]

# with open("doc_2_vec_model", "r") as f:'
f = get_tmpfile(r"C:\Main Contents\Python progs\crawl_gp\litels\recommender\scripts\doc_2_vec_model")
model = gensim.models.Doc2Vec.load(f)

doc_vec_text = []
for i in range(0, 300):
    doc_vec_text.append(random.uniform(-0.5, 0.5))

doc_vec_text = numpy.asarray(doc_vec_text)
doc_vector = model.infer_vector(test_article["content"])
query = { 'id': "100000" }
print(doc_vector)
print(doc_vec_text)
print(type(doc_vector))
print(len(doc_vec_text))
 #int(model.docvecs.most_similar([doc_vector])[9][0])
#  similar = articles.find(query).sort("id", "100000").skip(int(query["id"]) - 2).limit(0)
most_similar_docs = model.docvecs.most_similar([doc_vec_text], topn = 20)
similar = articles.find()[int(model.docvecs.most_similar([doc_vector])[4][0])]
for doc in most_similar_docs:
    cont = articles.find()[int(doc[0])]
    print(doc[0], ":  ", cont["title"])
# similar = articles.find(query)
# print(model.docvecs.most_similar([doc_vector]))

# print(test_article)
# print(test_article["title"])
# print(" ".join(test_article["content"]))
# print()

# print(" ".join(similar["content"]))

