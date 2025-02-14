# https://www.geeksforgeeks.org/password-hashing-with-bcrypt-in-flask/

from flask import Flask , request
from flask_bcrypt import Bcrypt 

app = Flask(__name__) 
bcrypt = Bcrypt(app) 

_dbPassword = "test"  # Senha do sistema.


@app.route('/login', methods=['POST']) 
def login(): 

    username = request.authorization.parameters['username']  # Basic Auth no Postman.
    password = request.authorization.parameters['password']

    hashedPassword = bcrypt.generate_password_hash (password).decode('utf-8') # Senha criptografada.
    is_valid = bcrypt.check_password_hash (hashedPassword, _dbPassword)
    
    return "Acesso concedido" if (username == 'admin') and is_valid else "Acesso negado"


if __name__ == '__main__':
    app.run(host="0.0.0.0")