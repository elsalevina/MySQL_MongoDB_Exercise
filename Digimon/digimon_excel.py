from bs4 import BeautifulSoup
import requests

url = "http://digidb.io/digimon-list/"
html = requests.get(url)
soup = BeautifulSoup(html.content, "html.parser")

# find table where the data is located
table = soup.find(id="digiList")

# find labels in 'table'
label = []
for i in table.find_all('th'):
    label.append(i.text)
label.insert(1, 'Img Src')

# find img & get img src in 'table'
img = []
for i in table.find_all('img'):
    img.append(i.get('src'))

# find data in 'table'
data = []
for i in table.find_all('td'):
    data.append(i.text)

# find data (per column) in 'data'
num = []
indexnum = list(range(0,len(data),13))
digimon = []
indexdigimon = list(range(1,len(data),13))
stage = []
indexstage = list(range(2,len(data),13))
type = []
indextype = list(range(3,len(data),13))
attr = []
indexattr = list(range(4,len(data),13))
memory = []
indexmemory = list(range(5,len(data),13))
slot = []
indexslot = list(range(6,len(data),13))
hp = []
indexhp = list(range(7,len(data),13))
sp = []
indexsp = list(range(8,len(data),13))
atk = []
indexatk = list(range(9,len(data),13))
def_ = []
indexdef_ = list(range(10,len(data),13))
int_= []
indexint_ = list(range(11,len(data),13))
spd= []
indexspd= list(range(12,len(data),13))

for i in range(len(data)):
    if i in indexnum:
        num.append(data[i][1:])
    elif i in indexdigimon:
        digimon.append(data[i][2:])
    elif i in indexstage:
        stage.append(data[i])
    elif i in indextype:
        type.append(data[i])
    elif i in indexattr:
        attr.append(data[i])
    elif i in indexmemory:
        memory.append(data[i])
    elif i in indexslot:
        slot.append(data[i])
    elif i in indexhp:
        hp.append(data[i])
    elif i in indexsp:
        sp.append(data[i])
    elif i in indexatk:
        atk.append(data[i])
    elif i in indexdef_:
        def_.append(data[i])
    elif i in indexint_:
        int_.append(data[i])
    elif i in indexspd:
        spd.append(data[i])

# make a dictionary list containing all data
datadigimon = []
for i in range(len(num)):
    datadigimon.append({
        label[0] : num[i],
        label[1] : img[i],
        label[2] : digimon[i],
        label[3] : stage[i],
        label[4] : type[i],
        label[5] : attr[i],
        label[6] : memory[i],
        label[7] : slot[i],
        label[8] : hp[i],
        label[9] : sp[i],
        label[10] : atk[i],
        label[11] : def_[i],
        label[12] : int_[i],
        label[13] : spd[i]
    })


''' CONVERT TO EXCEL '''
import xlsxwriter

book = xlsxwriter.Workbook('digimon.xlsx')
sheet = book.add_worksheet('List Digimon')

# write label
for i in range(len(label)):
    sheet.write(0,i,label[i])
# write data in table
col = 0
row = 1
for i in range(len(datadigimon)):
    for j in datadigimon[i]:
        sheet.write(row, col, datadigimon[i][j])
        col += 1
    col = 0
    row += 1
book.close()