##########################
# Ism: Baxtiyorjon
# Familya: Mirzajonov
##########################

import math

# 1-savol
def kvadrat_perim():
    a = int(input("a = "))
    return 4 * a

#print(kvadrat_perim())

# 2-savol
def kvadrat_yuzasi():
    a = int(input("a = "))
    return a ** 2

# print(kvadrat_yuzasi())

# 3-savol
def tortburchak1():
    a = int(input("a = "))
    b = int(input("b = "))
    
    return (
        "To'rtburchak perimetiri: ", 2 * (a + b), 
        "To'rtburchak Yuzasi: ", a * b
    )

# print(tortburchak1())

# 4-savol
def aylana_uzunligi():
    d = int(input("d: "))
    return math.pi * d

# print(aylana_uzunligi())

# 5-savol
def kub():
    a = int(input("a = "))
    return (
        "Kubning hajmi: ", a ** 3, 
        "kubning to'la sirti: ", 6 * (a ** 2)
    )

# print(kub())

# 6-savol
def parallelopiped():
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))

    return (
        "Parallelopipedning hajmi: ", a * b * c, 
        "Parallelopipedning sirti: ", 2 * (a*b + b*c + a*c)
    )

# print(parallelopiped())

# 7-savol
def doira():
    r = int(input("r = "))

    return (
        "Doiraning uzunligi: ", 2 * math.pi * r,
        "Doiraning yuzasi: ", math.pi * (r ** 2)
    )

# print(doira())

# 8-savol
def orta_arfimetik():
    a = int(input("a = "))
    b = int(input("b = "))

    return "O'rta arfimetigi: ", (a + b) / 2

# print(orta_arfimetik())

# 9-savol
def orta_geometrik():
    a = int(input("a = "))
    b = int(input("b = "))

    return "O'rta geometrigi: ", (a * b) ** 0.5

# print(orta_geometrik())

# 10-savol
def arfimetika1():
    a = int(input("a = "))
    b = int(input("b = "))

    return (
        "Yig'indisi: ", a + b,
        "Ko'paytmasi: ", a * b,
        "a^2: ", a ** 2,
        "b^2: ", b ** 2
    )

# print(arfimetika1())

# 11-savol
def arfimetika2():
    a = int(input("a = "))
    b = int(input("b = "))

    return (
        "Yig'indisi: ", a + b,
        "Ko'paytmasi: ", a * b,
        "|a|: ", abs(a),
        "|b|: ", abs(b)
    )

# print(arfimetika2())

# 12-savol
def uchburchak1():
    a = int(input("a = "))
    b = int(input("b = "))

    c = ( (a ** 2) + (b ** 2)) ** 0.5
    p = a + b + c

    return (
        "Gipatenuzasi: ", c,
        "Perimetri: ", p
    )

# print(uchburchak1())

# 13-savol
def aylana1():
    r1 = int(input("r1 = "))
    r2 = int(input("r2 = "))

    return (
        "Birinchi aylana yuzasi: ", math.pi * (r1 ** 2),
        "Ikkinchi aylana yuzasi: ", math.pi * (r2 ** 2),
        "Aylanalar yuzalari ayrimasi: ", math.pi * ( (r1 - r2) ** 2)
    )

# print(aylana1())

# 14-savol
def aylana2():
    L = int(input("Aylana uzunligi = "))
    r = L / (2 * math.pi)
    s = math.pi * ( r ** 2)

    return (
        "Aylana radiusi: ", r,
        "Aylana yuzasi: ", s
    )

# print(aylana2())

# 15-savol
def aylana3():
    s = int(input("Aylana yuzasi = "))

    r = (s / math.pi) ** 0.5
    d = 2 * r

    return (
        "Aylana diametri: ", d,
        "Aylana Radiusi: ", r
    )

# print(aylana3())

# 16-savol
def son_oqi1():
    x1 = int(input("x1 = "))
    x2 = int(input("x2 = "))

    return abs(x1 - x2)

# print(son_oqi1())

# 17-savol
def kesmalar1():
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))

    L = sorted([a, b, c])
    a, b, c = L[0], L[1], L[2]

    ac = c - a
    bc = c - b

    return (
        "AC: ", ac,
        "BC: ", bc,
        "Yig'indisi: ", ac + bc
    )

# print(kesmalar1())

# 18-savol
def kesmalar2():
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))

    L = sorted([a, b, c])
    a, c, b = L[0], L[1], L[2]

    ac = c - a
    bc = b - c

    return ac * bc

# print(kesmalar2())

# 19-savol
def tortburchak2():
    x1 = int(input("Birinchi nuqta x koordinati: "))
    y1 = int(input("Birinchi nuqta y koordinatasi: "))

    x2 = int(input("Ikkinchi nuqta x koordinati: "))
    y2 = int(input("Ikkinchi nuqta y koordinatasi: "))

    x = abs(x1 - x2)
    y = abs(y1 - y2)

    return (
        "To'rtburchak yuzasi: ", x * y,
        "To'rtburchak perimetiri: ", 2 * (x + y)
    )

# print(tortburchak2())

# 20-savol
def nuqtalar_masofasi():
    x1 = int(input("Birinchi nuqta x koordinati: "))
    y1 = int(input("Birinchi nuqta y koordinatasi: "))

    x2 = int(input("Ikkinchi nuqta x koordinati: "))
    y2 = int(input("Ikkinchi nuqta y koordinatasi: "))

    return "Nuqtalar orasidagi masofa: ", ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# print(nuqtalar_masofasi())

# 21-savol
def uchburchak2():
    x1 = int(input("Birinchi nuqta x koordinati: "))
    y1 = int(input("Birinchi nuqta y koordinatasi: "))

    x2 = int(input("Ikkinchi nuqta x koordinati: "))
    y2 = int(input("Ikkinchi nuqta y koordinatasi: "))

    x3 = int(input("Uchinchi nuqta x koordinati: "))
    y3 = int(input("Uchinchi nuqta y koordinatasi: "))

    a = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    b = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5
    c = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5

    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5

    return f"Uchburchakning yuzasi: {s}, Uchburchakning perimetiri: {p}"
    

# print(uchburchak2())

# 22-savol
def almashtirish1():
    a = int(input("a = "))
    b = int(input("b = "))

    a = a + b
    b = a - b
    a = a - b

    return f"a = {a}, b = {b}"

# print(almashtirish1())

# 23-savol
def almashtirish2():
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))

    a = a + b + c

    b = a - b - c
    c = a - b - c
    a = a - b - c

    return f"a = {a}, b = {b}, c = {c}"

# print(almashtirish2())

# 24-savol
def almashtirish3():
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))

    b = a + b + c

    a = b - a - c 
    c = b - a - c
    b = b - a - c

    return f"a = {a}, b = {b}, c = {c}"
        
# print(almashtirish3())

# 25-savol
def funksiya1():
    x = int(input("x = "))

    return 3 * (x ** 6) - 6 * (x ** 2) - 7

# print(funksiya1())

# 26-savol
def funksiya2():
    x = int(input("x = "))

    return 4 * ((x - 3) ** 6) - 7 * ((x -3) ** 3) + 2

# print(funksiya2())

# 27-savol
def daraja1():
    a = int(input("a = "))

    a2 = a ** 2
    a4 = a ** 4
    a8 = a ** 8

    return f"a^2 = {a2}, a^4 = {a4}, a^8 = {a8}"

# print(daraja1())

# 28-savol
def daraja2():
    a = int(input("a = "))

    a2 = a ** 2
    a3 = a ** 3
    a5 = a ** 5
    a10 = a ** 10
    a15 = a ** 15

    return f"a^2 = {a2}, a^3 = {a3}, a^5 = {a5}, a^10 = {a10}, a^15 = {a15}"

# print(daraja2())

# 29-savol
def alfa1():
    a = float(input("Alfa kiritilsin: "))
    return a * math.pi / 180

# print(alfa1())

# 30-savol
def alfa2():
    a = float(input("Radian kiritilsin: "))
    return a * 180 / math.pi

# print(alfa2())

# 31-savol
def temp1():
    t = float(input("Temperatura farangeytda kiritilsin: "))
    return (t - 32) * 5 / 9

# print(temp1())

# 32-savol
def temp2():
    t = float(input("Temperatura selsiyda kiritilsin: "))
    return t * 9 / 5 + 32

# print(temp2())

# 33-savol
def konfet1():
    n = float(input("Konfetning kilosi narxi qancha: "))
    x = float(input("Nechchi kilo konfet olmoqchisiz: "))

    return f"1kg Konfetning narxi {n} so'm, va {x}kg kanfet {n * x}so'm turadi."

# print(konfet1())

# 34-savol
def konfet2():
    x = float(input("Shokoladning kilosi kiritilsin: "))
    ns = float(input(f"{x}kg shokoladning narxi kiritilsin: "))

    y = float(input("Konfetning kilosi kiritilsin: "))
    nk = float(input(f"{y}kg konfetning narxi kiritilsin: "))

    return f"1kg shokolad 1kg konfetdan {ns / x - nk / y} so'm qimmat turadi."

# print(konfet2())

# 35-savol


# 36-savol
def avto1():
    v1 = float(input("Birinchi avtomobilning tezligini kiriting (km/soat): "))
    v2 = float(input("Ikkinchi avtomobilning tezligini kiriting (km/soat): "))
    t = float(input("Oradan o'tgan vaqt (soatda): "))

    return f"{t} minutdan keyingi masofa = {v1 * t + v2 * t}."

# print(avto1())

# 37-savol
def avto2():
    v1 = float(input("Birinchi avtomobilning tezligini kiriting (km/soat): "))
    v2 = float(input("Ikkinchi avtomobilning tezligini kiriting (km/soat): "))
    s = float(input("Avtomobillar orasidagi masofani kiriting (km): "))
    t = float(input("Oradan o'tgan vaqt (soat): "))

    masofa = v1 * t + v2 * t 
    
    return f"Mashinalar orasidagi masofa {abs(s - masofa)}km."

# print(avto2())



   
