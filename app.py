from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_mail import Mail, Message
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

# --- CONFIGURAÇÃO DO FLASK-MAIL ---
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Servidor SMTP do seu provedor de e-mail
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_USERNAME')

mail = Mail(app)

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

# ROTA FINAL PARA A PÁGINA DE CONTATO
@app.route('/landing_v2', endpoint='landing_v2')
def landing_v2():
    return render_template('landing_v2.html')

# ROTA PARA PROCESSAR O FORMULÁRIO
@app.route('/enviar-contato', methods=['POST'])
def handle_contact_form():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Cria a mensagem de e-mail
        msg = Message(
            subject=f"Nova mensagem do site: {name}",
            recipients=[os.getenv('MAIL_RECIPIENT')], # Altere para o e-mail que receberá as mensagens
            body=f"Nome: {name}\nEmail: {email}\n\nMensagem:\n{message}"
        )

        try:
            # Envia a mensagem
            mail.send(msg)
            print("E-mail enviado com sucesso!")
            # Redireciona para uma página de sucesso
            return redirect(url_for('contato')) # Pode criar uma página de "obrigado.html"
        except Exception as e:
            print(f"Erro ao enviar o e-mail: {e}")
            return "Erro ao enviar a mensagem. Por favor, tente novamente.", 500

    return "Método não permitido", 405

# --- FIM DAS ROTAS ---

# Executar o aplicativo
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
