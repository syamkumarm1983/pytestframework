import requests

class MyAPIClient:
    def __init__(self, base_url: str, session: requests.Session):
        self.baseurl = base_url
        self.session = session
        
    def get(self, endpoint, **kwargs):
        headers = kwargs.get('headers', {})
        headers = self.session.headers
        kwargs['headers'] = headers
        return self.session.get(f"{self.baseurl}{endpoint}", **kwargs)

    def post(self, endpoint, data=None, **kwargs):
        headers = kwargs.get('headers', {})
        headers = self.session.headers
        kwargs['headers'] = headers
        return self.session.post(f"{self.baseurl}{endpoint}", json=data, **kwargs)

    def put(self, endpoint, data=None, **kwargs):
        headers = kwargs.get('headers', {})
        headers = self.session.headers
        kwargs['headers'] = headers        
        return self.session.put(f"{self.baseurl}{endpoint}", json=data, **kwargs)

    def delete(self, endpoint, **kwargs):
        headers = kwargs.get('headers', {})
        headers = self.session.headers
        kwargs['headers'] = headers        
        return self.session.delete(f"{self.baseurl}{endpoint}", **kwargs)
    
       