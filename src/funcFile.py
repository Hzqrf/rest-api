""" Module Name: 
    All function that required for the application

    Created By: Haziq
    Created: 18/06/2025
    Framework: Python 3.10

    Last Edited: 180625
     Reason Edited: create function connection
"""

# source : library
# usage : read json file
import json

# source : library
# usage : encyption library
from cryptography.fernet import Fernet

fernetKey = 'joiyKed1p78GJQ-N2MtEdHfOZ8gzlxe4I7GEyoMTm1Q='

# encypt password personnel
def funcEncrypt(strPassword):
    # get fernet key
    cipher_suite = Fernet(fernetKey)
    # change the password type string to byte
    strPwEncrypt = strPassword.encode('utf-8')
    # encrypt the password
    strEncrypted = cipher_suite.encrypt(strPwEncrypt)
    # decode from byte to string so it can be passed to jsonify
    strPwDecode = strEncrypted.decode('utf-8')

    return strPwDecode

# decypt password personnel
def funcDecrypt(strEnPassword):
    # get fernet key
    cipher_suite = Fernet(fernetKey)
    strPwDecode = strEnPassword.encode('utf-8')
    # decrypt the password
    strDecryptedPw = cipher_suite.decrypt(strPwDecode)
    # decode from byte to string so it can be passed to jsonify
    strPwDecode = strDecryptedPw.decode('utf-8')

    return strPwDecode