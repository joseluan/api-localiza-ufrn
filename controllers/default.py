from app import app
from tika import parser
from flask import request
from controllers.funcions import *
import re
import requests
import json

config = json.load(open('config.json'))

@app.route('/')
def index():
    return {'Horarios': {
        '35T12': 'FMC II'
    }}
    
@app.route('/horarios', methods=['POST'])
def horarios():
    try:
        if 'pdf_atestado' in request.files:            
            file = request.files['pdf_atestado']
            raw = parser.from_buffer(file.read(), config['url_tika'])
            content = raw['content']
            return {'message': 'sucesso',
                    'status': 'lu00',
                    'content': get_horarios(content)}
        else:
            return {'message': 'erro como pdf',
                    'status': 'lu01',
                    'content': ''}
    except KeyError as e:
        return {'message': 'exception',
                'status': 'lu02',
                'content': e}

@app.route('/disciplinas', methods=['POST'])
def disciplinas():
    try:
        if 'pdf_atestado' in request.files:            
            file = request.files['pdf_atestado']
            raw = parser.from_buffer(file.read(), config['url_tika'])
            content = raw['content']
            return {'message': 'sucesso',
                    'status': 'lu00',
                    'content': get_disciplinas(content)}
        else:
            return {'message': 'erro como pdf',
                    'status': 'lu01',
                    'content': ''}
    except KeyError as e:
        return {'message': 'exception',
                'status': 'lu02',
                'content': e}        

@app.errorhandler(Exception)
def internal_error(error):
    return {'message': 'exception with request',
            'status': 'lu03',
            'content': ''}