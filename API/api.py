import requests

def pobierz_dane_z_api(nip):
    url = f'https://wl-api.mf.gov.pl/api/search/nip/{nip}?date=2022-01-01'
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Sprawdza, czy zapytanie zakończyło się sukcesem
        
        dane_firmy = response.json()
        
        # Wyświetlanie pobranych danych
        print("Nazwa firmy:", dane_firmy['result']['company']['name'])
        print("Adres:", dane_firmy['result']['company']['address'])
        print("NIP:", dane_firmy['result']['company']['nip'])
        
    except requests.exceptions.HTTPError as errh:
        print ("HTTP Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print ("Something went wrong:", err)

if __name__ == "__main__":
    # Wprowadź numer NIP firmy, dla której chcesz pobrać dane
    nip_do_pobrania = input("Podaj numer NIP firmy: ")
    
    pobierz_dane_z_api(nip_do_pobrania)
