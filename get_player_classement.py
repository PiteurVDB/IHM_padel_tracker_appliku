import requests
import json
from datetime import datetime, timedelta

all_data = []
tranche = 100

# Obtenir la date actuelle
now = datetime.now()

# Déterminer le premier jour du mois actuel
first_day = datetime(now.year, now.month, 1)

# Calculer le nombre de jours jusqu'au premier mardi
days_to_first_tuesday = 7 if (1 - first_day.weekday() + 7) % 7 == 0 else (1 - first_day.weekday() + 7) % 7

# Ajouter les jours nécessaires pour atteindre le premier mardi
date = (first_day + timedelta(days=days_to_first_tuesday)).strftime('%Y-%m-%dT00')

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://tenup.fft.fr',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
}
while True:
    url = f"https://tenup.fft.fr/classement-padel?date={date}%3A00%3A00.000&age=&tranche={tranche}&type=H&export"

    if tranche == 200:
        tranche = 44100
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Error with status code {response.status_code} for tranche {tranche}")
        break

    data = response.json()

    if "classement" not in data or not data["classement"].get("rows"):
        print(f"No more data for tranche {tranche}")
        break

    classement = data["classement"]["rows"]
    all_data.extend(classement)
    tranche += 100

with open('static/data/classement_joueurs_padel.json', 'w', encoding='utf-8') as f:
    json.dump(all_data, f, ensure_ascii=False, indent=4)
