from flask import Flask, render_template, jsonify, request
# from flask_cors import CORS # Descomente se precisar de CORS
import os
# from dotenv import load_dotenv # Descomente se estiver usando um arquivo .env
# import firebase_admin
# from firebase_admin import credentials, auth, firestore
# import requests
# from functools import wraps

# Carregar variáveis de ambiente
# load_dotenv()

# Configuração do Flask
app = Flask(__name__)

# --- ROTAS DO FLASK ---
# Adicione 'endpoint' a cada rota para que o url_for() funcione

@app.route('/', endpoint='index')
def home():
    # Supondo que você também corrigirá os links em index.html
    return render_template('index.html')

@app.route('/sobre', endpoint='sobre')
def sobre():
    return render_template('sobre.html')

# ROTA ATUALIZADA PARA A PÁGINA DE SERVIÇOS
@app.route('/servicos', endpoint='servicos')
def servicos():
    return render_template('servicos.html') 

# ROTA FINAL PARA A PÁGINA DE CONTATO
@app.route('/contato', endpoint='contato')
def contato():
    return render_template('contato.html')

# ROTA PARA PROCESSAR O FORMULÁRIO (exemplo)
@app.route('/enviar-contato', methods=['POST'])
def handle_contact_form():
    # Esta é a função que receberá os dados do formulário.
    # Por enquanto, ela apenas imprime os dados no terminal.
    # No futuro, você pode adicionar aqui a lógica para enviar email ou salvar no banco de dados.
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        print("--- NOVA MENSAGEM DO SITE ---")
        print(f"Nome: {name}")
        print(f"Email: {email}")
        print(f"Mensagem: {message}")
        print("-----------------------------")
        
        # Você pode redirecionar para uma página de "obrigado" ou retornar uma mensagem de sucesso.
        return "Mensagem recebida com sucesso!", 200
    return "Método não permitido", 405

# --- FIM DAS ROTAS ---

# Executar o aplicativo
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
