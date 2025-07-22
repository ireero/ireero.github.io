from flask import Blueprint

# Cria o blueprint
main = Blueprint('main', __name__)

# Importa as rotas para registrá-las nesse blueprint
from . import routes