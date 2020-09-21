import gzip
import json
import io
import re
import mmap
import os
import warc
from pprint import pprint

data = ''
datafile = 'CC-MAIN-20150226074100-00147-ip-10-28-5-156.ec2.internal.warc.wet.gz'
# with open('text.txt', 'w', encoding="utf-8") as foil:
#     with gzip.open(datafile, 'rb') as f:
#         for line in f: 
#             data = line.decode()
#             foil.write(data)
           
# with open('text.txt', 'w') as wf:
#     wf.write(data)

text = ''  
k = 0 
pattern = re.compile(r'[\s\S]*microsoft.com[\s\S]*')
with warc.open(datafile, 'r') as f:
    for record in f:
        #pprint(vars(record.header))
        if (record.header['warc-type'] != 'warcinfo'):
            if pattern.match(record.header['warc-target-uri']):
                if (int(record.header['content-length']) > 1000):
                    text = record.payload.read()
                    print(record.header['warc-target-uri'])
                    print(int(record.header['content-length']))
                    #print(text.decode())
                    text = record.payload.read()
                    k += 1

                
        
       # 
        
        if k > 30:
            break
        #url = record.header.get('http://1023blakefm.com/pay-to-promote-facebook-posts-dollars-and-sense/', None)
        # if not url:
        #     continue
        # text = record.payload.read()
    # print(url)
    # print(text)

# with open('text.txt', 'r') as foil:
#     for line in foil:
#         print(line)
# pattern = re.compile(r'WARC-Type[\s\S]*microsoft.com[\s\S]*WARC-Type')
# with open('text.txt', 'r', encoding="utf-8") as f:
#     for line in f:
#         for match in re.finditer(pattern, line):
#             print(match)
# for match in matches:
#     print(match)
# raw_string = r"{}".format(string)
# https://stackoverflow.com/questions/18707338/print-raw-string-from-variable-not-getting-the-answers 





