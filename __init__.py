from flask import Flask

app = Flask(__name__)
@app.route('/<int:n>')
s=0
def somme (n):
    for i in  range (n):
        if (i%5==0) or (i%7==0):
            s+=i
        elif (n%11==0):
            i+=1
        if s> 5000:
            return f"<h1>Somme dépassée : {s}</h1><p>Arrêt à i = {i}</p>"

    return f"<h1>Somme finale : {s}</h1>"

if __name__ == "__main__":
    app.run(debug=True)
