from flask import Flask

app = Flask(__name__)

@app.route('/<int:n>')
def calculer_somme(n):
    somme = 0

    for i in range(1, n + 1):
        if i %11 == 0:
            i+=1

        if i % 5 == 0 or i % 7 == 0:
            somme += i

        if somme > 5000:
            return(somme) 
    return(somme) 
if __name__ == "__main__":
    app.run(debug=True)
