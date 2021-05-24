import gzip
import json
import requests
import io
import re
import mmap

pattern = re.compile(r'WARC-Type[\s\S]*091labs.com[\s\S]*WARC-Type')
datafile = 'CC-MAIN-20150226074100-00147-ip-10-28-5-156.ec2.internal.warc.wet.gz'
arhic
with open(datafile, 'rb') as f:
    with mmap.mmap(f.fileno(), 0,
                   access=mmap.ACCESS_READ) as mapped:
            gzipfile = gzip.GzipFile(mode="r", fileobj=mapped)
        # for match in pattern.findall(m):
        #     print(match[1].replace(b'\n', b' '))
    data = f.read()
    data = data.decode()
    print(data[:1000])



matches = pattern.finditer(data)

for match in matches:
    print(match)
# raw_string = r"{}".format(string)
# https://stackoverflow.com/questions/18707338/print-raw-string-from-variable-not-getting-the-answers

