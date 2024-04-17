import json
import requests

response = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL")
print("--------------------------------------------------------")
moedasDict = json.loads(response.content)
print(moedasDict["USDBRL"].get("ask"))
print("--------------------------------------------------------")
responseEUR = requests.get("https://economia.awesomeapi.com.br/json/last/EUR-BRL")
moedasDict.update(responseEUR.json())
print(moedasDict.get("EURBRL").get("ask"))