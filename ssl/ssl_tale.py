from requests import get, post
from os import system
from base64 import b64encode

res = get("https://hackattic.com/challenges/tales_of_ssl/problem?access_token=b53b9d130f72e759")
data = res.json()
print('\n', data['required_data'], '\n')
pk = f"-----BEGIN RSA PRIVATE KEY-----\n{data['private_key']}\n-----END RSA PRIVATE KEY-----"
with open('pvt.key', 'w') as fd:
  fd.write(pk)
country_code_map = {
  "Sint Maarten": "TL",
  "Tokelau Islands": "TK",
  "Keeling Islands": 'CC',
  "Cocos Islands": "CC",
  "Christmas Island": "CX"
}
# serial_number = int(data['required_data']['serial_number'], base=16)
serial_number = data['required_data']['serial_number']
csr_cmd = (f"openssl req -key pvt.key -new -out domain.csr -subj '/C={country_code_map[data['required_data']['country']]}/CN={data['required_data']['domain']}/serialNumber={serial_number}'")

print("RUNNING:", csr_cmd)
system(csr_cmd)

system(f"openssl x509 -in domain.csr -out cert.pem -set_serial {serial_number} -req -signkey pvt.key")
system("openssl x509 -in cert.pem -inform pem -out cert.der -outform der")

bindata = ""
with open('cert.der', 'rb') as fd:
  bindata = b64encode(fd.read())
print(bindata)
resPost = post('https://hackattic.com/challenges/tales_of_ssl/solve?access_token=b53b9d130f72e759', json={
  "certificate": bindata
})

print(resPost.json())