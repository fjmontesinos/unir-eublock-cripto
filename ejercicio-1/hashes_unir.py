# imports necesarios
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

from enum import Enum

# enumeración tipos de hashes disponibles
class HashType(Enum):
    SHA256 = 1
    MD5 = 2

class CryptoUNIR:
    # función que dada la ruta de un fichero retorna el contenido como bytes
    def fileAsBytes(self, ruta):
        file = open(ruta, 'rb')
        with file:
            return file.read()

    # función que calcula el hash MD5 de una cadena e imprime resultado por pantalla
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