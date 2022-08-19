from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from api import api

app = Flask(__name__)
app.config.from_prefixed_env()      # Loading variables from .env having "FLASK_" as prefix


# Swagger configurations
SWAGGER_URL = app.config['SWAGGER_URL']         # Swagger documentation endpoint
API_URL = app.config['API_URL']             # Swagger configuration file path
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "API Doc"
    }
)

app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)     # Registering swagger blueprint
app.register_blueprint(api)     # Registering api blueprint


if __name__=='__main__':
    app.run()
