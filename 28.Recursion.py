# -*- coding: utf-8 -*-
"""Recursion.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cUbQdKYpmBiruYyDhlPnO__94BaSFHeN

#Iterative Recursion
"""

#Creating Factorical Function
def iterative_factorial(n):
  '''
  :param n: Integer
  :return: n*n-1 * n-2 * n-3...n-1
  '''
  fac=1
  for i in range(n):
    fac = fac*(i+1)
  return fac

number = int(input('Enter Number:'))
iterative_factorial(number)

#5*4*3*2*1

"""# Recursive Recursion"""

def factorial_recursion(n):
  if n==1:
    return 1
  else:
    return n*factorial_recursion(n-1)
  
number = int(input('Enter Number:'))
factorial_recursion(number)

factorial = 1
n = 10
for i in range(n):
  factorial = factorial*(i+1)
  print(factorial)