class Error:
    errors = (
        {'id': '0001', 'message': 'Invalid Field(s)'},
        {'id': '0002', 'message': 'Player already exists'},
        {'id': '0003', 'message': 'Player does not exist'},
        {'id': '0004', 'message': 'Missing key(s)'}
        )

    @classmethod
    def id(self, id):
        for row in self.errors:
            if row['id'] == id:
                return row
