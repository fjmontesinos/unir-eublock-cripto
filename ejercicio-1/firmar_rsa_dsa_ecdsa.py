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

# Firmar con RSA y mostrar por consola
signatureRSA = crypto.firmarConRSA(privateRSAKey, fileContent)
print(f'Contenido del fichero:\n{fileContent.decode()}\nFirma RSA:\n{signatureRSA.hex()}')

# Firma con DSA
# .....................................................................................
# Generar claves DSA
privateDSAKey = crypto.generarClaveDSA()

# Firmar con RSA y mostrar por consola
signatureDSA = crypto.firmarConDSA(privateDSAKey, fileContent)
print(f'Firma DSA:\n{signatureDSA.hex()}')

# Firma con ECDSA
# .....................................................................................
# Generar claves ECDSA
privateECDSAKey = crypto.generarClaveECDSA()

# Firmar con ECRSA y mostrar por consola
signatureECDSA = crypto.firmarConECDSA(privateECDSAKey, fileContent)
print(f'Firma ECDSA:\n{signatureECDSA.hex()}')
