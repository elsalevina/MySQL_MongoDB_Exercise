''' MONGODB => JSON '''

import pymongo

urldb = "mongodb://127.0.0.1:27017"
mongoku = pymongo.MongoClient(urldb)
dbku = mongoku["ptxyz"]   
colku = dbku['karyawan']
data = list(colku.find())

import json

for i in range(len(data)):
    data[i]['_id'] = str(data[i]['_id'])
with open ('karyawan.json','w') as myjson :
    json.dump(data, myjson)