def recur_fibo(n):
   """Funcion Recursiva"""
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))


# Numero dado por usuario
nterms = int(input("How many terms? "))

# Mirar si el numero es valido
if nterms <= 0:
   print("Por favor ingrese un enero positivo")
else:
   print("Serie Fibonacci:")
   for i in range(nterms):
       print(recur_fibo(i))
