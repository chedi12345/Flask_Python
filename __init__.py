from flask import Flask
from flask import render_template
from flask import json                                                                                                                                     
app = Flask(__name__)                                                                                                                  

n=int(input("donner le nombre de base de pyramid"))
k=""
for i in range (1,n+1):
    k=k+str(i)
    l=""
    for j in range(0,len(k-1),-1):
        l=l+str(j)
    
if __name__ == "__main__":
  app.run(debug=True)

