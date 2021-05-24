import gzip
import json
import requests
import io

# Let's fetch the Common Crawl FAQ using the CC index
resp = requests.get('http://index.commoncrawl.org/CC-MAIN-2015-11-index?url=wikipedia.org&output=json&limit=1')

pages = [json.loads(x) for x in resp.text.strip().split('\n')]
# Multiple pages may have been found - we're only interested in one
page = pages[0]
print(pages)
print(resp.text)
# If we print this, we'll see the JSON representation of the response
# Most important is the file path to read and the location within the large file that the GZIP response exists
print ('JSON response from index.commoncrawl.org')
print ('---')
print (page)
print ('---')

# We need to calculate the start and the end of the relevant byte range
# (each WARC file is composed of many small GZIP files stuck together)
offset, length = (int(page['offset'])), int(page['length'])
offset_end = offset + length - 1
# We'll get the file via HTTPS so we don't need to worry about S3 credentials
# Getting the file on S3 is equivalent however - you can request a Range
prefix = 'https://commoncrawl.s3.amazonaws.com/'
# We can then use the Range header to ask for just this set of bytes
#resp = requests.get(prefix + page['filename'], headers={'Range': 'bytes={}-{}'.format(offset, offset_end)})
resp = requests.get('https://commoncrawl.s3.amazonaws.com/crawl-data/CC-MAIN-2015-11/segments/1424936460472.17/wet/CC-MAIN-20150226074100-00147-ip-10-28-5-156.ec2.internal.warc.wet.gz')#, headers={'Range': 'bytes=0-9000000'})
# The page is stored compressed (gzip) to save space
# We can extract it using the GZIP library
#print(resp.content)
#type(resp.content)
raw_data = resp.content
f = gzip.decompress(raw_data)
data = f.decode()
# What we have now is just the WARC response, formatted:
#data = f.read()
print(data)
#warc = data.strip().split('\r\n\r\n', 2)
#
print ('WARC headers')
print ('---')
#print (warc[:100])
print ('---')
print ('HTTP headers')
print ('---')
#print (header[:100])
print ('---')
print ('HTTP response')
print ('---')
#print (response[:100])