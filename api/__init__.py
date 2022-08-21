from flask import Blueprint, render_template

# Initializing blueprint
api = Blueprint('api', __name__, url_prefix='/api')


@api.get('/redoc')
def doc():
    ''' Endpoint to expose API Documentations
    '''
    return render_template('index.html')


@api.get('/ping')
def ping():
    ''' Endpoint will return 'pong' as a response
    '''
    try:
        return {'response': 'pong'}, 200
    except Exception as error:
        return error


@api.put('/restaurant')
def updateRestaurant():
    ''' Endpoint to update restaurant details
    '''
    try:
        return {
            "response": "Details updated successfully",
            "restaurantId": 123
        }, 200
    except Exception as error:
        return error


@api.get('/menu/<int:menuId>')
def getMenuById(menuId):
    ''' Endpoint will return menu
    '''
    try:
        return {'response': 'Menu unavailable, restaurant is temporarily closed'}, 200
    except Exception as error:
        return error
