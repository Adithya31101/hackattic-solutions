import base64
import requests
from os import system
res = requests.get("https://hackattic.com/challenges/backup_restore/problem?access_token=b53b9d130f72e759")
val = res.json()
with open('dump.gz', 'wb+') as fd:
  fd.write(base64.b64decode(val['dump']))
system("gunzip dump.gz")
content = ""
fd = open('dump', 'r')
alive_ssns = []
for line in fd:
  if line[0].isdigit():
    vals = line.split('\t')
    if vals[7].strip() == 'alive':
      alive_ssns.append(vals[3])
print(alive_ssns)
fd.close()
post_res = requests.post('https://hackattic.com/challenges/backup_restore/solve?access_token=b53b9d130f72e759', json={'alive_ssns': alive_ssns})
print(post_res.json())