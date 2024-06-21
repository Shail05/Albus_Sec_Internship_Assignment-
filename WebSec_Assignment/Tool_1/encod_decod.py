import base64

def encrypt_pass(password):
    encode_bytes = base64.b64encode(password.encode())
    print(encode_bytes)
    
user_pass = input("enter your password:")
encrypt_pass(user_pass)

import base64

def decode_pass(password):
    decode_bytes = base64.b64decode(password)
    decode_data = decode_bytes.decode()
    print(f"your decoded password is {decode_data} ")   
    
encoded_string = input("enter encoded code:")
decode_pass(encoded_string)