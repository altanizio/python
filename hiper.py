# coding=UTF-8
#Hipergeométrica
import math
import mathprob
################################################################################
print("-----------------------------------\nBem vindo à interface Hipergeométrica\nEsse programa calcula todas as probabilidades de X\nLicenciado e criado por AJu\n-----------------------------------")
################################################################################


def hiper(x,N,r,nn):
    return mathprob.combinacao(r,x)*mathprob.combinacao(N-r,nn-x)/mathprob.combinacao(N,nn)






print("Insira o tamanho da população")
N = int(input ("N = "))

print("Insira quantos elementos tem uma tal cararcterística")
r = int(input ("r = "))

print("Insira o tamanho do grupo de elementos selecionados")
nn = int(input ("n = "))

if nn>N or N<0 or r<0 or nn<0 or r>N or r<nn:
    print("Erro! Insira valores validos!")
    exit()

aux01=0
aux02=0

for i in range(0,nn+1):
    print ("x"+str(i), "=", hiper(i,N,r,nn))
    aux01+=hiper(i,N,r,nn)
print("Soma de todos os X é ",aux01,"\nSoma em um intervalo:")
print("Bote o valor de a e b afim de representar: P(a=<X=<b)")

a = int(input ("a = "))
b = int(input ("b = "))

for i in range(a,b+1):
    aux02+=hiper(i,N,r,nn)
print("P(a=<X=<b) = ", aux02)
input ("[Enter]Exit")
exit()




    
