"""
Usando Flask, crie uma API simples com dois endpoints:
GET /saudacao?nome=SeuNome que retorna uma mensagem de saudação personalizada.
POST /soma que recebe um JSON com dois números e retorna a soma.
"""

# https://www.geeksforgeeks.org/access-the-query-string-in-flask-routes/
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)


@app.route('/saudacao', methods=['GET'])
def saudacao():
    """
        Endpoint para retornar uma mensagem de saudação.
        Retorna "Bom dia", "Boa tarde" ou "Boa noite", dependendo do horário.
        O nome do usuário é obrigatório para a saudação. 
    """
    
    name:str = request.args.get('nome', None)

    message = ""
    if name is not None:
        hour = datetime.now().hour
        
        if (hour >= 6) and (hour <= 12):
            message = "Bom dia "
        elif (hour > 12) and (hour <= 18):
            message = "Boa tarde "
        else:
            message = "Boa noite "
        
        message += name + '\U0001F603'  # Unicode Emoji.
        
    else:
        # <HTML>
        message = """
        Instruções para receber uma mensagem personalizada:
        <br><br>
        GET /saudacao?nome=SeuNome
        <br>
        Exemplo:
        /saudacao=Willian"""
        
    return message 


# https://stackoverflow.com/questions/20001229/how-to-get-posted-json-in-flask
@app.route("/soma", methods=['POST'])
def sum():
    """
        Soma dois números.
        Não retorna a soma se forem passados mais de dois números.
        Os parâmetros podem ser enviados como inteiros (INT) ou (STR) que representem números.
    """
    
    errorMessage:str = "Sistema realiza a soma apenas dois números"
    keyMessage:str = "Erro"
    sumResult:int = 0
    
    content:dict = request.get_json()
    
    if len(content) == 2: # OK
        try:
            for _, value in content.items():
                sumResult += int(value)  # Mesmo sendo enviado como string, o sistema efetua o cálculo.
            
            errorMessage:str = sumResult
            keyMessage:str = "Resultado"

        except Exception:
            errorMessage = "Deve ser passado apenas números para a soma !"

    # https://stackoverflow.com/questions/13081532/return-json-response-from-flask-view
    return jsonify({keyMessage: errorMessage})
    

if __name__ == "__main__":
    app.run(host="0.0.0.0")