from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index")

@app.route('/quem.html')
def quem():
    return render_template("quem.html")

@app.route('/contato.html')
def contato():
    return render_template("contato.html")

@app.route("/user/<nome_usuario>") #cria uma pagina dinamica, onde cada usuario teria uma pagina diferente
def user(nome_usuario):              #definir a função user com o parametro sendo o "nome_usuario"
    return render_template("user.html", nome_usuario=nome_usuario)


#colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)
