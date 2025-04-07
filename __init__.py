from flask import Flask

app = Flask(name)

@app.route('/<path:valeurs>')
def exercice(valeurs):
    liste_nombres = valeurs.split('/')
    liste_nombres = [int(n) for n in liste_nombres]

    for i in range(len(liste_nombres) - 1):
        if liste_nombres[i] > liste_nombres[i + 1]:
            liste_nombres[i + 1] = liste_nombres[i]

    return f"Le nombre maximum est : {liste_nombres[-1]}"

if name == 'main':
    app.run(host='0.0.0.0')
