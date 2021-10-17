import random

input("  🅿🅰🆂🆂 \n → Presione Enter para generar nueva contraseña   \n Para ir al almacenamiento de contraseñas → python3 pswd.py \n Para salir → Exit  ")

minus = "abcdefghijklmnopqrstuvwxyz"
mayus = minus.upper()
numeros = "0123456789"
simbolos = "@()/[]}=?¿!·#~$-_*+ç'¡"
 
base = minus+mayus+numeros+simbolos
longitud = 12

muestra = random.sample(base, longitud)
password = "".join(muestra)
print(password)



