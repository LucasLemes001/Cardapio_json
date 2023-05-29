from flask import Flask,request,jsonify
import json

app = Flask(__name__)

@app.route('/')
def chamar_cardapio():
    with open('dog.json') as arquivo:
        data = json.load(arquivo)
    return jsonify(data)
        
@app.route('/novopedido', methods=['POST'])
def novo_pedido():
    with open('novopedido.json','a') as arquivo_pedido:
        dados = json.load(arquivo_pedido)
    return jsonify(dados)
    

app.run(port=5000, host='localhost', debug= True)