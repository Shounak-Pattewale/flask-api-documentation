from flask_swagger_ui import get_swaggerui_blueprint


def swaggerBlueprint(SWAGGER_URL, API_URL):
    ''' Swagger configurations
    '''

    SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "API Doc"
        }
    )

    return SWAGGERUI_BLUEPRINT
