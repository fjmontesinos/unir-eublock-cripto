from crypto_unir import HashType, CryptoUNIR

crypto = CryptoUNIR()

mensaje1 = 'Estamos aplicando de forma practica los conocimientos de criptografia'
mensaje1Hash = crypto.calcularHash(HashType.SHA256, mensaje1, True)

mensaje2 = 'criptografia'
mensaje2Hash = crypto.calcularHash(HashType.SHA256, mensaje2, True)

if( len(mensaje1Hash) == len(mensaje2Hash) ):
    print("El hash SHA256 de los mensajes 1 y 2 son iguales en tamaño")
else:
    print("El hash SHA256 de los mensajes 1 y 2 NO son iguales en tamaño")

mensaje3 = 'criptografio'
mensaje3Hash = crypto.calcularHash(HashType.SHA256, mensaje3, True)