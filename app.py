from flask import Flask, render_template, request
from encriptar import encriptar_texto
from decriptar import decriptar_texto

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encriptar', methods=['POST'])
def encriptar():
    texto = request.form.get('texto', '')
    texto_original, texto_encriptado = encriptar_texto(texto)
    return render_template('index.html',
                           texto_original=texto_original,
                           resultado=texto_encriptado,
                           acao='Encriptado')

@app.route('/decriptar', methods=['POST'])
def decriptar():
    texto = request.form.get('texto', '')
    texto_original, texto_decriptado = decriptar_texto(texto)
    return render_template('index.html',
                           texto_original=texto_original,
                           resultado=texto_decriptado,
                           acao='Decriptado')

if __name__ == '__main__':
    app.run(debug=True)
