from requests import get, post
from os import system

res = get("https://hackattic.com/challenges/trivial_filing/problem?access_token=b53b9d130f72e759").json()['files']

for fname in res.keys():
  with open(fname, 'w') as fd:
    fd.write(res[fname])
print("Created files")
system("sudo chown -R nobody /tftpboot")
resPost = post("https://hackattic.com/challenges/trivial_filing/solve?access_token=b53b9d130f72e759", json={
  "tftp_host": "ec2-44-197-242-70.compute-1.amazonaws.com",
  "tftp_port": 69
})

print(resPost.json())