import json
from typing import Any

j ={
  "imie": "John",
  "nazwisko": "Doe",
  "wiek": 30,
  "miasto": "Nowy Jork",
  "czy_ubezpieczony": True,
  "ulubione_kolory": ["czerwony", "zielony", "niebieski"]
}

#zamiana pythona na jsona

x = json.dumps(j)

#print(x)

m = '{"imie": "John", "nazwisko": "Doe", "wiek": 30, "miasto": "Nowy Jork", "czy_ubezpieczony": true, "ulubione_kolory": ["czerwony", "zielony", "niebieski"]}'

k = json.loads(m)  #zmiana json na python s-oznacza string przy loads
print(k)


with open("plik.json" ,"r") as file:
    data = json.load(file)

# load wycztuje dane z pliku do python
    

#moj_obiekt został zapisany do pliku w formacie json
moj_obiekt = {"imie": "Jan", "wiek": 25, "miasto": "Warszawa"}
with open("plik.json" , "w") as file:
    json.dump(moj_obiekt,file,indent=2)

class MyEncoder(json.JSONEncoder)
    def default(self, o: Any) -> Any:
        return super().default(o)

