from flask import Flask, render_template, redirect, request, flash
from flask_mail import Mail, Message
from config import email,senha

app = Flask(__name__)
app.secret_key = 'obrabodogalo'

mail_settings = {

    "MAIL_SERVER": 'smtp.hostinger.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": email,
    "MAIL_PASSWORD": senha

}

app.config.update(mail_settings)

mail = Mail(app)

class Contato:
    def __init__(self, nome, email, mensagem):
        self.nome = nome
        self.email = email
        self.mensagem = mensagem



@app.route('/')

def index():
    return render_template('index.html')

@app.route('/adelzonilton')
def adelzonilton():
    return render_template('Adelzonilton.html')

@app.route('/bimba')
def bimba():
    return render_template('bimba.html')

@app.route('/russo')
def russo():
    return render_template('russo.html')

@app.route('/nilo')
def nilo():
    return render_template('nilo.html')

@app.route('/nilson')
def nilson():
    return render_template('nilson.html')

@app.route('/barberin')
def barberin():
    return render_template('barberin.html')

@app.route('/gil')
def gil():
    return render_template('gil.html')

@app.route('/baes')
def baes():
    return render_template('baes.html')

@app.route('/popular')
def popular():
    return render_template('popular.html')

@app.route('/sergin')
def sergin():
    return render_template('sergin.html')

@app.route('/roxinho')
def roxinho():
    return render_template('roxinho.html')

@app.route('/pinga')
def pinga():
    return render_template('pinga.html')

@app.route('/rody')
def rody():
    return render_template('rody.html')

@app.route('/pqd')
def pqd():
    return render_template('pqd.html')

@app.route('/titio')
def titio():
    return render_template('titio.html')

@app.route('/bombeiro')
def bombeiro():
    return render_template('bombeiro.html')

@app.route('/show')
def show():
    return render_template('show.html')
    
@app.route('/adelino')
def adelino():
    return render_template('adelino.html')

@app.route('/betosembraco')
def betosembraco():
    return render_template('betosembraco.html')

@app.route('/claudinho')
def claudinho():
    return render_template('claudinho.html')

@app.route('/criolodoido')
def criolodoido():
    return render_template('criolodoido.html')

@app.route('/gmartins')
def gmartins():
    return render_template('gmartins.html')

@app.route('/joel')
def joel():
    return render_template('joel.html')

@app.route('/juarez')
def juarez():
    return render_template('juarez.html')

@app.route('/marcosdiniz')
def marcosdiniz():
    return render_template('marcosdiniz.html')

@app.route('/luizgrande')
def luizgrande():
    return render_template('luizgrande.html')

@app.route('/naval')
def naval():
    return render_template('naval.html')

@app.route('/neguinbeijaflor')
def neguinbeijaflor():
    return render_template('neguinbeijaflor.html')

@app.route('/botina')
def botina():
    return render_template('botina.html')

@app.route('/meriti')
def meriti():
    return render_template('meriti.html')

@app.route('/walmirpurific')
def walmirpurific():
    return render_template('walmirpurific.html')

@app.route('/ronaldao')
def ronaldao():
    return render_template('ronaldao.html')

@app.route('/miltinho')
def miltinho():
    return render_template('miltinho.html')


@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        formContato = Contato(
            request.form["nome"],
            request.form["email"],
            request.form["mensagem"]
        )

        msg = Message(
            subject = f'{formContato.nome} te enviou msg do site bezerrao',
            sender = app.config.get("MAIL_USERNAME"),
            recipients = ['guigowtech@gmail.com', app.config.get("MAIL_USERNAME")],
            body = f'''
            
            {formContato.nome} com o email {formContato.email}, te enviou a seguinte mensagem:

            {formContato.mensagem} 

            '''
        )
        mail.send(msg)
        flash('Mensagem enviada com sucesso!')

    return redirect('/')






if __name__ == '__main__':

    app.run(debug=True)

