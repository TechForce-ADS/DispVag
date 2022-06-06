from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("/index.html")

@app.route('/departamentalizacao.html')
def departamentalizacao():
    return render_template("/departamentalizacao.html")

@app.route('/vagas/vagas-fe.html')
def vagasfe():
    return render_template("/vagas/vagas-fe.html")

@app.route('/vagas/vaga-fe1.html')
def vagafe1():
    return render_template("/vagas/vaga-fe1.html")

@app.route('/vagas/vaga-fe2.html')
def vagafe2():
    return render_template("/vagas/vaga-fe2.html")

@app.route('/vagas/vaga-fe3.html')
def vagafe3():
    return render_template("/vagas/vaga-fe3.html")

@app.route('/vagas/vaga-fe4.html')
def vagafe4():
    return render_template("/vagas/vaga-fe4.html")

@app.route('/vagas/vaga-fe5.html')
def vagafe5():
    return render_template("/vagas/vaga-fe5.html")

@app.route('/vagas/vagas-be.html')
def vagasbe():
    return render_template("/vagas/vagas-be.html")

@app.route('/vagas/vaga-be1.html')
def vagabe1():
    return render_template("/vagas/vaga-be1.html")

@app.route('/vagas/vaga-be2.html')
def vagabe2():
    return render_template("/vagas/vaga-be2.html")

@app.route('/vagas/vaga-be3.html')
def vagabe3():
    return render_template("/vagas/vaga-be3.html")

@app.route('/vagas/vaga-be4.html')
def vagabe4():
    return render_template("/vagas/vaga-be4.html")

@app.route('/vagas/vaga-be5.html')
def vagabe5():
    return render_template("/vagas/vaga-be5.html")

@app.route('/vagas/vagas-outros.html')
def vagasoutros():
    return render_template("/vagas/vagas-outros.html")

@app.route('/vagas/vaga-outros1.html')
def vagaoutros1():
    return render_template("/vagas/vaga-outros1.html")

@app.route('/vagas/vaga-outros2.html')
def vagaoutros2():
    return render_template("/vagas/vaga-outros2.html")

@app.route('/vagas/vaga-outros3.html')
def vagaoutros3():
    return render_template("/vagas/vaga-outros3.html")

@app.route('/vagas/vaga-outros4.html')
def vagaoutros4():
    return render_template("/vagas/vaga-outros4.html")

@app.route('/vagas/vaga-outros5.html')
def vagaoutros5():
    return render_template("/vagas/vaga-outros5.html")

@app.route('/vagas/vagas-ti.html')
def vagasti():
    return render_template("/vagas/vagas-ti.html")

@app.route('/vagas/vaga-ti1.html')
def vagati1():
    return render_template("/vagas/vaga-ti1.html")

@app.route('/vagas/vaga-ti2.html')
def vagati2():
    return render_template("/vagas/vaga-ti2.html")

@app.route('/vagas/vaga-ti3.html')
def vagati3():
    return render_template("/vagas/vaga-ti3.html")

@app.route('/vagas/vaga-ti4.html')
def vagati4():
    return render_template("/vagas/vaga-ti4.html")

@app.route('/vagas/vaga-ti5.html')
def vagati5():
    return render_template("/vagas/vaga-ti5.html")

@app.route("/cursos.html")
def cursos():
    return render_template("/cursos.html")

@app.route("/metricas.html")
def metricas():
    return render_template("/metricas.html")

@app.route("/map_front.html")
def map_front():
    return render_template("/map_front.html")

@app.route("/contato.html")
def contato():
    return render_template("/contato.html")

@app.route("/localizaçao.html")
def localizaçao():
    return render_template("/localizaçao.html")

@app.route("/map_back.html")
def map_back():
    return render_template("/map_back.html")

@app.route("/map_ti.html")
def map_ti():
    return render_template("/map_ti.html")
@app.route("/map_outros.html")
def map_outros():
    return render_template("/map_outros.html")

@app.route("/duvidas.html")
def duvidas():
    return render_template("/duvidas.html")

@app.route("/cadastrar.html")
def cadastrar():
    return render_template("/cadastrar.html")
    
@app.route("/encontrar.html")
def encontrar():
    return render_template("/encontrar.html")

@app.route("/user/<nome_usuario>") #cria uma pagina dinamica, onde cada usuario teria uma pagina diferente
def user(nome_usuario):              #definir a função user com o parametro sendo o "nome_usuario"
    return render_template("user.html", nome_usuario=nome_usuario)


#colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)
