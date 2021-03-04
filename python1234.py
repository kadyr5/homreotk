# Написать функцию которая принимает числа, выводит сумму чисел. Функцию надо вызвать.
k = (3)
a = (6)
def plus():
    print(k + a)
plus()

# Написать функцию которая принимает числа, выводит разность чисел. Функцию надо вызвать.
kara = (23)
kyzyl = (43)
def alabula():
    print(kara - kyzyl)
alabula()
# Написать функцию которая принимает числа, выводит произведение чисел. Функцию надо вызвать.
ka = (2)
da = (4)
def koboit():
    print(ka * da)
koboit()
# Написать функцию которая принимает числа, выводит деление чисел. Функцию надо вызвать.
sam = (22)
kak = (3)
def bol():
    print(sam // kak)
bol()
# Написать функцию которая принимает числа, выводит деление чисел. Функцию надо вызвать.

# Написать функцию которая принемает массив, проходится по циклом по массиву и печатает объекты массива. Функцию надо вызвать.
kady = ['ak', 'kara', 'jashyl']
def boz():
    for k in kady:
        print(k)
boz()
# Написать функцию которая принемает массив, проходится по циклом по массиву и печатает объекты массива. Функцию надо вызвать.

# Напишите приммеры использования всех операций с массивами
    # len()
m = [1, 3, 3, 4]
c = len(m)
print(c)
    # append()
m = [1, 3, 3, 4]
m.append('ok')
print(m)
    # clear()
okei = ['hello', 'my', 'naem', 'is', 'kadyrbek']
okei.clear()
print(okei)
    # count()
horosho = ['hello', 'my', 'naem', 'is', 'kadyrbek']
horosho.count('naem')
print('naem')
    # copy()
zebra = [2, 3, 4, 'joni', 5]

zebra.copy()
print(zebra)
    # extend()
kon = [1, 2, 3, 4, 5, 6, 7]
kon.extend(kon)
print(kon)

    # index()
tekego = ['hello', 'my', 'naem', 'is', 'kadyrbek']
chego = tekego.index('naem')
print(chego)

    # remove('Meder')
attar = ['kak', 'tak', 'emnege', 'meder']
attar.remove('emnege')
print(attar)
    # reverse()
kd = [23, 43, 53, 54]
kd.reverse()
print(kd)

    # pop()
kg = [445, 65346, 6575, 466]
kg.pop(3)
print(kg)

# Оберните все операции в функции, которые принимают масссив и выполняют над нимм операцию. Функцию надо вызвать.
    # len()
famly = ['semya', 'ya', 'ty', 'my']
def joni():
    r = len(famly)
    print(r)
joni()
    # append(
ff = [ 2, 4, 4, 5, 6]
def damir():
    ff.append(87)
    print(ff)
damir()

    # clear()
kk = [23, 43, 55, 66]
def gg():
    kk.clear()
    print(kk)
gg()
    # count()
ll = [1, 2, 2, 2, 2, 3, 3]
def jj():
    p = ll.count(2)
    print(p)
jj()
    # copy()
ss = [1, 2, 2, 2, 2, 3, 3]
def dd():
    ss.copy()
    print(ss)
dd()
    # extend()
ee = [5, 6, 7, 8, 9, 9]
def hh():
    ee.extend(ee)
    print(ee)
hh()
    # index()
oo = [5, 6, 7, 8, 9, 9]
def yy():
    w = oo.index(6)
    print(w)
yy()

    # remove()
qq = [5, 6, 7, 8, 9, 9]
def c():
    qq.remove(6)
    print(qq)
c()

    # reverse()
nn = [77, 'll', 66, 55, 33]
def vv():
    nn.reverse()
    print(nn)
vv()

    # pop()
sss = [233, 44, 55, 6, 7, 7]
def aa():
    sss.pop(0)
    print(sss)
aa()