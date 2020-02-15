import turtle as t

passo=100
angolo=90
print("Inserire una stringa di comandi('f','b','r','l')")
lettere=input()
t.begin_poly()
for lettera in lettere:
    if lettera=='f':
        t.forward(passo)
    elif lettera=='l':
        t.left(angolo)
        t.forward(passo)
    elif lettera == 'r':
        t.right(angolo)
        t.forward(passo)
    elif lettera == 'b':
        t.back(passo)
    else:
        print("Comando inesistente")
t.done()



