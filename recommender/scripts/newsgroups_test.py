import gensim
import gensim.downloader as api
import re

dataset = api.load("20-newsgroups")
data = [d["data"].split() for d in dataset]
i = 0
for d in dataset:    
    topic_pattern = '(?s)(?<=Subject:).*?(?=Organization)'
    topic = re.findall(topic_pattern , d["data"].replace("\n", " "))[0]
    topic = topic.strip().replace("Re:", "")
    print(topic)
    break
    i += 1
