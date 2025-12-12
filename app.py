#importar biblioteca
from flask import Flask , render_template 

#generar servidor
app = Flask (__name__)

#ruta (principal)
@app.route ("/")
def index ():
    return render_template("index.html") 

@app.route ("/pokemons_legendarios")
def legendarios ():
    return render_template("legendarios.html") 

#ejecute el servidor
app.run (debug = True) 
