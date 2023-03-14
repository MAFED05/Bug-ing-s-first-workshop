# Bug.ing's first workshop

Bienvenidos a este, nuestro primer taller, el primer taller de Bug.ing 🐞

[![Logo-programaci-n.png](https://i.postimg.cc/d0grbQKt/Logo-programaci-n.png)](https://postimg.cc/d7mhdY1z)

Nosotros somos un grupo conformado por 3 ingenieros presentados a continuación 🤓😎

+ Cristian Felipe Gutiérrez Espitia : Ingeniero agrícola 🌾

+ Jhon Steven Padilla Goyes : Ingeniero Eléctrico ⚡

+ María Fernanda Duarte Parra : Ingeniera industrial 🏢

Durante este taller, realizamos el desarrollo de 9 puntos de programación diferentes que serán expuestos más adelante y un quiz inicial. 😶‍🌫️

Así que sin más que decir, iniciemos con el quiz; que es el primer punto

**Nota:** Los puntos pares estarán en archivos de extensión .py, mientras que los impares estarán en un archivo .ypynb (Notebook de Python)

## Quices (Primer punto)

Este quiz estaba conformado por 20 preguntas y debíamos acertar mínimo en el 90% de estas. Este punto lo realizamos de forma individual y las evidencias están adjuntas a continuación:

+ Quiz María Fernanda Duarte 🌺

[![Whats-App-Image-2023-03-10-at-11-46-31-PM.jpg](https://i.postimg.cc/8CGjMFDv/Whats-App-Image-2023-03-10-at-11-46-31-PM.jpg)](https://postimg.cc/Xr2j0YrN)

+ Quiz Jhon Steven Padilla 🎼



+ Quiz Cristian Felipe Gutiérrez 🎮



Después de haber completado este punto de manera individual, comenzamos a crear programas dependiendo de lo solicitado por el profesor.


**Nota:** Durante el taller podrán encontrar 3 diagramas de flujo pertenecientes a 3 de los puntos del taller. Estos fueron definidos con base en el último dígito de nuestra cédula

## Segundo punto 🧮

Realice un programa que lea tres números reales y determine cuál es el mayor.

Este punto lo podemos encontrar en el documento [puntoDos.py](/puntoDos.py) donde:

En este punto le solicita ingresar 3 números reales, esto se logra por medio del "input", despúes de esto, aunque antes de eso definimos los 3 números como reales, que se vería algo así:

``` python
a : float
b : float
c : float
a =float (input("Ingrese un número real"))
b =float (input("Ingrese un número real"))
c =float (input("Ingrese un número real"))
```

Y después de esto entonces definimos los condicionales que nos ayudarán a ejecutar el programa:

Para esto entonces si el primer número es mayor que el segundo y el tercero entonces se imprimirá el primero. Por el contrario si el segundo número es mayor que el primero y mayor que el tercero entonces se tendría que imprimir el segundo o en caso de que el tercero sea mayor que los 2 anteriores, pues se imprimiría el tercero. De esta manera el programa siempre imprimirá el número mayor. 

Los condicionales tienen que verse da la siguiente forma:

``` python
if a>b and a>c :
    print (str(a))
if b>a and b>c : 
    print (str(b))
if c>a and c>b :
    print (str(c))
```

Y finalmente el código se puede ver de la siguiente forma:


``` python
a : float
b : float
c : float
a =float (input("Ingrese un número real"))
b =float (input("Ingrese un número real"))
c =float (input("Ingrese un número real"))
if a>b and a>c :
    print (str(a))
if b>a and b>c : 
    print (str(b))
if c>a and c>b :
    print (str(c))
```

Y de esta manera ya tendríamos el código para el segundo punto, que si lo corremos se ejecutaría de la siguiente manera:

[![Captura-de-pantalla-2023-03-14-172159.png](https://i.postimg.cc/Qdp6Nj7f/Captura-de-pantalla-2023-03-14-172159.png)](https://postimg.cc/nXhK0b0m)

Para este punto podemos conseguir el siguente diagrama de flujo:

## Tercer punto 👾

Realice un programa que lea un número enteros y determine si es par o impar.

Este punto es un poco más fácil, pues aquí solo se solicitamos al usuario un número entero anteriormente definido. Después de esto le solicitamos al programa que realice una módulo que retornará el residuo de una división, si el residuo es '0' entonces el número ingresado será par, mientras que si su resultado es '1' entonces el número será par: 

El código se podrá ver de la siguente forma en [tallerUno.ipynb](/tallerUno.ipynb):

**Nota:** Recordemos que la igualdad en Python la mostramos por medio de '=='

``` python
# Punto 3
a : int
a = int (input("Ingrese un número entero"))
if a % 2 == 0 :
    print ((str(a)) + " es par")
elif a % 2 == 1 : 
    print (str(a) + " es impar")
``` 

Y si lo corremos en el terminal podríamos ver algo así:

[![Captura-de-pantalla-2023-03-14-173315.png](https://i.postimg.cc/HkVy3zYX/Captura-de-pantalla-2023-03-14-173315.png)](https://postimg.cc/75rhZgTZ)

Continuamos con el siguiente punto

## Cuarto punto 🔋

Realice un programa que lea dos números reales y determine si el primero es múltiplo del segundo.
 
En este caso le solicitamos al usurio que ingrese 2 números colocando 'input', como se ha visto reflejado en los ejercicios anteriores. Después de esto dividiremos el primer número entre el segundo número. Si el residuo de esta división es 0 entonces podremos decir que el primer número es múltiplo del segundo, de lo contrario estos 2 no serán multiplos.

El código se vería de la siguiente manera en el archivo [puntoCuatro.py](/puntoCuatro.py):

``` python
a: float
b: float
a = float (input("Ingrese un número real "))
b = float (input("Ingrese un número real "))
if a % b == 0 :
    print (str(a) + " es múltiplo de " + str(b))
elif a % b != 0 :
    print (str(a) + " no es múltiplo de " + str(b))
```
 
Y si lo corremos en el terminal obtendríamos lo siguiente:

[![Captura-de-pantalla-2023-03-14-180235.png](https://i.postimg.cc/Dzskr9RD/Captura-de-pantalla-2023-03-14-180235.png)](https://postimg.cc/kVnp9pJF)

Ya casi llegamos a la mitad, entonces ahora vamos al quinto punto

## Quinto punto ✨

Realice un programa que lea tres números reales y determine si la suma de los dos primeros es mayor, menor o igual que el tercer número.

Este punto lo podemos encontrar en [tallerUno.ipynb](/tallerUno.ipynb). En este caso le volvemos a solicitar al usuario que ingrese 3 números reales y el siguente paso será sumar los 2 primeros números ingresados y determinar si la suma de estos 2 es mayor, menor o igual al tercer número. 


``` python
# Punto 5
a: float
b: float
c: float
a= float (input("Ingrese un número real"))
b= float (input("Ingrese un número real"))
c= float (input("Ingrese un número real"))
if a+b > c :
    print (str(a) + (" + ") + str(b) + (" es mayor que ") +  (str(c)))
elif a+b < c : 
    print (str(a) + (" + ") + str(b) + (" es menor que ") +  (str(c)))
elif a+b == c :
    print (str(a) + (" + ") + str(b) + (" es igual que ") +  (str(c)))
```

Si corremos el código en el terminal podemos ver el siguiente resultado:

[![Captura-de-pantalla-2023-03-14-180913.png](https://i.postimg.cc/GpM7sqmN/Captura-de-pantalla-2023-03-14-180913.png)](https://postimg.cc/FfLgMbcg)

Y para tener un poco más de claridad hemos realizado el siguiente diagrama de flujo



¡Ya pasamos la mitad!Ahora vamos por el punto 6

## Punto 6 🔤

Escriba un programa que solicite al usuario una letra y determine si es una vocal o una consonante.

Para este sexto punto se le vuelve a solicitar al usurio ingresar un dato, pero en este caso es una letra. Luego el programa se encarga de determinar si esta es una vocal o consonante. Para esto lo que realizamos es que le decimos al programa por medio de disyunciones (or) que si la letra es una vocal pues se imprimirá tal como corresponde y al igual que en puntos anterirores utilizamos los '==' para determinar la igualdad.
En este caso utilizamos las comillas sin contenido adentro para así no tener que definir la variable

``` python
a=""
a=(input(" Ingrese una letra "))
if a == "a" or a == "e" or a == "i" or a == "o" or a == "u" or a == "A" or a == "E" or a=="I" or a =="O" or a =="U" :
    print (str(a)+ (" es una vocal "))
else:
    print (str(a)+ (" es una consonante "))
```

Y cuando en el terminal corremos el archivo [puntoSeis.py](/puntoSeis.py) se ve algo así:

[![Captura-de-pantalla-2023-03-14-183126.png](https://i.postimg.cc/1zP0560d/Captura-de-pantalla-2023-03-14-183126.png)](https://postimg.cc/xXxN6X4G)

Ahora al punto más difícil

## Punto 7 🧠

Sin duda alguna este es el punto más difícil del taller por la cantidad de condicionales que se utilizan

Por este motivo decidimos crear el siguiente video:

Aún así se explicará de una manera breve en este espacio. Este punto lo podemos ver en [tallerUno.ipynb](/tallerUno.ipynb) y también podremos ver que es el más largo de todos pues lo podemos ver a continuación: 

``` python
# Punto 7 

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
num4 = float(input("Ingrese el cuarto número: "))
num5 = float(input("Ingrese el quinto número: "))

# 7.1
# Cálculo del promedio
promedio = (num1 + num2 + num3 + num4 + num5) / 5

# 7.2
# Cálculo de la mediana
if num1 <= num2 <= num3 <= num4 <= num5:
    mediana = num3
elif num5 <= num4 <= num3 <= num2 <= num1:
    mediana = num3
elif num1 <= num3 <= num2 <= num4 <= num5:
    mediana = num3
elif num5 <= num4 <= num2 <= num3 <= num1:
    mediana = num3
elif num1 <= num3 <= num4 <= num2 <= num5:
    mediana = num3
elif num5 <= num2 <= num4 <= num3 <= num1:
    mediana = num3
elif num2 <= num1 <= num3 <= num4 <= num5:
    mediana = num3
elif num5 <= num4 <= num3 <= num1 <= num2:
    mediana = num3
elif num1 <= num4 <= num2 <= num3 <= num5:
    mediana = num3
elif num5 <= num3 <= num2 <= num4 <= num1:
    mediana = num3
else:
    mediana = "No se puede calcular la mediana."

print("El promedio de los números ingresados es:", promedio)
print("La mediana de los números ingresados es:", mediana)

# 7.3
# Cálculo del promedio multiplicativo
if num1 != 0 and num2 != 0 and num3 != 0 and num4 != 0 and num5 != 0:
    promedio_multiplicativo = ((num1 * num2 * num3 * num4 * num5) ** (1/5))
else:
    promedio_multiplicativo = "No se puede calcular el promedio multiplicativo."

print("El promedio multiplicativo de los números ingresados es:", promedio_multiplicativo)

# 7.4
# Ordenamiento de los números de forma ascendente
if num1 > num2:
    num1, num2 = num2, num1
if num2 > num3:
    num2, num3 = num3, num2
if num3 > num4:
    num3, num4 = num4, num3
if num4 > num5:
    num4, num5 = num5, num4
if num1 > num2:
    num1, num2 = num2, num1
if num2 > num3:
    num2, num3 = num3, num2
if num3 > num4:
    num3, num4 = num4, num3
if num1 > num2:
    num1, num2 = num2, num1
if num2 > num3:
    num2, num3 = num3, num2
if num1 > num2:
    num1, num2 = num2, num1

print("Los números ingresados en orden ascendente son:", num1, num2, num3, num4, num5)

# 7.5
# Ordenamiento de los números de forma descendente
if num1 < num2:
    num1, num2 = num2, num1
if num2 < num3:
    num2, num3 = num3, num2
if num3 < num4:
    num3, num4 = num4, num3
if num4 < num5:
    num4, num5 = num5, num4
if num1 < num2:
    num1, num2 = num2, num1
if num2 < num3:
    num2, num3 = num3, num2
if num3 < num4:
    num3, num4 = num4, num3
if num1 < num2:
    num1, num2 = num2, num1
if num2 < num3:
    num2, num3 = num3, num2
if num1 < num2:
    num1, num2 = num2, num1

print("Los números ingresados en orden descendente son:", num1, num2, num3, num4, num5)

# 7.6
# Determinar el número mayor y el número menor
if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5:
    mayor = num1
elif num2 > num3 and num2 > num4 and num2 > num5:
    mayor = num2
elif num3 > num4 and num3 > num5:
    mayor = num3
elif num4 > num5:
    mayor = num4
else:
    mayor = num5
    
if num1 < num2 and num1 < num3 and num1 < num4 and num1 < num5:
    menor = num1
elif num2 < num3 and num2 < num4 and num2 < num5:
    menor = num2
elif num3 < num4 and num3 < num5:
    menor = num3
elif num4 < num5:
    menor = num4
else:
    menor = num5

# 7.7    
# Calcular la potencia del mayor número elevado al menor número
potencia = mayor ** menor

print("La potencia del mayor número elevado al menor número es:", potencia)
  
# 7.8    
# Calcular la raíz cúbica del menor número
if menor >= 0:
    raiz_cubica = menor ** (1/3)
else:
    raiz_cubica = -((-menor) ** (1/3))

print("La raíz cúbica del menor número es:", raiz_cubica)
```

