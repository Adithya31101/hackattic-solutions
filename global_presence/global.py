
from urllib.request import ProxyHandler, Request, build_opener, install_opener, urlopen
from requests import get, post
from time import sleep
import threading

CAproxies = [
  "socks4://104.248.225.143:22065",
  "socks4://186.96.147.50:4153",
  "socks4://51.222.241.8:31169",
  "socks4://201.184.159.28:5678",
  "socks4://195.168.91.238:4153",
  "socks4://148.77.34.200:54321",
  "socks4://177.234.192.45:32213",
  "socks4://187.130.139.197:37812",
  "socks4://181.129.39.58:4153",
  "socks4://174.64.125.227:5678",
  "socks4://94.253.95.241:3629",
  "socks4://5.58.66.55:14888",
  "socks4://91.203.25.28:4153",
  "socks4://190.104.26.227:33638",
  "socks4://51.161.99.114:48235",
  "socks4://217.21.148.50:33192",
  "socks4://179.97.193.250:4153",
  "socks4://177.234.244.171:32213",
  "socks4://178.210.130.89:5678",
  "socks4://82.137.245.41:1080",
  "socks4://201.159.103.97:31337",
  "socks4://186.201.31.189:4145",
  "socks4://216.154.201.132:54321",
  "socks4://94.72.158.129:4153",
  "socks4://212.174.17.57:1080",
  "socks4://187.216.144.170:5678",
  "socks4://212.79.107.116:5678",
  "socks4://213.171.44.82:3629",
  "socks4://62.103.186.66:4153",
  "socks4://195.164.138.34:1080",
  "socks4://217.197.151.182:5678",
  "socks4://91.203.165.23:5678",
  "socks4://46.171.28.162:59311",
  "socks4://211.229.254.177:28572",
  "socks4://198.89.91.90:5678",
  "socks4://36.95.48.45:1080",
  "socks4://132.148.155.180:14850",
  "socks4://187.130.139.197:37812",
  "socks4://120.42.35.90:35010",
  "socks4://120.42.35.91:35010",
  "socks4://103.30.201.39:3001",
  "socks4://47.88.104.193:23121",
  "socks4://119.148.10.54:9990",
  "socks4://213.16.81.182:35559",
  "socks4://94.253.95.241:3629",
  "socks4://186.96.147.50:4153",
  "socks4://116.229.201.36:7891",
  "socks4://119.148.50.110:9990",
  "socks4://91.213.119.246:46024",
  "socks4://201.217.51.9:4145",
  "socks4://95.31.5.29:51528",
  "socks4://110.77.145.159:4145",
  "socks4://158.69.55.204:23900",
  "socks4://109.68.189.22:54643",
  "socks4://158.69.247.89:2285",
  "socks4://156.0.229.194:42692",
  "socks4://41.223.234.116:37259",
  "socks4://82.103.118.42:1099",
  "socks4://190.104.26.227:33638",
  "socks4://212.115.232.79:10800",
  "socks4://188.163.170.130:35578",
  "socks4://190.119.62.42:18",
  "socks4://41.139.194.249:18",
  "socks4://62.73.127.98:9898",
  "socks4://163.172.147.89:16379",
  "socks4://92.255.164.166:4145",
  "socks4://200.32.105.86:4153",
  "socks4://193.105.62.11:58973",
  "socks4://159.224.243.185:61303",
  "socks4://92.241.92.218:14888",
  "socks4://192.99.244.173:5137",
]


res = get("https://hackattic.com/challenges/a_global_presence/problem?access_token=b53b9d130f72e759")
pt = res.json()['presence_token']

def make_get_call(ip):
  print("Making Proxy Call", ip)
  try:
    res = get(f"https://hackattic.com/_/presence/{pt}", proxies={
      "http": ip,
      "https": ip
    }).text

    if(len(res.split(',')) == 7):
      res = post("https://hackattic.com/challenges/a_global_presence/solve?access_token=b53b9d130f72e759", json={})
      print("%"*100)
      print(res.json())
      print("%"*100)
      exit()
  except:
    print("Something wrong with ip", ip)


for ip in CAproxies:
  threading.Thread(target=make_get_call, args=(ip,)).start()


sleep(28)