from flask import json

def generate_view(result, success):
    if success: # If success is True
        response = json.dumps({'result': result, 'success': success, 'errors': None})
        status_code = 200
    elif success == False: # If success is False
        response = json.dumps({'result': None, 'success': success, 'errors': result})
        status_code = 404
    else: # If success is None
        response = result
        status_code = 200
    return response, status_code
