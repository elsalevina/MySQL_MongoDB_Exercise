''' MONGODB => CSV '''

import pymongo

urldb = "mongodb://127.0.0.1:27017"
mongoku = pymongo.MongoClient(urldb)
dbku = mongoku["ptxyz"]   
colku = dbku['karyawan']
data = list(colku.find())
for i in range(len(data)):
    data[i]['_id'] = str(data[i]['_id'])

import csv 

with open('karyawan.csv','w',newline='\n') as mycsv :
    writer = csv.DictWriter(mycsv, delimiter =';', fieldnames = ['_id','nama','kota','usia'])
    writer.writerows([{'_id':'_id', 'nama':'nama', 'kota':'kota','usia':'usia'}])
    writer.writerows(data)
