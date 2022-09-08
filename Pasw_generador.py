# Generador de contraseñas
from random import randrange
from secrets import choice

def pasw_gen() :
    numero = input("Ingrese la longitud de la contraseña: ")
    if numero.isdecimal() :
        a, b, c, d = [], [], [], []
        l1, l2, l3, l4 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz", "0123456789", ",.<>/?;:'|]}[{-_=+~!@#$%^&*()" 
        for i in range(int(numero)) :
            a.append(l1[randrange(len(l1))]), b.append(l2[randrange(len(l2))]), c.append(l3[randrange(len(l3))]), d.append(l4[randrange(len(l4))])
        a1, b1, c1, d1 = [], [], [], []
        for i in range(int(int(numero) / 2)) :
            a1.append(choice(a)), b1.append(choice(b)), c1.append(choice(c)), d1.append(choice(d))
        pasw = ""
        l = [a1, b1, c1, d1]
        while len(pasw) < int(numero) :
            c = randrange(4)
            pasw += str(l[c][randrange(len(l[c]))])
        return(pasw)
    else :
        return("Valor invalido.\n")

print(pasw_gen())