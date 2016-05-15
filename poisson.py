
#Poisson
import math
import mathprob
################################################################################
print("-----------------------------------\nBem vindo à interface Poison\nEsse programa calcula todas as probabilidades de X\nLicenciado e criado por AJu\n-----------------------------------")
################################################################################


def poisson(x,y):
    return math.exp(-y)*math.pow(y,x)/mathprob.fatorial(x)



print("Insira a taxa")
y = float(input ("y = "))

print("Insira até que elemento quer analizar")
f = int(input ("f = "))

aux01=0
aux02=0

for i in range(0,f+1):
    print ("x"+str(i), "=", poisson(i,y))
    aux01+=poisson(i,y)
print("Soma de todos os X é ",aux01,"\nSoma em um intervalo:")
print("Bote o valor de a e b afim de representar: P(a=<X=<b)")

a = int(input ("a = "))
b = int(input ("b = "))

for i in range(a,b+1):
    aux02+=poisson(i,y)
print("P(a=<X=<b) = ", aux02)
input ("[Enter]Exit")
exit()



