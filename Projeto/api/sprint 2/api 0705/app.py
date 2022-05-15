from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("/index.html")

@app.route('/departamentalizacao.html')
def departamentalizacao():
    return render_template("/departamentalizacao.html")

@app.route('/vagas/vagas-rh.html')
def vagas():
    return render_template("/vagas/vagas-rh.html")

@app.route('/vagas/vaga-rh.html')
def vaga():
    return render_template("/vagas/vaga-rh.html")

@app.route("/cursos.html")
def cursos():
    return render_template("/cursos.html")

@app.route("/metricas.html")
def metricas():
    return render_template("/metricas.html")

@app.route("/sobre.html")
def sobre():
    return render_template("/sobre.html")

@app.route("/contato.html")
def contato():
    return render_template("/contato.html")



@app.route("/user/<nome_usuario>") #cria uma pagina dinamica, onde cada usuario teria uma pagina diferente
def user(nome_usuario):              #definir a função user com o parametro sendo o "nome_usuario"
    return render_template("user.html", nome_usuario=nome_usuario)


#colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)
