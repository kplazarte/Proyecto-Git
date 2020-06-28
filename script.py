# Sofware Libre
#Autor: Kevin Plazarte
# Fecha: 24-06-2020
def main():
    nombre= input("Ingresa tu nombre: ")
    print("Hola ", nombre, "Bienvenido a Git")
    n1=float(input("Ingrese un numero: "))
n2=float(input("Ingrese un numero: "))
op=input("Ingrese una operacion: ")

def suma(n1,n2):
    return n1+n2

def resta(n1,n2):
    return n1-n2

def multiplicacion(n1,n2):
    return n1*n2

def division(n1,n2):
    return n1/n2

if(op == '+'):
    print("El valor al Sumar es:", suma(n1,n2))

if (op == '-'):
    print( "El valor al Restar es:", resta( n1, n2 ) )

if (op == '*'):
    print( "El valor al Multiplicar es:", multiplicacion( n1, n2 ) )

if (op == '/'):
    print( "El valor al Dividir es:", division( n1, n2 ) )
if __name__== "__main__":
    main()
