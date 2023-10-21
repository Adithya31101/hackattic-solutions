from requests import get, post
from os import system
from base64 import b64encode


res = get("https://hackattic.com/challenges/collision_course/problem?access_token=b53b9d130f72e759")
incl = res.json()["include"]

with open("x.txt", 'w') as fd: fd.write(incl)

system("docker run --rm -it -v $PWD:/work -w /work -u $UID:$GID brimstone/fastcoll --prefixfile x.txt -o msg1 msg2")
system("cat msg1 >> x.txt")
system("cat msg2 >> x.txt")
system('md5sum msg1 msg2')
ans = []

with open("msg1", 'rb') as fd: ans.append(b64encode(fd.read()))

with open("msg2", 'rb') as fd: ans.append(b64encode(fd.read()))

resPost = post('https://hackattic.com/challenges/collision_course/solve?access_token=b53b9d130f72e759', json={"files": ans})
print(resPost.json())
