''' MYSQL => JSON '''

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

import json

with open ('world_city.json','w') as myjson1 :
    json.dump(data1, myjson1)

with open ('world_country.json','w') as myjson2 :
    json.dump(data2, myjson2)

with open ('world_countrylanguage.json','w') as myjson3 :
    json.dump(data3, myjson3)
