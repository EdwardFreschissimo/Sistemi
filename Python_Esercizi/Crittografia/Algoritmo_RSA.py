import math

def mcd(a,b):
    while b:
        a,b = b,a%b
    return a

def mcm(a,b):
    return a // mcd(a,b)*b

def Primo(n):
    for p in range(2,int(np.sqrt(n))+1):
        if (n%p==0):
            return False
    return True

def findC(m):
    c=2
    while c<m:
        if (mcd(c,m) != 1):
            c=c+1
        else:
            return c

def findD(c, m):
    d = 0
    while d<m:
        if ((c*d)%m)!=1:
            d = d+1
        else:
            return d

while True:
    p=int(input("Inserisci un numero primo: "))
    q=int(input("Inserisci il secondo numero primo: "))
    if(Primo(p) and Primo(q)):
        break
    else:
        print("I numeri non sono primi!!")

n=p*q
print(f"N: {n}")

m=mcm(p-1, q-1)
print(f"M: {m}")

c=findC(m)
print(f"C: {c}")

d=findD(c, m)
print(f"D: {d}")

while True:
    inp=int(input("Inserisci un numero: "))
    if (a < n):
        criptInp = pow(inp,c) % n
        print(f"{criptInp}")
        uncriptInp = pow(criptInp, d)%n
        print(f"{uncriptInp}")
        break
    else:
        print(f"Inserisci un numero maggiore di {n}")