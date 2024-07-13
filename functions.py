import requests
import json
import statistics

def reload_token():
    url = "https://auth.fft.fr/auth/realms/master/protocol/openid-connect/token"

    payload = "scope=openid&refresh_token=eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJlMzFjYjkyZC02YjhjLTQ5NzItYTFjOS1jMzVkNjI2ZDhiYWIifQ.eyJleHAiOjE3MjYwOTY4OTksImlhdCI6MTcyMDkxMjg5OSwianRpIjoiNTYwNThjODQtMDU1YS00ODAzLWFmZTQtMTg2M2QxYzZiNDgzIiwiaXNzIjoiaHR0cHM6Ly9hdXRoLmZmdC5mci9hdXRoL3JlYWxtcy9tYXN0ZXIiLCJhdWQiOiJodHRwczovL2F1dGguZmZ0LmZyL2F1dGgvcmVhbG1zL21hc3RlciIsInN1YiI6IjAxZGQ0OTAwLWM5MDAtNGIxZS04MTNhLTg3MDFiYzcwZTBlNSIsInR5cCI6IlJlZnJlc2giLCJhenAiOiJ0ZW51cC1hcHAiLCJzZXNzaW9uX3N0YXRlIjoiNzVmYmJmMzEtNmQzYi00ZWE2LTljNmUtZGY5MWNiYWE4NWZlIiwic2NvcGUiOiJvcGVuaWQgd3JpdGU6aWRlbnRpdHkgcmVhZDpsaWNlbmNlIHNlYXJjaDppZGVudGl0eSBtb2phOnB1YmxpYyBvcGVuX2lkIHdyaXRlOnBhaWVtZW50IHdyaXRlOmZpbGVzIHNlYXJjaDphY2NvdW50IHJlYWQ6ZmlsZXM6anVzdGlmaWNhdGlmIGRlbGV0ZTphY2NvdW50IHJlYWQ6Y2xhc3NlbWVudCBlbWFpbCBnZXN0aW9uOmhvbW9sb2dhdGlvbiByZWFkOmlkZW50aXR5OmFsbCBwcm9maWxlIHJlYWQ6cGFpZW1lbnQgZGVsZXRlOmlkZW50aXR5IHdyaXRlOmFjY291bnQgcmVhZDppZGVudGl0eSBjbGFzc2VtZW50X3JlYWQiLCJzaWQiOiI3NWZiYmYzMS02ZDNiLTRlYTYtOWM2ZS1kZjkxY2JhYTg1ZmUifQ.Jv8E4XIRsTZJWLq73WFImCir3hstgBj-sF973-DI9oA&code=3e28c9bc-38f8-437f-99bf-2a954b2336e8.75fbbf31-6d3b-4ea6-9c6e-df91cbaa85fe.5e9f9e49-e93f-4ecb-8fed-3b8fef522f82&client_id=tenup-app&code_verifier=FIiyWALFKqBpauNdzDC_wMico5fNNLFrqgIRQV2jnjs&grant_type=refresh_token&redirect_uri=mat://auth_callback"
    headers = {
        'accept': 'application/vnd.fft+json;version=1',
        'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
        'cookie': 'KEYCLOAK_SESSION=master/01dd4900-c900-4b1e-813a-8701bc70e0e5/c34838f6-4c28-49ca-a316-5398b35e0fbe',
        'user-agent': 'MAT/5413 CFNetwork/1496.0.7 Darwin/23.5.0',
        'accept-language': 'fr-FR,fr;q=0.9',
        'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJRaTV3bWx2bTNuX2p1YW4tSTl1dHo3UGZRLU1tVVlvektwSExhbm9lTXI4In0.eyJleHAiOjE3MjA5MTMxOTksImlhdCI6MTcyMDkxMjg5OSwiYXV0aF90aW1lIjoxNzIwOTEyODk5LCJqdGkiOiIxNWU0NGI2OS1jYmE1LTRkMGQtOGE2OC01MGRjYjMxZjcyZTYiLCJpc3MiOiJodHRwczovL2F1dGguZmZ0LmZyL2F1dGgvcmVhbG1zL21hc3RlciIsImF1ZCI6ImFjY291bnQiLCJzdWIiOiIwMWRkNDkwMC1jOTAwLTRiMWUtODEzYS04NzAxYmM3MGUwZTUiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJ0ZW51cC1hcHAiLCJzZXNzaW9uX3N0YXRlIjoiNzVmYmJmMzEtNmQzYi00ZWE2LTljNmUtZGY5MWNiYWE4NWZlIiwiYWNyIjoiMSIsInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJkZWZhdWx0LXJvbGVzLW1hc3RlciIsIm9mZmxpbmVfYWNjZXNzIiwidW1hX2F1dGhvcml6YXRpb24iXX0sInJlc291cmNlX2FjY2VzcyI6eyJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6Im9wZW5pZCB3cml0ZTppZGVudGl0eSByZWFkOmxpY2VuY2Ugc2VhcmNoOmlkZW50aXR5IG1vamE6cHVibGljIG9wZW5faWQgd3JpdGU6cGFpZW1lbnQgd3JpdGU6ZmlsZXMgc2VhcmNoOmFjY291bnQgcmVhZDpmaWxlczpqdXN0aWZpY2F0aWYgZGVsZXRlOmFjY291bnQgcmVhZDpjbGFzc2VtZW50IGVtYWlsIGdlc3Rpb246aG9tb2xvZ2F0aW9uIHJlYWQ6aWRlbnRpdHk6YWxsIHByb2ZpbGUgcmVhZDpwYWllbWVudCBkZWxldGU6aWRlbnRpdHkgd3JpdGU6YWNjb3VudCByZWFkOmlkZW50aXR5IGNsYXNzZW1lbnRfcmVhZCIsInNpZCI6Ijc1ZmJiZjMxLTZkM2ItNGVhNi05YzZlLWRmOTFjYmFhODVmZSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJpZENybSI6IjEwMDAyNTYxNzQyIiwibmFtZSI6InBpZXJyZSBWQU4gREVOIEJPT00iLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJwaXRldXJyIiwiZ2l2ZW5fbmFtZSI6InBpZXJyZSIsImxvY2FsZSI6ImZyIiwiZmFtaWx5X25hbWUiOiJWQU4gREVOIEJPT00iLCJlbWFpbCI6InB2ZGIyMDAyQGdtYWlsLmNvbSJ9.KGRQNRs2e_GDCEESXBBR-vYf1lW_s_IjN1_CclKru8ZQ-J6Dt94up8vHkMmWoEWm31c_Qak0ovPN3qgY5T3z-tiCvQtuinLtNZEGKTJR0pRf6G-hpfwOn0d8VvfrE4JMpff7LATsCAKJpiRgyg3b1AVomWtSlCHmPRqyPM8MDzz1ciPctYvwxCfBtHY7x9zJPejCeERwxpKVWFo2eLM0GTuTVLwLiyYJdl59RrqHzVfU7sgH-294cjlBi2BJAwIZeiZcU7FR0w8C6QVG-vRVq8aoby27-1EMH6hJPl7a929ClFinBPyFA_SkxxJQ_Myn5y4nsVA213mQptx2vGG03w'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json()["access_token"]

def player_result(nom, prenom):
  token = reload_token()

  url = f"https://api.fft.fr/pratique/v1/players?gender=M&lastName={nom}&size=20&from=0&firstName={prenom}"

  headers = {
    'Content-Type': 'application/json',
    'X-APPLICATION-ID': 'tenup-app',
    'Connection': 'keep-alive',
    'Accept': '*/*',
    'Accept-Language': 'fr-FR,fr;q=0.9',
    'Authorization': f'Bearer {token}',
    'User-Agent': 'MAT/5413 CFNetwork/1496.0.7 Darwin/23.5.0'
  }

  response = requests.request("GET", url, headers=headers)
  data = response.json()

  return data


def player_infos(idCrm):
    token = reload_token()

    headers = {
    'Content-Type': 'application/json',
    'X-APPLICATION-ID': 'tenup-app',
    'Connection': 'keep-alive',
    'Accept-Language': 'fr-FR,fr;q=0.9',
    'Authorization': f'Bearer {token}',
    'User-Agent': 'MAT/5413 CFNetwork/1496.0.7 Darwin/23.5.0'
    }

    url_primary_infos = f"https://api.fft.fr/fft/v1/personne/{idCrm}/classements?idCrm={idCrm}"
    info_1 = requests.request("GET", url_primary_infos, headers=headers).json()

    url_secondary_infos = f"https://api.fft.fr/pratique/v1/profiles/{idCrm}"
    info_2 = requests.request("GET", url_secondary_infos, headers=headers).json()

    date = info_1["padel"]["dernierClassementPadel"]["date"]
    url_tournament_infos = f"https://api.fft.fr/fft/v1/personne/{idCrm}/bilan/PADEL?dateClassement={date}&idCategorieAge=200"
    info_3 = requests.request("GET", url_tournament_infos, headers=headers).json()

    liste_tournoi = []

    for tournoi in info_3:
        try:
            nom_partenaire = tournoi["nomPartenaire"]
            prenom_partenaire = tournoi["prenomPartenaire"]
        except:
            nom_partenaire = "inconnu"
            prenom_partenaire = "inconnu"

        dico = {
            "id_tournoi": tournoi["idHomologation"],
            "epreuve": tournoi["typeEpreuve"]["libelle"],
            "nom_partenaire": nom_partenaire,
            "prenom_partenaire": prenom_partenaire,
            "classement": tournoi["classementEquipe"],
            "nb_points": tournoi["nombrePoints"],
            "date_tournoi": tournoi["dateFinHomologation"][:10]
        }
        liste_tournoi.append(dico)

    try:
        progression = info_1["padel"]["dernierClassementPadel"]["progression"]
    except KeyError:
        progression = 0

    try:
        coup_favoris = info_2["practices"]["PADEL"]["favoriteShot"]
    except KeyError:
        coup_favoris = "inconnu"

    try:
        type_jeu = info_2["practices"]["PADEL"]["favoriteGameType"]
    except KeyError:
        type_jeu = "inconnu"

    try:
        main_forte = info_2["laterality"]
    except KeyError:
        main_forte = "inconnu"

    try:
        frequence = info_2["practiceFrequency"]
    except KeyError:
        frequence = "inconnu"

    info_joueur = {
        "age_min": info_1["padel"]["dernierClassementPadel"]["categorieAge"]["ageMin"],
        "age_max": info_1["padel"]["dernierClassementPadel"]["categorieAge"]["ageMax"],
        "rang": info_1["padel"]["dernierClassementPadel"]["rang"],
        "nb_tournoi": info_1["padel"]["dernierClassementPadel"]["nombreDeTournois"],
        "progression": progression,
        "points": info_1["padel"]["dernierClassementPadel"]["points"],
        "sexe": info_1["padel"]["dernierClassementPadel"]["type"],
        "meilleur_rang": info_1["padel"]["meilleurClassementPadel"]["rang"],
        "meilleur_nb_tournoi": info_1["padel"]["meilleurClassementPadel"]["nombreDeTournois"],
        "meilleur_annee": info_1["padel"]["meilleurClassementPadel"]["millesime"],
        "coup_favori": coup_favoris,
        "type_jeu": type_jeu,
        "main_forte": main_forte,
        "frequence": frequence,
        "nb_tournoi": len(liste_tournoi),
        "avg_podium": round(statistics.mean([i["nb_points"] for i in liste_tournoi]), 2),
        "liste_tournoi": liste_tournoi
    }

    return info_joueur
