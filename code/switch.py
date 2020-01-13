# -*- coding: utf-8 -*-

def sumar(a, b):
    return a + b
 
def restar(a, b):
    return a - b
 
def multiplicar(a, b):
    return a * b;
 
num1 = input("Num1: ")
num2 = input("Num2: ")
 
print("Opciones\n1.- Sumar\n2.- Restar\n3.- Multiplicar")
 
operaciones = { '1': sumar, '2': restar, '3': multiplicar}
 
seleccion = int(input('Escoge una: '))

try:
    resultado = operaciones[seleccion](int(num1), int(num2))
    print (resultado)
except:
    print("Esa no vale")
