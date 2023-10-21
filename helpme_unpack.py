import base64
import requests
import struct
res = requests.get("https://hackattic.com/challenges/help_me_unpack/problem?access_token=b53b9d130f72e759")
val = res.json()
print("Got string", val['bytes'])
b_arr = base64.b64decode(val['bytes'])
# b_arr = base64.b64decode("wCn5g5l8BfkwKAAAiOJ9QV6GAx4OZ/k/P/lnDh4Dhl4=")
results = {
  'int':  struct.unpack('i', b_arr[:4])[0], # 4
  'uint': struct.unpack('I', b_arr[4:8])[0], # 4
  'short': struct.unpack('h', b_arr[8:10])[0], # 2
  'float': struct.unpack('f', b_arr[12:16])[0], # 4
  'double': struct.unpack('d', b_arr[16:24])[0], # 8
  'big_endian_double': struct.unpack('!d', b_arr[24:32])[0] # 8
}
print(results)
postRes = requests.post('https://hackattic.com/challenges/help_me_unpack/solve?access_token=b53b9d130f72e759', json=results)
print(postRes.json())

