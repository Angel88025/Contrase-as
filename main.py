import random
contrasena = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
Pregunta = int(input("¿Cuantas carecteres quieres?"))
Almacenamiento = ""
for i in range(Pregunta):
    Almacenamiento +=random.choice(contrasena)

print(Almacenamiento)  
