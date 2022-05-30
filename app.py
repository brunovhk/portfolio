from flask import Flask, render_template, redirect, request, flash
import gzip
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = 'brunoportfolio'

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": os.getenv("EMAIL"),
    "MAIL_PASSWORD": os.getenv("SENHA"),
}

app.config.update(mail_settings)

mail = Mail(app)


class Contato:
    def __init__(self, nome, email, msg):
        self.nome = nome
        self.email = email
        self.msg = msg


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        formContato = Contato(
            request.form["nome"],
            request.form["email"],
            request.form["mensagem"]
        )
        msg = Message(
            subject=f'{formContato.nome} te enviou uma mensagem no portfólio',
            sender=app.config.get("MAIL_USERNAME"),
            recipients=['brunorick11@gmail.com', app.config.get("MAIL_USERNAME")],
            body=f'''
            {formContato.nome} com o e-mail {formContato.email}, te enviou a seguinte mensagem:
            {formContato.msg}
            '''
        )
        mail.send(msg)
        flash('Mensagem enviada com sucesso!')
    return redirect('/')


@app.after_request
def compress(response):
    accept_encoding = Flask.request.headers.get('accept-encoding', '').lower()
    if response.status_code < 200 or response.status_code >= 300 or response.direct_passthrough or 'gzip' not in accept_encoding or 'Content-Encoding' in response.headers:  return response
    content = gzip.compress(response.get_data(),
                            compresslevel=9)  # 0: no compression, 1: fastest, 9: slowest. Default: 9
    response.set_data(content)
    response.headers['content-length'] = len(content)
    response.headers['content-encoding'] = 'gzip'
    return response


if __name__ == '__main__':
    app.run(debug=True)
