from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import base64
import hashlib
import cryptography
import ssl

with open('private_key.pem', 'rb') as f:
    key_data = f.read()

print("Cryptography:", cryptography.__version__)
print("OpenSSL:", ssl.OPENSSL_VERSION)
print("PEM length:", len(key_data))
print("PEM SHA256:", hashlib.sha256(key_data).hexdigest())
print("PEM header:", key_data.splitlines()[0])
print("PEM footer:", key_data.splitlines()[-1])

loaded_private_key = serialization.load_pem_private_key(
    key_data,
    password=None
)

print("RSA key loaded successfully")


def sign(uuid):
    signature = loaded_private_key.sign(
        bytes(uuid, 'utf-8'),
        padding.PKCS1v15(),
        hashes.SHA256()
    )

    return base64.b64encode(signature).decode('utf-8')
