from crypto_unir import CryptoUNIR
import os

crypto = CryptoUNIR()

# Leer el contenido del fichero
path = os.path.dirname(__file__) + "/"
fileName = 'TransaccionBitcoin.txt'
fileContent = crypto.fileAsBytes(path + fileName)

# Firma con RSA
# .....................................................................................
# Generar claves RSA
privateRSAKey = crypto.generarClaveRSA()
publicRSAKey = privateRSAKey.public_key()

# Firmar con RSA y mostrar por consola
signatureRSA = crypto.firmarConRSA(privateRSAKey, fileContent)
print(f'Contenido del fichero:\n{fileContent.decode()}\nFirma RSA:\n{signatureRSA.hex()}')

if(crypto.verificarFirmaRSA(publicRSAKey, fileContent, signatureRSA) == True):
    print("Firma RSA valida del contenido")
else:
    print("Firma RSA no valida del contenido")

print("...............................................................................")

# Firma con DSA
# .....................................................................................
# Generar claves DSA
privateDSAKey = crypto.generarClaveDSA()
publicDSAKey = privateDSAKey.public_key()

# Firmar con RSA y mostrar por consola
signatureDSA = crypto.firmarConDSA(privateDSAKey, fileContent)


from cryptography.hazmat.primitives.asymmetric import utils
print('Firma DSA  : ', utils.decode_dss_signature(signatureDSA))

if(crypto.verificarFirmaDSA(publicDSAKey, fileContent, signatureDSA) == True):
    print("Firma DSA valida del contenido")
else:
    print("Firma DSA no valida del contenido")

print("...............................................................................")

# Firma con ECDSA
# .....................................................................................
# Generar claves ECDSA
privateECDSAKey = crypto.generarClaveECDSA()
publicECDSAKey = privateECDSAKey.public_key()

# Firmar con ECRSA y mostrar por consola
signatureECDSA = crypto.firmarConECDSA(privateECDSAKey, fileContent)
print('Firma ECDSA: ', utils.decode_dss_signature(signatureECDSA))

if(crypto.verificarFirmaECDSA(publicECDSAKey, fileContent, signatureECDSA) == True):
    print("Firma ECDSA valida del contenido")
else:
    print("Firma ECDSA no valida del contenido")
