'''
El usuario quiere saber cual es el área de un círculo teniendo el radio
--------------------------------

Algoritmo:
1. Solicitar al usuario que ingrese el radio del círculo.
2. Calcular el área del círculo utilizando la fórmula area = π * radio^2
3. Mostrar al usuario el área calculada
--------------------------------
'''

import math
print(' ')
print('Programa para calcular el area de un circulo!!')
print('---------------------------------------------')
print(' ')
radio = float(input('Ingrese el radio del circulo: '))
print(f'El area del circulo es {math.pi * (radio**2)}')