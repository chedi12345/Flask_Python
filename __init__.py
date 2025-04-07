from flask import Flask

app = Flask(__name__)
@app.route('/<int:n>')
def somme (n):
    s=0
    for i in  range (n):
        if (i%5==0) or (i%7==0):
            s+=i
        elif (n%11==0):
            i+=1
        if (s<=5000):
            print(s)
        else:
            print(s-i)

if __name__ == "__main__":
    app.run(debug=True)
