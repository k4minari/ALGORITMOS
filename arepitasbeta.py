# El programa va a iniciar interactuando con el usuario

input("¿Estas listo para hacer unas arepas? ")

# A continuacion el programa le preguntara al usuario que cantidad de cada cosa va a desear utilizar

cantidad_harina = int(input("¿cuantas tazas de harina utilizaras? "))
cantidad_agua = int(input("¿cuantas tazas de agua utilizaras? "))
cantidad_sal = int(input("¿cuantas cucharadas de sal utilizaras? "))
cantidad_aceite = int(input("¿cuantas cucharadas de aceite utilizaras? "))

# Las variables se van a establecer para poder tener los valores que el usuario indique con sus respectivas conversiones

harina = cantidad_harina
agua = cantidad_agua
sal = float(cantidad_sal/16/3)
aceite = float(cantidad_aceite/16)

# En esta parte se realiza el calculo de la cantidad de masa y el valor al colocar la arepa en el budare

print("llego el momento de juntar todos los ingredientes en un bowl")
bowl = harina + agua + sal
print("Tu cantidad de masa total es de: " + str(bowl))
print("es momento de colocarlas en el budare")
budare = int(bowl + aceite*0.75)
print("Ya estan listas, al sacarlas del budare tienes como resultado: " + str(budare) + " ahora a disfrutar :D")