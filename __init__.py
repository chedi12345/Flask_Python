from flask import Flask
from flask import render_template
from flask import json

app = Flask(__name__)

@app.route('/<int:valeur>')
def pyramide(valeur):
    lignes = []
    for i in range(1, valeur + 1):
        espaces = ' ' * (valeur - i)
        gauche = ''.join(str(j) for j in range(1, i + 1))
        droite = ''.join(str(j) for j in range(i - 1, 0, -1))
        ligne = espaces + gauche + droite
        lignes.append(ligne)
    
    return render_template(lignes=lignes, valeur=valeur) 
if name == "main":
    app.run(debug=True)
