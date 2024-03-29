# imports necesarios
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding, dsa, ec
from cryptography.exceptions import InvalidSignature

from enum import Enum

# enumeración tipos de hashes disponibles
class HashType(Enum):
    SHA256 = 1
    MD5 = 2

class CryptoUNIR:
    # función que dada la ruta de un fichero retorna el contenido como bytes
    # ..........................................................................................
    def fileAsBytes(self, ruta):
        file = open(ruta, 'rb')
        contenido = file.read()
        file.close()
        return contenido

    # función que calcula el hash MD5 de una cadena e imprime resultado por pantalla
    # ..........................................................................................
    def calcularHash(self, hashType, mensaje , debug):  
        # Instanciar el tipo de hash MD5
        if(hashType == HashType.MD5):
            algorithm = hashes.MD5()
        elif (hashType == HashType.SHA256):
            algorithm = hashes.SHA256()
        else:
            print(f"Tipo de hash no contemplado: {hashType}")
            return

        digest = hashes.Hash(algorithm=algorithm, backend=default_backend())

        # Establecer el mensaje para calcular el hash deseado
        if(not isinstance(mensaje, (bytes, bytearray))):
            mensajeB = mensaje.encode()
            mensajePlano = mensaje
        else:
            mensajeB = mensaje
            mensajePlano = mensaje.decode()

        digest.update(mensajeB)

        # calcular el hash 
        mensajeHash = digest.finalize()

        # pasar el hash a hexadecimal
        mensajeHashHex = mensajeHash.hex()

        if(debug):
            print(f"El Hash {hashType.name} de: \n{mensajePlano}\nes: \n{mensajeHashHex}")
        
        return mensajeHashHex
        
    
    # Funcionalidad de Firma RSA, DSA y ECDSA
    # ..........................................................................................
    def generarClaveRSA(self):
        return rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())

    def firmarConRSA(self, privateKey, contenido):
        return privateKey.sign(
            contenido,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
        )
    
    def verificarFirmaRSA(self, publicKey, contenido, firma):
        try:
            publicKey.verify(
                firma,
                contenido,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                    ),
                hashes.SHA256()
            )

            return True

        except InvalidSignature:
            return False

    def generarClaveDSA(self):
        return dsa.generate_private_key(key_size=2048, backend=default_backend())

    def firmarConDSA(self, privateKey, contenido):
        return privateKey.sign(contenido, hashes.SHA256())

    def verificarFirmaDSA(self, publicKey, contenido, firma):
        try:
            publicKey.verify(firma, contenido, hashes.SHA256())

            return True

        except InvalidSignature:
            return False

    def generarClaveECDSA(self):
        return ec.generate_private_key(curve=ec.SECP256K1(), backend=default_backend())

    def firmarConECDSA(self, privateKey, contenido):
        return privateKey.sign(contenido, ec.ECDSA(hashes.SHA256()))

    def verificarFirmaECDSA(self, publicKey, contenido, firma):
        try:
            publicKey.verify(firma, contenido, ec.ECDSA(hashes.SHA256()))

            return True

        except InvalidSignature:
            return False