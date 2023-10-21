from hashlib import sha256
from requests import get, post
import json

res = get("https://hackattic.com/challenges/mini_miner/problem?access_token=b53b9d130f72e759")
val = res.json()
# val = {'difficulty': 13, 'block': {'nonce': None, 'data': [['c1756447470efeb1a0722350049f06fe', -75], ['fc75e54b6b9e3de8d74c53b2c6b5e41b', -99], ['11b5624990dc41e5293bbc3aedfca7f1', 51], ['5f15c67d8c930505d971d2b329c88060', -49]]}}
nonce = 0
data = {
  'data': val['block']['data'],
  'nonce': 0
}
diff = "0"*3
get_hstr = lambda obj: json.dumps(obj).replace(' ', '').encode()
print('started mining for difficulty', val['difficulty'], data)
hstr = sha256(get_hstr(data)).hexdigest()
while not hstr.startswith(diff):
  data['nonce'] += 1
  hstr = sha256(get_hstr(data)).hexdigest()
post_res = post("https://hackattic.com/challenges/mini_miner/solve?access_token=b53b9d130f72e759", json={'nonce': data['nonce']})
print(post_res.json())