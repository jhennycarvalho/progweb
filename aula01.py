from flask import Flask, render_template


app_Projeto = Flask(__name__, template_folder='templates')
#cria o objeto da aplicação

@app_Projeto.route("/")
def homepage():
    return render_template("homepage.html")

@app_Projeto.route("/contato")
def contato():
    return render_template("contato.html")

@app_Projeto.route("/index")
def indice():
    return render_template ("index.html")
    

@app_Projeto.route("/usuario")
def dados_usuario():
    nome_usuario ="jhennyfer"
    dados_usu = {"profissao": "Tecnica em informatica"}
    return render_template("usuario.html", nome_usuario, dados_usu)


if __name__ == "__main__":
    app_Projeto.run(port= 8000)