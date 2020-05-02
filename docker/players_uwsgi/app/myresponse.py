from flask import Response, json

class MyResponse(Response):
        default_mimetype = 'application/json'

        def __init__(self, result=None, success=None, **kwargs):
            self.result = result
            self.success = success

            if self.success: # If success is True
                self.response = json.dumps({'result': self.result, 'success': self.success, 'errors': None})
                self.status_code = 200
            elif self.success == False: # If success is False
                self.response = json.dumps({'result': None, 'success': self.success, 'errors': self.result})
                self.status_code = 404
            else: # If success is None
                self.response = result
                self.status_code = 200

            super().__init__(response=self.response, status=self.status_code, **kwargs)
