from flask import Flask, request

app = Flask(__name__)
 
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username == 'admin' and password == '1234':
        return "Acesso concedido"

    return "Acesso negado"
 

if __name__ == '__main__':
    app.run(debug=True)
