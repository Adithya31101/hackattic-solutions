from requests import get, post
import hashlib
import hmac
import scrypt
from base64 import b64decode

res = get('https://hackattic.com/challenges/password_hashing/problem?access_token=b53b9d130f72e759')
data = res.json()
# data = {'password': 'nds09813-0508551', 'salt': '01ZOI7ni/FWJIYXaJ7E=', 'pbkdf2': {'rounds': 600000, 'hash': 'sha256'}, 'scrypt': {'N': 131072, 'r': 8, 'p': 4, 'buflen': 32, '_control': 'b19a18ea8a50a861d08eb94be602f6cbfe67ab98d2021400a3b83fbe3b8ba698'}}
salt = b64decode(data['salt'])
password = bytes(data['password'].encode())
results = {
  "sha256": hashlib.sha256(password).hexdigest(),
  "hmac": hmac.new(salt, msg=password, digestmod=hashlib.sha256).hexdigest(),
  "pbkdf2": hashlib.pbkdf2_hmac(data['pbkdf2']['hash'], password, salt, data['pbkdf2']['rounds']).hex(),
  "scrypt": scrypt.hash(password=password, salt=salt, N=data['scrypt']['N'], r=data['scrypt']['r'], p=data['scrypt']['p'], buflen=data['scrypt']['buflen']).hex()
}
print(results)
postRes = post("https://hackattic.com/challenges/password_hashing/solve?access_token=b53b9d130f72e759", json=results)
print(postRes.json())