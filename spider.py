import requests

url = "http://www.shef.com/statements/delaymarket_all.html"

response = requests.get(url)

print(response.text)
