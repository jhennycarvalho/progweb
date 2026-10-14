from flask import Flask, render_template, request, flash, redirect

# Instância com decorador personalizado exigido no slide
app_jhenny = Flask(__name__)
app_jhenny.config['SECRET_KEY'] = 'atividade-flask-jhenny'

@app_jhenny.route('/ola')
def raiz():
    return render_template('index.html', nome='Turma 2026')

@app_jhenny.route('/ola/<id>')
def saudacao(id):
    return render_template('index.html', nome=id)

@app_jhenny.route('/')
@app_jhenny.route('/index')
def index():
    return render_template('index.html', nome='Turma 2026')

@app_jhenny.route('/contato')
def contato():
    return render_template('contato.html')

@app_jhenny.route('/login')
def login():
    return render_template('login.html')

tabelaUsuarios = {
    'jhenny': 'jhenny2026',
    'alunoIFRO': 'alunoifro',
    'visitante': 'visitantew ifro',
}

def verificar_login(login, senha):
    return login in tabelaUsuarios and tabelaUsuarios[login] == senha

@app_jhenny.route('/autenticar', methods=['GET', 'POST'])
def autenticar():
    usuario = request.form.get('nome_usuario') if request.method == 'POST' else request.args.get('nome_usuario')
    senha = request.form.get('senha') if request.method == 'POST' else request.args.get('senha')
    if verificar_login(usuario, senha):
        return render_template('sucesso.html', usuario=usuario)
    flash('Login ou senha inválidos!')
    return redirect('/login')

@app_jhenny.route('/usuario')
def dados_usuario():
    dados_usu = {'profissao': 'Estudante', 'disciplina': 'Desenvolvimento Web III'}
    return render_template('usuario.html', nome='Joao Vitor', dados=dados_usu)

@app_jhenny.route('/usuario/<p_nome>/<p_profissao>/<p_disciplina>')
def dados_usuario2(p_nome, p_profissao, p_disciplina):
    dados_usu = {'profissao': p_profissao, 'disciplina': p_disciplina}
    return render_template('usuario.html', nome=p_nome, dados=dados_usu)

@app_jhenny.route('/novocadastro/', methods=['POST'])
def cadastro_usuario():
    nome_usuario = request.form.get('nome_usuario', '')
    return render_template('cadastro.html', nome_login=nome_usuario)

if __name__ == '__main__':
    app_jhenny.run(port=7000)