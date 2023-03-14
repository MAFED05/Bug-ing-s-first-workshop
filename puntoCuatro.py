a: float
b: float
x: float
a = float (input("Ingrese un número real"))
b = float (input("Ingrese un número real"))
if a % b == 0 :
    print (str(a) + " es múltiplo de " + str(b))
elif a % b != 0 :
    print (str(a) + " no es múltiplo de " + str(b))
