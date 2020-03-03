''' MYSQL => CSV '''

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


import csv

with open("world_city.csv","w",newline='\n') as mycsv:
    label = csv.writer(mycsv, delimiter =",")
    label.writerow(["ID","Name","CountryCode","District","Population"])
    isi = csv.DictWriter(mycsv, delimiter=",", fieldnames=["ID","Name","CountryCode","District","Population"])
    isi.writerows(data1)

with open("world_country.csv", "w",newline='\n') as mycsv:       
    label = csv.writer(mycsv, delimiter = ",")
    label.writerow([
        "Code",
        "Name",
        "Continent",
        "Region",
        "SurfaceArea",
        "IndepYear",
        "Population",
        "LifeExpectancy",
        "GNP",
        "GNPOld",
        "LocalName",
        "GovernmentForm",
        "HeadOfState",
        "Capital",
        "Code2"
    ])
    isi = csv.DictWriter(mycsv, delimiter=",", fieldnames=[
        "Code",
        "Name",
        "Continent",
        "Region",
        "SurfaceArea",
        "IndepYear",
        "Population",
        "LifeExpectancy",
        "GNP",
        "GNPOld",
        "LocalName",
        "GovernmentForm",
        "HeadOfState",
        "Capital",
        "Code2"
        ])
    isi.writerows(data2)

with open("world_language.csv","w",newline='\n') as mycsv:
    label = csv.writer(mycsv, delimiter =",")
    label.writerow(["CountryCode","Language","IsOfficial","Percentage"])
    isi = csv.DictWriter(mycsv, delimiter=",", fieldnames=["CountryCode","Language","IsOfficial","Percentage"])
    isi.writerows(data3)
