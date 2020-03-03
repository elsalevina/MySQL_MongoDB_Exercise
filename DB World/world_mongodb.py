''' MYSQL => MONGODB '''

# Ambil data dari MySQL
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


# Memasukkan data ke MongoDB
import pymongo
urldb = "mongodb://127.0.0.1:27017"
mongoku = pymongo.MongoClient(urldb)
# buat database
dbku = mongoku['World1']    
# buat collection
city = dbku['city']
country = dbku['country']
lang = dbku['language']    

kirim1 = city.insert_many(data1)
kirim2 = country.insert_many(data2)
kirim3 = lang.insert_many(data3)
