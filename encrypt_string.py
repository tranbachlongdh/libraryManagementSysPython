import base64


# Reverse string than encode by base64
def encode_string(string):
    return base64.b64encode(bytes(string[::-1], 'utf-8'))


def decode_string(string):
    return base64.b64decode(string).decode('utf-8')[::-1]
