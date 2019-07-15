import base64


def encode_string(string):
    return base64.b64encode(bytes(string, 'utf-8'))


def decode_string(string):
    return base64.b64decode(string).decode('utf-8')
