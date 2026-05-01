import random
try:
    with open('#file_name#', 'r') as file:
        lista = file.readlines()
except FileNotFoundError:
    print('nie ma tego pliku')
znaki_spec = ['!','@','#','$','%',"^",'&','*','-','_','=','+','{','}','[',']']
hasla = []
imiona = []
nazwiska = []
for i in range(len(lista)):
    ini = lista[i]
    imie, nazwisko = ini.split(' ')
    nazwisko = nazwisko[:-1]
    imiona.append(imie)
    nazwiska.append(nazwisko)
for i in range(len(nazwiska)):
    dlugosc = len(nazwiska[i]) + len(imiona[i]*2)*random.randrange(2,10)
    h = random.choice(znaki_spec) + random.choice(znaki_spec) + imiona[i][-3:][::-1] + nazwiska[i][0] + nazwiska[i][-1] + random.choice(znaki_spec) + str(dlugosc)
    hasla.append(h)
for i in range(len(hasla)):
    nazwiskoo = nazwiska[i]
    imieee = imiona[i]
    dlugi = len(imieee) + len(nazwiskoo)
    while True:
        if dlugi < 30:
            nazwiskoo += ' '
            dlugi = len(imieee) + len(nazwiskoo)
        else:
            break
    print(imieee,nazwiskoo,hasla[i])
