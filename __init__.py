from flask import Flask

app = Flask(__name__)

@app.route('/<int:n>')
def calculer_somme(n):
    somme = 0

    for i in range(1, n + 1):
        if i % 11 == 0:
            continue  # On ignore les nombres divisibles par 11

        if i % 5 == 0 or i % 7 == 0:
            somme += i

        if somme > 5000:
            return f"<h1>Somme dépassée : {somme}</h1><p>Arrêt à i = {i}</p>"

    return f"<h1>Somme finale : {somme}</h1>"

if __name__ == "__main__":
    app.run(debug=True)
