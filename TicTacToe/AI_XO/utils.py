

def get_value(request, param):
    if param in request:
        return request[param]
    return ""
