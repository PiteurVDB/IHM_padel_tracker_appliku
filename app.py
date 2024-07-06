from flask import Flask, jsonify, render_template, request
from functions import *
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/joueur')
def joueur():
    return render_template('joueur.html')

@app.route('/liste_joueurs_custom')
def liste_joueurs_custom():
    return render_template('liste_joueurs_custom.html')

@app.route('/search_players', methods=['POST'])
def search_players():
    search_data = request.json
    nom = search_data.get('nom', '')
    prenom = search_data.get('prenom', '')

    recherche = player_result(nom, prenom)

    return jsonify(recherche)


@app.route('/get_player_stats', methods=['POST'])
def get_player_stats():
    player_data = request.json
    idCrm = player_data["idCrm"]
    prenom = player_data["firstName"]
    nom = player_data["lastName"]
    ville = player_data.get('city', '')
    date_naissance = datetime.strptime(player_data.get('birthDate', ''), "%Y-%m-%d")
    age = datetime.now().year - date_naissance.year - ((datetime.now().month, datetime.now().day) < (date_naissance.month, date_naissance.day))
    nom_club = player_data.get('licenceClubLabel', '')
    image = player_data.get('picture', '')

    # Traitement des données et récupération des statistiques supplémentaires
    info_joueur = player_infos(idCrm)
    info_joueur['prenom'] = prenom
    info_joueur['nom'] = nom
    info_joueur['ville'] = ville
    info_joueur['age'] = age
    info_joueur['nom_club'] = nom_club
    info_joueur['image'] = image

    print(json.dumps(info_joueur, indent=4))

    # Vous pouvez simplement retourner le dictionnaire
    return jsonify(info_joueur)

if __name__ == '__main__':
    app.run(debug=True)
