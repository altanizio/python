#Binomial programa
import math
import mathprob

def binomial(x,n,p):
    return mathprob.combinacao(n,x)*math.pow(p,x)*math.pow(1-p,n-x)


    
print("X~Bin(n,p)")
n=int(input("n="))
p=float(input("p="))
if p>1:
    print("erro")
    exit()
aux=0
for i in range(0,n+1):
     print("x"+str(i), "=", binomial(i,n,p))
     aux =  binomial(i,n,p) + aux
print("soma =", aux)
print("E(x) =", n*p)
print("Var(x) =", n*p*(1-p))
print("D.P.(x) =",math.sqrt(n*p*(1-p)))
soma=0

a=int(input("a="))
b=int(input("b="))

for i in range(a,b+1):
    soma=soma+binomial(i,n,p)
print("soma(a,b) =", soma)
input("[Enter]Exit")
exit()
