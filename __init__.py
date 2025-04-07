from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            valeurs = request.form['nombres']
            liste = [int(x) for x in valeurs.split()]
            
            # Trouver le max sans utiliser max()
            valeur_max = liste[0]
            for nombre in liste[1:]:
                if nombre > valeur_max:
                    valeur_max = nombre

            return render_template('result.html', max_val=valeur_max, liste=liste)

        except ValueError:
            erreur = "Erreur : Veuillez entrer uniquement des nombres séparés par des espaces."
            return render_template('index.html', erreur=erreur)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

