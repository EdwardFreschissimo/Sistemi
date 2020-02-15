import numpy as np
n = 234324244423366575435
isPrime = True

for p in range(2, ((n//2)+1)):
    if(n % p == 0):
        print(f"trovato fattore: {p}")
        isPrime=False

if isPrime:
    print(f"Il numero è primo")        
    