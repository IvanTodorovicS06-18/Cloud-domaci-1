import http.client
import json

conn = http.client.HTTPSConnection("getpantry.cloud")
predmet = ["web programiranje","web dizajn","sql programiranje"]
class kontakt: 
    adresa = "Beogradska 4",
    mesto = "Beograd",
    telefon = "062 111 7777"

kon = kontakt()

payload = json.dumps({
  "id" : "666777",
  "ime": "Ivan",
  "prezime":"Todorovic",
  "smer": "Informacione tehnologije",
  "predmet": predmet,
  "prosek" : "8.0",
  "kontakt": [kon.adresa,kon.mesto,kon.telefon] 

})
headers = {
  'Content-Type': 'application/json'
}
conn.request("POST", "/apiv1/pantry/a8c43ec4-7481-4780-97e2-2dd9a157a9db/basket/Ivan", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))