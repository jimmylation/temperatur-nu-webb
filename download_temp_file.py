import requests

# URL för temperaturfilen
url = "http://www.temperatur.nu/termo/pitea-lindbacksstadion/temp.txt"

# Ladda ner filen
response = requests.get(url)
if response.status_code == 200:
    with open('temp.txt', 'w') as file:
        file.write(response.text)  # Skriv innehållet till en lokal fil
else:
    print(f"Fel vid nedladdning av filen: {response.status_code}")
