# Evidências de teste — Atividade GitHub + Flask

## 1. Base utilizada

O projeto foi revisado a partir do código-base fornecido na aula, consolidando a evolução em um único `app.py`, mantendo o histórico no Git por commits e branch.

## 2. Revisão realizada

Foram revisados:

* código Python (`app.py`);
* todas as rotas e métodos HTTP;
* templates Jinja2 na pasta `templates/`;
* referências `url_for()` dos templates;
* fluxo de login, `flash`, `redirect` e cadastro;
* `requirements.txt` e `.gitignore`;
* histórico, branches e integridade do repositório Git.

Durante a revisão, o decorador do Flask foi atualizado para `@app_jhenny` conforme as exigências da atividade, e a rota de cadastro foi devidamente posicionada antes do bloco `if __name__ == '__main__':`.