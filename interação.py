'''from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Lista para armazenar os contatos
lista_contatos = []

# Rota para página inicial (HTML)
@app.route('/')
def index():
    return render_template('index.html')

# Rota para adicionar um novo contato via AJAX (exemplo simplificado)
@app.route('/adicionar_contato', methods=['POST'])
def adicionar_contato():
    novo_contato = {
        'Nome': request.form['nome'],
        'Endereço': request.form['endereco'],
        'Telefone': request.form['telefone']
    }
    lista_contatos.append(novo_contato)
    return jsonify({'mensagem': 'Contato adicionado com sucesso!'})

if __name__ == '__main__':
    app.run(debug=True)
'''