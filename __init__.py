from flask import Flask
from flask import render_template
from flask import json                                                                                                                                     
app = Flask(__name__)                                                                                                                  


@app.route('/<int:valeur>')
def carre_etoiles(n):
    for i in range(n):
        print('*' * n)

# Exemple d'utilisation
n = int(input("Entrez la taille du carré : "))
carre_etoiles(n)


if __name__ == "__main__":
  app.run(debug=True)
