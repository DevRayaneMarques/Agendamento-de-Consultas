from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

agenda = {}

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/adicionar_consulta', methods=['POST'])
def adicionar_consulta():
    nome = request.form['nome']
    data = request.form['data']
    hora = request.form['hora']
    telefone = request.form['telefone']
    consulta = {"nome": nome, "data": data, "hora": hora, "telefone": telefone}
    agenda[nome] = consulta
    return render_template('index.html')


@app.route('/listar_consultas')
def listar_consultas():
    with app.app_context():
        return render_template('listar_consultas.html')

@app.route('/remover_consulta', methods=['POST'])
def remover_consulta():
    nome = request.form['nome']
    if nome in agenda:
        del agenda[nome]
    return render_template('index.html')

@app.route('/atualizar_consulta', methods=['POST'])
def atualizar_consulta():
    nome = request.form['nome']
    nova_data = request.form['nova_data']
    nova_hora = request.form['nova_hora']
    if nome in agenda:
        consulta = agenda[nome]
        consulta["data"] = nova_data
        consulta["hora"] = nova_hora
    return render_template('index.html')

@app.route('/pesquisar_consulta', methods=['POST'])
def pesquisar_consulta():
    nome = request.form['nome']
    consulta = None
    for nome_agenda, consulta_agenda in agenda.items():
        if nome_agenda.lower() == nome.lower():
            consulta = consulta_agenda
            break
    if consulta:
        return render_template('pesquisar_consulta.html', consulta=consulta)
    else:
        return render_template('nao_encontrado.html')

if __name__ == '__main__':
    app.run(debug=True)