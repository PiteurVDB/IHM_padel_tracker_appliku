import requests
import json
import statistics

def reload_token():
    url = "https://auth.fft.fr/auth/realms/master/protocol/openid-connect/token"

    payload = "redirect_uri=mat://auth_callback&grant_type=refresh_token&client_id=tenup-app&refresh_token=eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJlMzFjYjkyZC02YjhjLTQ5NzItYTFjOS1jMzVkNjI2ZDhiYWIifQ.eyJleHAiOjE3MjQ5MjA2NDksImlhdCI6MTcxOTczNjY1MCwianRpIjoiZDIyMjUyMmYtNGE0MC00MTE2LTgwMjktYTUzNWU3NDc4ZTRmIiwiaXNzIjoiaHR0cHM6Ly9hdXRoLmZmdC5mci9hdXRoL3JlYWxtcy9tYXN0ZXIiLCJhdWQiOiJodHRwczovL2F1dGguZmZ0LmZyL2F1dGgvcmVhbG1zL21hc3RlciIsInN1YiI6IjAxZGQ0OTAwLWM5MDAtNGIxZS04MTNhLTg3MDFiYzcwZTBlNSIsInR5cCI6IlJlZnJlc2giLCJhenAiOiJ0ZW51cC1hcHAiLCJzZXNzaW9uX3N0YXRlIjoiYzM0ODM4ZjYtNGMyOC00OWNhLWEzMTYtNTM5OGIzNWUwZmJlIiwic2NvcGUiOiJvcGVuaWQgd3JpdGU6aWRlbnRpdHkgcmVhZDpsaWNlbmNlIHNlYXJjaDppZGVudGl0eSBtb2phOnB1YmxpYyBvcGVuX2lkIHdyaXRlOnBhaWVtZW50IHdyaXRlOmZpbGVzIHJlYWQ6ZmlsZXM6anVzdGlmaWNhdGlmIHJlYWQ6Y2xhc3NlbWVudCBlbWFpbCBnZXN0aW9uOmhvbW9sb2dhdGlvbiByZWFkOmlkZW50aXR5OmFsbCBwcm9maWxlIHJlYWQ6cGFpZW1lbnQgZGVsZXRlOmlkZW50aXR5IHJlYWQ6aWRlbnRpdHkgY2xhc3NlbWVudF9yZWFkIiwic2lkIjoiYzM0ODM4ZjYtNGMyOC00OWNhLWEzMTYtNTM5OGIzNWUwZmJlIn0.07Xy58AP9ISntBNr25PaRLb6R0KECwFLyZTUNzysyvY&code=a58adcdf-0dea-4bc5-ba61-51d40e061afc.c34838f6-4c28-49ca-a316-5398b35e0fbe.5e9f9e49-e93f-4ecb-8fed-3b8fef522f82&code_verifier=9Sd8HpiLgWy2pP4kgxbVB4fsdye9xxGtK8IqIbWG74s&scope=openid"
    headers = {
        'accept': 'application/vnd.fft+json;version=1',
        'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
        'cookie': 'KEYCLOAK_SESSION=master/01dd4900-c900-4b1e-813a-8701bc70e0e5/c34838f6-4c28-49ca-a316-5398b35e0fbe',
        'user-agent': 'MAT/5413 CFNetwork/1496.0.7 Darwin/23.5.0',
        'accept-language': 'fr-FR,fr;q=0.9',
        'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJRaTV3bWx2bTNuX2p1YW4tSTl1dHo3UGZRLU1tVVlvektwSExhbm9lTXI4In0.eyJleHAiOjE3MTk3MzY5NTAsImlhdCI6MTcxOTczNjY1MCwiYXV0aF90aW1lIjoxNzE5NzM2NjQ5LCJqdGkiOiI5YTY3YWIwYy02NDE5LTQ1M2QtYjkwZi03Y2FlMmQ0ZWFhM2UiLCJpc3MiOiJodHRwczovL2F1dGguZmZ0LmZyL2F1dGgvcmVhbG1zL21hc3RlciIsImF1ZCI6ImFjY291bnQiLCJzdWIiOiIwMWRkNDkwMC1jOTAwLTRiMWUtODEzYS04NzAxYmM3MGUwZTUiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJ0ZW51cC1hcHAiLCJzZXNzaW9uX3N0YXRlIjoiYzM0ODM4ZjYtNGMyOC00OWNhLWEzMTYtNTM5OGIzNWUwZmJlIiwiYWNyIjoiMSIsInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJkZWZhdWx0LXJvbGVzLW1hc3RlciIsIm9mZmxpbmVfYWNjZXNzIiwidW1hX2F1dGhvcml6YXRpb24iXX0sInJlc291cmNlX2FjY2VzcyI6eyJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6Im9wZW5pZCB3cml0ZTppZGVudGl0eSByZWFkOmxpY2VuY2Ugc2VhcmNoOmlkZW50aXR5IG1vamE6cHVibGljIG9wZW5faWQgd3JpdGU6cGFpZW1lbnQgd3JpdGU6ZmlsZXMgcmVhZDpmaWxlczpqdXN0aWZpY2F0aWYgcmVhZDpjbGFzc2VtZW50IGVtYWlsIGdlc3Rpb246aG9tb2xvZ2F0aW9uIHJlYWQ6aWRlbnRpdHk6YWxsIHByb2ZpbGUgcmVhZDpwYWllbWVudCBkZWxldGU6aWRlbnRpdHkgcmVhZDppZGVudGl0eSBjbGFzc2VtZW50X3JlYWQiLCJzaWQiOiJjMzQ4MzhmNi00YzI4LTQ5Y2EtYTMxNi01Mzk4YjM1ZTBmYmUiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaWRDcm0iOiIxMDAwMjU2MTc0MiIsIm5hbWUiOiJwaWVycmUgVkFOIERFTiBCT09NIiwicHJlZmVycmVkX3VzZXJuYW1lIjoicGl0ZXVyciIsImdpdmVuX25hbWUiOiJwaWVycmUiLCJsb2NhbGUiOiJmciIsImZhbWlseV9uYW1lIjoiVkFOIERFTiBCT09NIiwiZW1haWwiOiJwdmRiMjAwMkBnbWFpbC5jb20ifQ.ARr_MWVNz07RYG2TluJM1nbvFwJhOYKhaKnJhKdzQCwgyf0HW4bZWBEDGDAsgjQzuO7BKmaoOxAGxp_SP5twwQqAzolcihAAHProeZrjzpH7bmL7r5bwj_d6wuMhKTkiQ6l3Q5n3HQFt0zjuL7QOZfstQrYF_qD7H28Ov2zJRWd1Trv3YIS8ZRhT5U9-zaf0Q33Ye6Kap-fuci0Vqh2tmJvdwKismZCdqKMal2v9yGJi797OAilYLn3kgxhkEtcycDhybPrvV5TR0cF2WLsvClF8oQyrq52OWEdR25BQYXr93Uj65iR5IcQF-qqUrTp885kM9WN0t4DPsCW-nhmuLQ'
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