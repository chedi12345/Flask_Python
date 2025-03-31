from flask import Flask
from flask import render_template
from flask import json                                                                                                                                     
app = Flask(__name__)                                                                                                                  


@app.route('/<int:valeur>')
def exercice():
    etoiles = int(input("donner un nombre d'etoiles"))
    for i in range (etoiles):
        for j in range(etoiles):
            etoiles += '*'
        return etoiles


if __name__ == "__main__":
  app.run(debug=True)
