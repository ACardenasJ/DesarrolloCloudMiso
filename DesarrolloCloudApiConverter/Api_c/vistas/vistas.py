from flask_restful import Resource
from flask import request
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required, create_access_token
import requests
import json

class statusCheck(Resource):
    def get(self):
        return {'status': 'ok'}

class VistaSingUp(Resource):
    def post(self):
        #@jwt_required()
        try:
            url_back = 'http://localhost:5000/signin/user'
            dataBudy = {'usuario' : request.json['usuario'],
                        'password1': request.json['password1'],
                        'password2': request.json['password2'],
                        'email': request.json["email"]}

            register = requests.post(url_back, json=dataBudy)  
            return register.json(), 200
        except ConnectionError as e:
            return {'error': 'Api_c SinguP offline -- Connection'}, 404
        except requests.exceptions.Timeout:
            # Maybe set up for a retry, or continue in a retry loop
            return {'error': 'Api_c SinguP offline -- Timeout'}, 404
        except requests.exceptions.TooManyRedirects:
            # Tell the user their URL was bad and try a different one
            return {'error': 'Api_c SinguP offline -- ManyRedirects'}, 404
        except requests.exceptions.RequestException as e:
            # catastrophic error. bail.
            return {'error': 'Api_c SinguP offline -- Request'}, 404
        except Exception as e:
            return {'error': 'Api_c SinguP - Error desconocido -' + str(e)}, 404

class VistaLogIn(Resource):
    def post(self):
        try:
            url_back = 'http://localhost:5000/login'
            dataBudy = {'usuario' : request.json['usuario'],
                        'password': request.json['password']}

            logIn = requests.post(url_back, json=dataBudy)  
            return logIn.json(), 200
        except ConnectionError as e:
            return {'error': 'Api_c Login offline -- Connection'}, 404
        except requests.exceptions.Timeout:
            # Maybe set up for a retry, or continue in a retry loop
            return {'error': 'Api_c Login offline -- Timeout'}, 404
        except requests.exceptions.TooManyRedirects:
            # Tell the user their URL was bad and try a different one
            return {'error': 'Api_c Login offline -- ManyRedirects'}, 404
        except requests.exceptions.RequestException as e:
            # catastrophic error. bail.
            return {'error': 'Api_c Login offline -- Request'}, 404
        except Exception as e:
            return {'error': 'Api_c Login - Error desconocido -' + str(e)}, 404

class VistaTasks(Resource):
    def get(self):
        try:
            url_back = 'http://localhost:5000/task'
            task = requests.get(url_back) 
            return task.json(), 200
        except ConnectionError as e:
            return {'error': 'Api_c getTask offline -- Connection'}, 404
        except requests.exceptions.Timeout:
            # Maybe set up for a retry, or continue in a retry loop
            return {'error': 'Api_c getTask offline -- Timeout'}, 404
        except requests.exceptions.TooManyRedirects:
            # Tell the user their URL was bad and try a different one
            return {'error': 'Api_c getTask offline -- ManyRedirects'}, 404
        except requests.exceptions.RequestException as e:
            # catastrophic error. bail.
            return {'error': 'Api_c getTask offline -- Request'}, 404
        except Exception as e:
            return {'error': 'Api_c getTask - Error desconocido -' + str(e)}, 404
    
class VistaTask(Resource):
    def post(self, id_task):
        try:
            url_back = 'http://localhost:5000/task'
            dataBudy = {'file_name' : request.json['fileName'],
                        'new_format': request.json['newFormat']}
            #TODO: faltan campos
            task = requests.post(url_back, json=dataBudy) 
            return task.json(), 200
        except ConnectionError as e:
            return {'error': 'Apic_c task post offline -- Connection'}, 404
        except requests.exceptions.Timeout:
            # Maybe set up for a retry, or continue in a retry loop
            return {'error': 'Apic_c task post offline -- Timeout'}, 404
        except requests.exceptions.TooManyRedirects:
            # Tell the user their URL was bad and try a different one
            return {'error': 'Apic_c task post offline -- ManyRedirects'}, 404
        except requests.exceptions.RequestException as e:
            # catastrophic error. bail.
            return {'error': 'Apic_c task post offline -- Request'}, 404
        except Exception as e:
            return {'error': 'Apic_c task post - Error desconocido -' + str(e)}, 404
    
    def get(self, id_task):
        try:
            url_back = 'http://localhost:5000/task/{}'.format(id_task)
            task = requests.get(url_back) 
            return task.json(), 200
        except ConnectionError as e:
            return {'error': 'Api_c getTask offline -- Connection'}, 404
        except requests.exceptions.Timeout:
            # Maybe set up for a retry, or continue in a retry loop
            return {'error': 'Api_c getTask offline -- Timeout'}, 404
        except requests.exceptions.TooManyRedirects:
            # Tell the user their URL was bad and try a different one
            return {'error': 'Api_c getTask offline -- ManyRedirects'}, 404
        except requests.exceptions.RequestException as e:
            # catastrophic error. bail.
            return {'error': 'Api_c getTask offline -- Request'}, 404
        except Exception as e:
            return {'error': 'Api_c getTask - Error desconocido -' + str(e)}, 404
    
    def put(self, id_task):
        try:
            url_back = 'http://localhost:5000/task/{}'.format(id_task)
            dataBudy = {'new_format': request.json['newFormat']}
            task = requests.put(url_back, json=dataBudy) 
            return task.json(), 200
        except ConnectionError as e:
            return {'error': 'Apic_c putTask offline -- Connection'}, 404
        except requests.exceptions.Timeout:
            # Maybe set up for a retry, or continue in a retry loop
            return {'error': 'Apic_c putTask offline -- Timeout'}, 404
        except requests.exceptions.TooManyRedirects:
            # Tell the user their URL was bad and try a different one
            return {'error': 'Apic_c putTask offline -- ManyRedirects'}, 404
        except requests.exceptions.RequestException as e:
            # catastrophic error. bail.
            return {'error': 'Apic_c putTask offline -- Request'}, 404
        except Exception as e:
            return {'error': 'Apic_c putTask - Error desconocido -' + str(e)}, 404

    def delete(self, id_task):
        try:
            url_back = 'http://localhost:5000/task/{}'.format(id_task)
            task = requests.delete(url_back) 
            return task.json(), 200
        except ConnectionError as e:
            return {'error': 'Apic_c deleteTask offline -- Connection'}, 404
        except requests.exceptions.Timeout:
            # Maybe set up for a retry, or continue in a retry loop
            return {'error': 'Apic_c deleteTask offline -- Timeout'}, 404
        except requests.exceptions.TooManyRedirects:
            # Tell the user their URL was bad and try a different one
            return {'error': 'Apic_c deleteTask offline -- ManyRedirects'}, 404
        except requests.exceptions.RequestException as e:
            # catastrophic error. bail.
            return {'error': 'Apic_c deleteTask offline -- Request'}, 404
        except Exception as e:
            return {'error': 'Apic_c deleteTask - Error desconocido -' + str(e)}, 404

class VistaFiles(Resource):
    def get(self, file_name):
        try:
            url_back = 'http://localhost:5000/files/{}'.format(file_name)
            task = requests.get(url_back) 
            return task.json(), 200
        except ConnectionError as e:
            return {'error': 'Api_c getFiles offline -- Connection'}, 404
        except requests.exceptions.Timeout:
            # Maybe set up for a retry, or continue in a retry loop
            return {'error': 'Api_c getFiles offline -- Timeout'}, 404
        except requests.exceptions.TooManyRedirects:
            # Tell the user their URL was bad and try a different one
            return {'error': 'Api_c getFiles offline -- ManyRedirects'}, 404
        except requests.exceptions.RequestException as e:
            # catastrophic error. bail.
            return {'error': 'Api_c getFiles offline -- Request'}, 404
        except Exception as e:
            return {'error': 'Api_c getFiles - Error desconocido -' + str(e)}, 404



    
   
            