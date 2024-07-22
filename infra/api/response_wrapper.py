class ResponseWrapper:
    def __init__(self, ok, status, data):
        self.ok = ok
        self.status = status
        self.data = data
