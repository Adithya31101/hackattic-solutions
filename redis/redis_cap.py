from requests import get, post
from os import system
from base64 import b64decode
import csv
import json
import datetime

res = get("https://hackattic.com/challenges/the_redis_one/problem?access_token=b53b9d130f72e759")
val = res.json()
print(val['requirements'])
binrdb = b64decode(val['rdb'])
check_type_of = val['requirements']['check_type_of']

with open('dump1.rdb', 'wb+') as fd:
  fd.write(b"REDIS0" + binrdb[6:])
system('rdb -c memory ./dump1.rdb -f mem.csv')

dbs = set()
emoji = None
expiry = None
typeofkey = None

system('rdb --command json ./dump1.rdb -f keys.json')
keyList = None
with open('keys.json') as fd:
  keyList = json.load(fd)

keys = {}
for keyblob in keyList:
   for k in keyblob.keys():
      keys[k] = keyblob[k]

with open('mem.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        dbs.add(row['database'])
        if ord(row['key'][0]) > 10000:
          emoji = row['key']
        if row['key'] == check_type_of:
          typeofkey = row['type']
        if row['expiry'] and row['expiry'] != "":
          expiry = datetime.datetime.strptime(row['expiry'], "%Y-%m-%dT%H:%M:%S.%f")
resJson = {
   "db_count": len(dbs),
   "emoji_key_value": keys[emoji],
   "expiry_millis": int(expiry.timestamp() * 1000),
   check_type_of: typeofkey
}

print(resJson['expiry_millis'])

resPost = post("https://hackattic.com/challenges/the_redis_one/solve?access_token=b53b9d130f72e759", json=resJson)
print(resPost.json())