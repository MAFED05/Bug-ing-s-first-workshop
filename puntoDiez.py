# Tenemos la velocidad de la luz
VelocidadDeLaLuz = 299792458

# Definimos la velocidad del sonido en metros por segundo a 20 grados Celsius, pues esta velocidad varia dependiendo de diferentes factores
VelocidadDelSonido = 343

#Velocidad del auto
VelocidadDelAuto = 136.2444

#Velocidad de Bolt
VelocidadBolt= 12.42

#Luego le solicitamos al usuario que ingrese la distancia en metros
Distancia = float(input("Ingrese la distancia en metros: "))

#Realizamos la división de la distancia entre la velocidad de la luz para encontrar el tiempo
Tiempo = Distancia / VelocidadDeLaLuz
Tiempo_Redondeado = round(Tiempo, 8)
#Imprimimos el resultado final
print("El tiempo que le tomaría a la luz recorrer", Distancia, "metros es de", Tiempo_Redondeado, "segundos.")


# Calcular el tiempo que le tomaría al sonido recorrer la distancia, dividiendo la distancia ingresada por la velocidad del sonido
tiempo = Distancia / VelocidadDelSonido
tiempo_redondeado = round(tiempo, 4)
# Imprimir el resultado
print("El tiempo que le tomaría al sonido recorrer", Distancia, "metros en el aire es de", tiempo_redondeado, "segundos.")


#Ahora revisaremos cuánto tiempo le tomaría al auto más veloz del mundo recorrer dicha distancia
Time = Distancia / VelocidadDelAuto
TimeRedondeado = round (Time, 4 )
#Imprimir el resultado
print ("El tiempo que le tomaría al auto más veloz del mundo recorrer", Distancia, " metros es de ",  TimeRedondeado, " segundos")


#Finalmente calcularemos el tiempo que le tomará a Bolt recorrer la distancia ingresada
time = Distancia / VelocidadBolt
timeRedondeado = round (time, 4)
#Imprimir el resultado
print ("El tiempo que le tomaría a Bolt recorrer", Distancia, "metros es de", timeRedondeado, "segundos")