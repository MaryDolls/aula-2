from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/contato', methods=['GET', 'POST'])
def contato():
    return render_template('contato.html')

@app.route('/confirmacao', methods=['POST'])
def confirmacao():
    nome = request.form.get('nome')
    email = request.form.get('email')
    mensagem = request.form.get('mensagem')
    print(f"Nome: {nome}, Email: {email}, Mensagem: {mensagem}")
    return render_template('confirmacao.html')

if __name__ == '__main__':
    app.run(debug=True)
