#http://www.programiz.com/python-programming/examples/fibonacci-recursion
def recur_fibo(n):
   """Funcion Recursiva"""
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))


# Se toma el valor ingresado porel usuario
nterms = int(input("Ingrese el numero al que se le calculara la serie? "))

# Se mira si el numero dado es valido
#Prueba de comentario
if nterms <= 0:
   print("Por favor ingresar un entero positivo")
else:
   print("Serie Fibonacci:")
   for i in range(nterms):
       print(recur_fibo(i))
