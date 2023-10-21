from requests import get, post
from os import system
from subprocess import check_output
import json

res = get("https://hackattic.com/challenges/dockerized_solutions/problem?access_token=b53b9d130f72e759").json()
username = res['credentials']['user']
password = res['credentials']['password']
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print(f"Creating auth password digest for {username} and {password}")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("IGNITION KEY: ", res['ignition_key'])
system(f"docker run --entrypoint htpasswd httpd:2 -Bbn {username} {password} > auth/htpasswd")
print("Created password file in auth/htpasswd")

print("Spinning up the repository")
system("""
docker run -d \
  -e REGISTRY_HTTP_ADDR=0.0.0.0:443 \
  -p 443:443 \
  --name registry \
  -v "$(pwd)"/auth:/auth \
  -e "REGISTRY_AUTH=htpasswd" \
  -e "REGISTRY_AUTH_HTPASSWD_REALM=Registry Realm" \
  -e REGISTRY_AUTH_HTPASSWD_PATH=/auth/htpasswd \
  -v "$(pwd)"/certs:/certs \
  -e REGISTRY_HTTP_TLS_CERTIFICATE=/certs/fullchain.pem \
  -e REGISTRY_HTTP_TLS_KEY=/certs/privkey.pem \
  registry:2
""")

print("Repo running, triggering the push from hackattic!")
resPost = post(f"https://hackattic.com/_/push/{res['trigger_token']}", json={
  "registry_host": "docker.animonic.xyz"
}).json()
print(resPost)
curlRes = check_output(f'curl -X GET -u {username}:{password} https://docker.animonic.xyz/v2/_catalog', shell=True)
repo = json.loads(curlRes[:-1].decode())['repositories'][0]
print("Repository Found, Name:", repo)
tagsCurlRes = check_output(f'curl -X GET -u {username}:{password} https://docker.animonic.xyz/v2/{repo}/tags/list', shell=True)
tags = json.loads(tagsCurlRes[:-1].decode())['tags']
print("Here are the tags", tags)
system(f"docker login -u {username} -p {password} docker.animonic.xyz")
for tag in tags:
  output = check_output(f"docker run -e 'IGNITION_KEY={res['ignition_key']}' docker.animonic.xyz/{repo}:{tag}")
  print(output)

val = input("Enter the right Value")
finalRes = post("https://hackattic.com/challenges/dockerized_solutions/solve?access_token=b53b9d130f72e759", json={
  "secret": secret
}).json()
print(finalRes)
# system("docker run ")