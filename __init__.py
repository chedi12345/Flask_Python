from flask import Flask
from flask import render_template
from flask import json                                                                                                                                     
app = Flask(__name__)                                                                                                                  

@app.route('/<int:valeur>')
def carre_etoiles(n):
    n = int(input("Entrez le nombre d'etoiles : "))
    for i in range(n):
        print('*', n)
carre_etoiles(n)


if __name__ == "__main__":
  app.run(debug=True)
