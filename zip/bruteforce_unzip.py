from requests import get, post
from os import system
from zipfile import ZipFile
from subprocess import Popen, PIPE, run

res = get("https://hackattic.com/challenges/brute_force_zip/problem?access_token=b53b9d130f72e759")
data = res.json()
system(f"wget -O package.zip {data['zip_url']}")
result = run(["fcrackzip", '-l4-6', '-u',  '-c', 'a1', 'package.zip'], stdout=PIPE)
print("From Python", str(result.stdout))
passw = str(result.stdout).split('== ')[1].split('\\')[0]
zipf = ZipFile('package.zip')
path = zipf.extract('secret.txt', pwd=bytes(passw.encode()))
secret = ""
with open(path) as fd:
  secret = fd.read()
print(secret)

postRes = post("https://hackattic.com/challenges/brute_force_zip/solve?access_token=b53b9d130f72e759", json={
  'secret': secret[:-1]
})

print(postRes.json())

