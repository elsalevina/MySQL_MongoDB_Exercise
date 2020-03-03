''' MYSQL => EXCEL '''

import mysql.connector

dbku = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'elsa',
    passwd = '12345',
    database = 'world'
)
#table city
x = dbku.cursor(dictionary = True)
x.execute('select * from city')
data1 = list(x)
#table country
y = dbku.cursor(dictionary = True)
y.execute('select * from country')
data2 = list(y)
#table countrylanguage
z = dbku.cursor(dictionary = True)
z.execute('select * from countrylanguage')
data3 = list(z)

import xlsxwriter

book = xlsxwriter.Workbook("worlddb.xlsx")
city = book.add_worksheet("City")
country = book.add_worksheet("Country")
lang = book.add_worksheet("Language")

#CITY
citykeys = list(data1[0].keys())
# label
col = 0
for i in citykeys:
    city.write(0, col, i)
    col += 1
# isi
row = 1
for i in range(len(data1)):
    col = 0
    for j in citykeys:
        city.write(row,col, data1[i][j])
        col += 1
    row += 1

#COUNTRY
countrykeys = list(data2[0].keys())
# label
col = 0
for i in countrykeys:
    country.write(0,col, i)
    col += 1
# isi
row = 1    
for i in range(0,len(data2)):
    col = 0
    for j in countrykeys:
        country.write(row,col, data2[i][j])
        col += 1
    row +=1

#LANGUAGE
langkeys = list(data3[0].keys())
# label
col = 0
for i in langkeys:
    lang.write(0,col, i)
    col += 1
# isi
row = 1    
for i in range(0,len(data3)):
    col = 0
    for j in langkeys:
        lang.write(row,col, data3[i][j])
        col += 1
    row +=1 

book.close()
