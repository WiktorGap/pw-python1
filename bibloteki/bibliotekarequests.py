import requests

#wykonanie żądania GET:

resposne = requests.get("https://www.example.com")
print(resposne.text)
# Kod wysyła żądanie get i zwróci odpowiedź w formie tekstu 

#przekazywanie parametrów do zapyatania GET:

payload = {'param1': 'value1', 'param2':'value2'}
resposne = requests.get('https://www.example.com', params=payload)
print(resposne.json())

#parametry są dodawane do URL-a

#Wysyłanie danych w zapytaniu POST:

data = {'key1': 'value1', 'key2': 'value2'}
response = requests.post("https://www.example.com/api", data=data)
print(response.json())

#Ten kod przedstawia, jak wysłać dane w zapytaniu POST. 
#Dane mogą być przekazywane jako słownik, a także jako ciąg znaków JSON.

#Obsługa nagłówków 

headers_custom = {'User-agent': 'my-app'}
resposne = requests.get('https://www.example.com',headers=headers_custom )
print(response.text)


#Nagłówki mogą być używane do przekazywania dodatkowych informacji w zapytaniu, takich jak dane autoryzacyjne czy informacje o kliencie


#Obsługa odpowiedzi i błędów HTTP:

try:
    resposne = requests.get('https://www.example.com')
    resposne.raise_for_status()  #sprawdza czy zapytanie zakończyło się sukcesem
    print(resposne.text)

except requests.exceptions.HTTPError as errh:
    print("HTTP Error:", errh)
except requests.exceptions.ConnectionError as errc:
    print("Error Connecting:", errc)
except requests.exceptions.Timeout as errt:
    print("Timeout Error:", errt)
except requests.exceptions.RequestException as err:
    print("Something went wrong:", err)

#Przesyłanie plików
    
files_dt = {'file':('filename.txt', open("filename.txt",'rb' ))}
    #Otwiera plik o nazwie 'filename.txt' w trybie binarnym ('rb'). 
    #To oznacza, że plik jest otwarty do odczytu w formie binarnej
    #Tworzymy słownik, w którym klucz to 'file', a wartość to krotka zawierająca nazwę pliku ('filename.txt') oraz otwarty plik w trybie binarnym. 
    #Ten słownik będzie używany jako parametr files w zapytaniu POST.
response = requests.post("https://www.example.com/upload", files=files_dt)
print(response.text)


#Obsługa sesji:

with requests.Session() as session:
    session.get("https://www.example.com/login", params={'user': 'username', 'password': 'password'})
    response = session.get("https://www.example.com/dashboard")
    print(response.text)

    #Session pozwala na utrzymanie trwałego stanu sesji pomiędzy różnymi zapytaniami. 
    #W tym przykładzie, użytkownik loguje się na stronie, a następnie dostaje się na stronę nawigacyjną. 
    #Sesja automatycznie obsługuje ciasteczka (cookies) i inne aspekty trwałego połączenia.


#Obsługa ciasteczek(Cookies):
    

    cookies ={'user': 'username', 'token': 'token_value'}
    response = requests.get("https://www.example.com", cookies=cookies)


    #Możesz ręcznie przekazać ciasteczka do zapytania, co jest przydatne, gdy chcesz utrzymać sesję pomiędzy różnymi żądaniami.

#Obsługa autoryzacji
    
    auth = ("username", "password")
    response = requests.get("https://www.example.com", auth=auth)
    print(response.text)


    #Opcja auth pozwala przekazać dane autoryzacyjne do zapytania, na przykład przy użyciu podstawowej autoryzacji HTTP (Basic Authentication).

#Ustawienia proxy
    
    proxies = {'http': 'http://proxy.example.com', 'https': 'https://proxy.example.com'}
    #Tworzymy słownik proxies, w którym klucze 'http' i 'https' to schematy protokołów HTTP i HTTPS, 
    #a wartości to adresy serwerów proxy, przez które chcemy przekierować zapytanie. 
    #W tym przypadku, zapytanie HTTP ('http') zostanie przekierowane przez serwer proxy o adresie 'http://proxy.example.com', 
    #a zapytanie HTTPS ('https') przez serwer proxy o adresie 'https://proxy.example.com'.

    response = requests.get("https://www.example.com", proxies=proxies)
    #Linia ta wykonuje zapytanie GET do strony "https://www.example.com", przy użyciu wcześniej skonfigurowanych serwerów proxy zapisanych w słowniku proxies. 
    #Moduł requests automatycznie przekazuje to zapytanie przez odpowiedni serwer proxy, zgodnie z ustawieniami przekazanymi w słowniku proxies
    print(response.text)