#Funcoes basicas fatorial
import math
def fatorial(n):
    if n<=1:
       return 1
    else :
       return n * fatorial(n-1)

def combinacao(n,s):
     return fatorial(n)/(fatorial(s)*fatorial(n-s))
