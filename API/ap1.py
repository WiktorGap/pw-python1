import requests

# r = requests.get(r"https://wl-api.mf.gov.pl/#nip?date")
# print(f"Status code resposne {r}")

# text = r

# print(text)


def download_data(nip):
    url =  f'https://wl-api.mf.gov.pl/api/search/nip/{nip}?date=2022-01-01'

    try:
        resposne = requests.get(url)
        resposne.raise_for_status()



        #Próba wykonania zapytania HTTP GET za pomocą requests.get(url). response zawiera odpowiedź serwera. response.raise_for_status() sprawdza, czy odpowiedź serwera ma status kodu 2xx (co oznacza sukces). 
        #Jeśli status nie jest 2xx, zostanie wygenerowane HTTPError

        company_data = resposne.json()

        print("Company name: ",company_data['result']['company']['name'])
        print("Address: ",company_data['result']['company']['address'])
        print("NIP:" ,company_data['result']['company']['nip'])

    except requests.exceptions.HTTPError as errh:
        print("HTTP Errpr:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error conecting", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeput error", errt)
    except requests.exceptions.RequestException as err:
        print("Info of error: ", err)
    
    #except requests.exceptions.HTTPError as errh:: Ten blok obsługuje wyjątki związane z błędami HTTP, takie jak błędy 4xx (błędy klienta) i 5xx (błędy serwera). Jeśli wystąpi taki błąd, obiekt błędu zostanie przypisany do zmiennej errh, a następnie wyświetli komunikat z informacją o błędzie HTTP.

    #except requests.exceptions.ConnectionError as errc:: Blok ten obsługuje błędy związane z problemami z połączeniem, takie jak brak połączenia z internetem lub problemy z siecią. Jeśli wystąpi taki błąd, obiekt błędu zostanie przypisany do zmiennej errc, a następnie wyświetli komunikat z informacją o problemie z połączeniem.

    #except requests.exceptions.Timeout as errt:: Ten blok obsługuje błędy związane z timeoutem, czyli sytuacjami, w których odpowiedź od serwera nie nadejdzie w oczekiwanym czasie. Jeśli wystąpi timeout, obiekt błędu zostanie przypisany do zmiennej errt, a następnie wyświetli komunikat z informacją o timeout.

    #except requests.exceptions.RequestException as err:: Blok ten obsługuje ogólne błędy związane z zapytaniami HTTP, które nie pasują do powyższych kategorii. Jeśli wystąpi ogólny błąd związany z zapytaniem HTTP, obiekt błędu zostanie przypisany do zmiennej err, a następnie wyświetli ogólny komunikat o błędzie.

    if __name__ == "__main__":
        your_nip = input("Entry your nip: ")

        download_data(your_nip)