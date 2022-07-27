# Flask Imports #
from src.e_Infra.b_Builders.FlaskBuilder import *


@app.route('/test', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def example_route():
    if request.method == 'GET':
        response = 'GET\n' + str(request.data)
        print("GET Route Call", flush=True)
        return response

    elif request.method == 'POST':
        response = 'POST\n' + str(request.data)
        print("POST Route Call", flush=True)
        return response

    elif request.method == 'PATCH':
        response = 'PATCH\n' + str(request.data)
        print("PATCH Route Call", flush=True)
        return response

    elif request.method == 'PUT':
        response = 'PUT\n' + str(request.data)
        print("PUT Route Call", flush=True)
        return response

    elif request.method == 'DELETE':
        response = 'DELETE\n' + str(request.data)
        print("DELETE Route Call", flush=True)
        return response
