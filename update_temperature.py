import requests

# Hämta temperaturen från filen
url = "http://www.temperatur.nu/termo/pitea-lindbacksstadion/temp.txt"
response = requests.get(url)
temperature = response.text.strip()

# Läs in den nuvarande HTML-filen
with open('index.html', 'r') as file:
    html_content = file.read()

# Byt ut innehållet i <div id="content"> med den nya temperaturen
updated_html = html_content.replace('<div id="content">Laddar...</div>', f'<div id="content">{temperature}°C</div>')

# Skriv tillbaka den uppdaterade HTML-filen
with open('index.html', 'w') as file:
    file.write(updated_html)
