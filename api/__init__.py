from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/api')     # Initializing blueprint


@api.get('/ping')
def ping():
    '''
    Endpoint will return 'Pong' as a response
    '''
    try:
        return {'response':'Pong'}, 200
    except Exception as error:
        return error

@api.get('/menu/<int:menuId>')
def getMenuById(menuId):
    '''
    Endpoint will return manuId from url argument (default : 123)
    '''
    try:
        return {'response':menuId}, 200
    except Exception as error:
        return error

