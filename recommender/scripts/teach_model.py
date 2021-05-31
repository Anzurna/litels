import pymongo
import gensim
from gensim.test.utils import get_tmpfile
import time

def create_tagged_document(list_of_list_of_words):
    for i, list_of_words in enumerate(list_of_list_of_words):
        yield gensim.models.doc2vec.TaggedDocument(list_of_words, [i])

def elapse_gensim_time(t_data, vec_size=50, min=2, eps = 5, window=5):
    start = time.time()
    model = gensim.models.doc2vec.Doc2Vec(vector_size=vec_size, min_count=min, epochs=eps)
    model.build_vocab(t_data)
    model.train(t_data, total_examples=model.corpus_count, epochs=model.epochs)
    end = time.time()
    return {"vec_size": vec_size, "epochs": eps, "time": end-start}


client = pymongo.MongoClient("mongodb://localhost:27017/recommender")
db = client["database"]
articles = db["articles"]

cursor = articles.find()
cursor2 = articles.find()

for document in cursor:
    print(document)
    break

def yield_doc(cursor):
    for i, document in enumerate(cursor):
        yield gensim.models.doc2vec.TaggedDocument(document["content"], [i])


# test = [print(doc) for doc in yield_doc(cursor)]

start = time.time()
model = gensim.models.doc2vec.Doc2Vec(vector_size=300, min_count=3, epochs=10, window=5)
# model.build_vocab([gensim.models.doc2vec.TaggedDocument(doc, [i]) for i, doc in enumerate(cursor)])
# model.train([gensim.models.doc2vec.TaggedDocument(doc, [i]) for i, doc in enumerate(cursor)],
#  total_examples=model.corpus_count, epochs=model.epochs, window=5)
model.build_vocab(yield_doc(cursor))
model.train(yield_doc(cursor2), total_examples=model.corpus_count, epochs=model.epochs)
end = time.time()
print("Время обучения:", end-start)

f = get_tmpfile(r"C:\Main Contents\Python progs\crawl_gp\litels\recommender\scripts\doc_2_vec_model")
with open("model2", "wb+") as file:
    # fname = get_tmpfile("model")
    model.save(f)

