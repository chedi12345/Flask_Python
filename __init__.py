from flask import Flask
from flask import render_template
from flask import json                                                                                                                                     
app = Flask(__name__)                                                                                                                  

@app.route('/<int:valeur>')
def carre_etoiles(5):
    n = int(input("Entrez le nombre d'etoiles : "))
    for i in range(5):
        print('*', 5)
carre_etoiles(5)


if __name__ == "__main__":
  app.run(debug=True)
