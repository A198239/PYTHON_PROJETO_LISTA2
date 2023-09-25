from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def principal():
    bebidas = ["Cerveja", "Whisky", "Cachaça", "Gin", "Vodka"]
    return render_template("index.html", bebidas=bebidas)
  
@app.route('/sobre')
def sobre():  
    return render_template("sobre.html")
app.run()    
   
#http://127.0.0.1:5000
