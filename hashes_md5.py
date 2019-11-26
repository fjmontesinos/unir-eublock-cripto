from crypto_unir import HashType, CryptoUNIR
import os

path = os.path.dirname(__file__) + "/"
fileName = 'TransaccionBitcoin.txt'

crypto = CryptoUNIR()
fileContent = crypto.fileAsBytes(path + fileName)
crypto.calcularHash(HashType.MD5, fileContent, True)