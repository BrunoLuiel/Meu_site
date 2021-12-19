#https://www.youtube.com/watch?v=K2ejI4z8Mbg&ab_channel=HashtagPrograma%C3%A7%C3%A3o
from flask import Flask, render_template, request
import Calculadora as C

app = Flask(__name__)

@app.route("/index")
def homepage():
    return render_template("homepage.html")

@app.route("/resultado")
def resultado():
    args = request.args
    pesquisaCNPJ = args["CNPJ"]
    pesquisaCPF = args["CPF"]
    if pesquisaCNPJ != "":
        dv1 = C.Cnpj().calcula_digito_verificador(pesquisaCNPJ, 1)
        dv2 = C.Cnpj().calcula_digito_verificador(pesquisaCNPJ + str(dv1), 2)
        return render_template('homepage.html', digiCnpj = f'{dv1}{dv2}');

    elif pesquisaCPF!= "":
        dv1 = C.Cpf().calcula_digito_verificador(pesquisaCPF,1)
        dv2 = C.Cpf().calcula_digito_verificador(pesquisaCPF + str(dv1),2)
        return render_template('homepage.html', digiCpf = f'{dv1}{dv2}');
    
    else:
        print('O número dígitado não corresponde a consulta à um CPF ou CNPJ')

if __name__=='__main__':
    app.run(debug=True)