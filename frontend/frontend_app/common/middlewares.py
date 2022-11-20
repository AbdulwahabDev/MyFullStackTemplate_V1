from fastapi import Request

class MyMiddleware:
    def __init__(
            self,
            some_attribute: str,
    ):
        self.some_attribute = some_attribute

    def __call__(self, request: Request, call_next):
        # do something with the request object
        e = str(request.headers)
        content_type = request.headers.get('Content-Type')
        print(content_type)
        
        # process the request and get the response    
        response = call_next(request)
        
        return response
