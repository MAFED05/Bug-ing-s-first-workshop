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






