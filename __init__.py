from flask import Flask
from flask import render_template
from flask import json                                                                                                                                     
app = Flask(__name__)                                                                                                                  


@app.route('/<int:valeur>')
def exercice():
    etoiles = ''
    for i in range (5):
        for j in range(5):
            etoiles += '*'
        return etoiles


if __name__ == "__main__":
  app.run(debug=True)
