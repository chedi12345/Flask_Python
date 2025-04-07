from flask import Flask
from flask import render_template
from flask import json                                                                                                                                     
app = Flask(__name__)                                                                                                                  

def generer_pyramide(valeur):
    for i in range(1, valeur + 1):  # Pour chaque ligne de 1 à valeur
        espaces = ' ' * (valeur - i)  # Ajoute des espaces pour centrer
        partie_croissante = ''.join(str(j) for j in range(1, i + 1))  # Exemple : 123
        partie_decroissante = ''.join(str(j) for j in range(i - 1, 0, -1))  # Exemple : 21
        ligne = espaces + partie_croissante + partie_decroissante  # Combine tout
        print(ligne)  # Affiche la ligne

# Demande à l'utilisateur un nombre
valeur_utilisateur = int(input("Entrez un nombre pour générer la pyramide : "))
generer_pyramide(valeur_utilisateur))
    
if __name__ == "__main__":
  app.run(debug=True)

