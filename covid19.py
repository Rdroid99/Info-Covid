#--coding utf-8--
#salam dariku Rdroid99
#KAYA GINI DOANG SCRIPTNYA JADI MAU DIRECODE ATAU NGGA SERAH
#JANGAN LUPA KASIH BINTANG GITHUBNYA OKE HEHE:D
import json,os,sys
from urllib import request
#clear
os.system("clear")
url = "https://indonesia-covid-19.mathdro.id/api/provinsi"

# http request buat buka link cok asu nentod lu:v
response = request.urlopen(url)

# parsing data jsonnya
data = json.loads(response.read())
print("")
#COVID DATA
print("INFO PERKEMBANGAN COVID19 PROVINSI DI INDO")
print("")
for covid in data['data']:
    print("      ======================= ")
    print(f"     |- {covid['provinsi']}:|")
    print("========================================")
    print(f"|🤒Positif Covid: {covid['kasusPosi']}")
    print("========================================")
    print(f"|🙂Sembuh  Covid: {covid['kasusSemb']}")
    print("========================================")
    print(f"|💀Meninggal    : {covid['kasusMeni']}")
    print("========================================")
    print("")
