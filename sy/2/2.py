import json

with open('C:/Users/93601/Code/python/sy/2/score1034.json', 'r', encoding='utf-8') as fp:
    json_data = json.load(fp)
n = int(input())
for i in range(n):
    print(json_data[i])
