import json
from typing import Any

data = {
    "imie": "Jan",
    "nazwisko": "Kowalski",
    "wiek": 30,
    "miasto": "Warszawa"
}
json_data = json.dumps(data)
print(json_data)
json_data1 = '{"imie": "Jan", "nazwisko": "Kowalski", "wiek": 30, "miasto": "Warszawa"}'
json_data4 = json.loads(json_data1)
print(json_data4)

with open("dane.json","w") as file:
    loded_data = json.load(file)

data = {"imie": "Jan", "nazwisko": "Kowalski", "wiek": 30}
json_string = json.dumps(data, indent=2, separators=";")
#zamiana pythona na format json

with open("dane.json","w") as file:
    json.dump(data,file, indent=4)
#zamiana pythona na format json ale dump zapisuje dodatkowo do pliku, oprócz zmiennej ktora formatuje potrzeba obiektu  tutaj plik do ktorego zapisujemy nasze dane

json_data = '{"imie": "Jan", "nazwisko": "Kowalski", "wiek": 30}'
data_py = json.loads(json_data)
print(json_data)
#zamiana z jsona na python

with open("dane.json", "r") as file:
    loded_data=json.load(file)
#działanie jak loads lecz load odczytuje z pliku

class MyEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        return super().default(o)

