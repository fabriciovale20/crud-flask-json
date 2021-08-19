from flask import Flask, render_template, request
import json

app = Flask(__name__)

cadastro = []


@app.route('/menu', methods=['POST', 'GET'])
def menu():
    while True:
        try:
            if request.method == 'GET':
                return render_template('menu.html')  # Página inicial
            else:
                resp = int(request.form.get('valor'))
                if resp == 1:
                    create_json(cadastro)
                    return render_template('create.html')
                if resp == 2:
                    get()
                if resp == 3:
                    return render_template('post.html')
        except Exception:
            return render_template('menu.html')


# Lendo arquivo JSON
@app.route('/menu/lista')
def get():
    return render_template('get.html', dados=read_json())


# Ler arquivo JSON
def read_json():
    global dados

    with open('arquivo_json.json', 'r', encoding='utf8') as f:
        return json.load(f)


# Criar arquivo JSON
def create_json(dados):
    with open('arquivo_json.json', 'w', encoding='utf8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4, separators=(',', ':'))


if __name__ == '__main__':
    app.run(debug=True)
