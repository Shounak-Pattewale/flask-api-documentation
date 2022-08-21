from flask import Flask
from api import api
from swaggerConfig import swaggerBlueprint

app = Flask(__name__)

# Loading variables from .env having "FLASK_" as prefix
app.config.from_prefixed_env()

# Swagger documentation endpoint
SWAGGER_URL = app.config['SWAGGER_URL']

# Swagger configuration file path
API_URL = app.config['API_URL']


# Registering blueprints
app.register_blueprint(swaggerBlueprint(
    SWAGGER_URL, API_URL), url_prefix=SWAGGER_URL)

app.register_blueprint(api)

if __name__ == '__main__':
    app.run()
