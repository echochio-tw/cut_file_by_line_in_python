import csv

with open('2021-04-16-1300-1359_wss508.naturallove666.cn.RI.log.csv', newline='', encoding="utf-8") as f:
    reader = csv.reader(f)
    data = list(reader)

d0=0
d101=0
d503=0
d504=0
for i in data:
  if i[8] == '0':
    d0 = d0+1
  if i[8] == '101':
    d101 = d101+1
  if i[8] == '504':
    d504 = d504+1
  if i[8] == '503':
    d503 = d503+1
    
print (d0,d101,d503,d504)
