import requests

class MyrequestFilter(requests.Session):
    def __init__(self):
        super().__init__()
    def request(self,method, url, *args, **kwargs):
        print(f"[Request] {method} {url} other info {kwargs}:")
        if "headers" not in kwargs :
            kwargs["headers"] = {}
        return super().request(method, url, *args, **kwargs)
    def send(self, request, **kwargs):
        response = super().send(request, **kwargs)
        print(f"[ResponseFilter] {response.status_code}")
        # Example: log response length
        print(f"Response is: {response.text}")
        return response   