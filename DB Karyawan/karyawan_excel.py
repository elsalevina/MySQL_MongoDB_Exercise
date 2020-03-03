''' MONGODB => EXCEL '''

import pymongo

urldb = "mongodb://127.0.0.1:27017"
mongoku = pymongo.MongoClient(urldb)
dbku = mongoku["ptxyz"]   
colku = dbku['karyawan']
data = list(colku.find())
for i in range(len(data)):
    data[i]['_id'] = str(data[i]['_id'])

import xlsxwriter

book = xlsxwriter.Workbook("ptxyz.xlsx")
sheet = book.add_worksheet("karyawan")

row = 1
for i in range(len(data)):
    sheet.write(0,0, "_id")
    sheet.write(0,1, "nama")
    sheet.write(0,2, "kota")
    sheet.write(0,3, "usia")
    sheet.write(row, 0, data[i]['_id'])
    sheet.write(row, 1, data[i]['nama'])
    sheet.write(row, 2, data[i]['kota'])
    sheet.write(row, 3, data[i]['usia'])
    row += 1

book.close()