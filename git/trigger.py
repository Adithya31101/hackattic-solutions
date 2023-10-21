from requests import get, post
from os import system

res = get("https://hackattic.com/challenges/hosting_git/problem?access_token=b53b9d130f72e759")
data = res.json()
print('--------------')
print(f"/bin/bash adduser.sh {data['username']}'")
print('--------------')

print()
print('--------------')
print(f"./creategit.sh {data['username']} '{data['ssh_key']}' '{data['repo_path']}'")
print('--------------')

input("All setup??")
print("Triggering push to remote server")

resPost1= post(f"https://hackattic.com/_/git/{data['push_token']}", json={"repo_host": "ec2-18-208-152-58.compute-1.amazonaws.com"})
print(resPost1.json())
input("Shall I clone??")

cloneCmd = (f'git clone {data["username"]}@ec2-18-208-152-58.compute-1.amazonaws.com:{data["repo_path"]}')
print(f"\n{cloneCmd}\n")
system(cloneCmd)

fname = data['repo_path'].split('/')[1].replace('.git', '')
secret = ""
with open(fname + "/solution.txt", 'r') as fd:
  secret = fd.read()

resPose2 = post("https://hackattic.com/challenges/hosting_git/solve?access_token=b53b9d130f72e759", json={"secret": secret})
print(resPose2.json())
