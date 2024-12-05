import random
lista= []
def veletlen():
    hossz = 20

    

    for i in range(hossz):
        lista.append(random.randint(1,50))
    return lista

def kiir():
    for i in veletlen():
        print(i, end=" ")

def osszeAd():
    sum=0
    for i in veletlen():
        sum=sum+i
    return sum

def legnagyobbElem():
    max = veletlen()[0]

    for i in veletlen():
        if i > max:
            max= i
    return max


veletlen()
kiir()
print()
print (f"A lista elemeinek az összege :  {osszeAd()}")
print(f"A lista elemeinek legnagyobb értéke :  {legnagyobbElem()}")

