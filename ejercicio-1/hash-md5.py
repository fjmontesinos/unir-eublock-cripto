from hashes_unir import HashType, CryptoUNIR

path = '/home/javier/UNIR-Blockchain/01-Introducción Blockchain/actividad-python/ejercicio-1/'
fileName = 'TransaccionBitcoin.txt'

crypto = CryptoUNIR()
fileContent = crypto.fileAsBytes(path + fileName)
crypto.calcularHash(HashType.MD5, fileContent, True)