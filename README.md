# UNIR - Experto Universitario en Desarrollo Blockchain - Práctica Criptografía

Repositorio destinado a recoger la práctica basada en criptografía del curso Experto Universitario en Blockchain de UNIR.

## Calcular Hashes con SHA256 y MD5

En este apartado vamos a estudiar diferentes propiedades de las funciones hash:

* Calcula el hash SHA-256 de «Estamos aplicando de forma práctica los conocimientos de criptografia». Ten en cuenta no incluir tildes en el texto y muestra el resultado en hexadecimal.
* Calcula el hash SHA-256 de «criptografia». Ten en cuenta no incluir tildes en el texto y muestra el resultado en hexadecimal.
* Los textos anteriores tienen diferente longitud, ¿qué sucede con la longitud de los hashes de ambos mensajes?
* Calcula el hash SHA-256 de «criptografio». Ten en cuenta no incluir tildes en el texto y muestra el resultado en hexadecimal.
* Compara el resultado obtenido en b) y d). El texto solo varía en un carácter, ¿cómo afecta esto al resultado de los hashes obtenidos?
* Utilizando la librería cryptography de Python calcula el hash MD5 del fichero «TransacciónBitcoin.txt».

## Firmar contenido de un fichero con RSA, DSA y ECDSA

Vamos a practicar con las firmas digitales:

* En primer lugar, vamos a emplear el algoritmo RSA para firmar. Para ello, genera un par de claves pública y privada de 2048 bits usando el exponente 65537.
* ¿Qué es el padding y para qué se usa?
* Firma con RSA el contenido del fichero «TransacciónBitcoin.txt». Utiliza PSS como padding y los parámetros por defecto que vienen en la documentación de la librería. Muestra la firma en hexadecimal. ¿Con qué clave has firmado?
* Verifica la firma. ¿Con qué clave lo haces? ¿Qué particularidad tiene este ejercicio?
* Firma con DSA el contenido del fichero «TransacciónBitcoin.txt». Utiliza una clave de 2048 bits. Imprime la firma, ¿qué diferencias observas con la firma generada por RSA? Verifica la firma.
* Firma con ECDSA el contenido del fichero «TransacciónBitcoin.txt». Utiliza la curva elíptica SECP256K1. Imprime la firma, ¿qué diferencias observas con las firmas anteriores? Verifica la firma.

 
## Objetivos de la práctica

El objetivo de esta actividad es asentar los conceptos estudiados en relación con la Criptografía y el contenido del primer módulo. Para ello se propone una actividad práctica de programación con Python que ayudarán a asimilar los conceptos estudiados y que éstos se puedan llevar a la práctica, incluyendo ejercicios relacionados con las funciones hash y las firmas digitales.

## Criterios de evaluación

* Se valorarán las respuestas claras y concisas.
* Es necesario argumentar y explicar cómo se ha resuelto cada ejercicio.
* Se deben incluir capturas de pantalla adjuntas que expliquen el proceso seguido para la resolución de la actividad.
* Se debe adjuntar el fichero .py generado con la solución de los ejercicios propuestos.
* Se valorará un trabajo original y personal.
* Es necesario citar en APA.
