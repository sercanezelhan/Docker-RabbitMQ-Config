from __future__ import print_function
import base64
import os
import hashlib
import struct
import getpass

password = getpass.getpass("password: ")
salt = os.urandom(4)
tmp0 = salt + password.encode('utf-8')
tmp1 = hashlib.sha256(tmp0).digest()
salted_hash = salt + tmp1
pass_hash = base64.b64encode(salted_hash)
print(pass_hash)
