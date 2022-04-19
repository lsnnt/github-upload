import requests
url="https://asnapi.com/api/"
resp=requests.get(url)
last=resp.text.find("\":{",11)
print(last)
ip = resp.text[13:last]
print(f"your ip is {ip}")
f=open('log/ip.log','a')
f.writelines(f"{ip}\n")
f.close()
