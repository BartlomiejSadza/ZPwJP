import random


# -------------------------------------------------------------
def zadanie1():
    r = list(range(10, 20))

    for n in r:
        sum = int(str(n)[0]) + int(str(n)[1])
        print("suma dla " + str(n) + " wynosi: " + str(sum))


# -------------------------------------------------------------
def zadanie2():
    r = list(range(4, 10))
    l = []

    while len(l) < 3:
        t = []
        while len(t) < 3:
            n = random.choice(r)
            t.append(n)
        l.append(t)
        t = []

    print(l)


# -------------------------------------------------------------
def zadanie3():
    list = [[1, 2, 3], [4, 5], [6, 7, 8]]
    new_list = []
    for l in list:
        for n in l:
            new_list.append(n)
    print(new_list)


# -------------------------------------------------------------
def zadanie4():
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    new_m = []
    small_m = []
    for i in m:
        for j in i:
            while len(new_m) < 3:
                if len(small_m) == 3:
                    new_m.append(small_m)
                    small_m = []
                else:
                    if j < 5:
                        small_m.append(random.randint(5, 9))
                    else:
                        small_m.append(j)
    print(new_m)


# -------------------------------------------------------------
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]


def zadanie5(A, B):
    result = [
        [sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)] for i in range(3)
    ]

    print(result)


# zadanie5(A, B)

# -------------------------------------------------------------
words_dict = {"apple": 5, "banana": 3, "cherry": 7, "date": 2}


def zadanie6(words_dict):
    new_dict = {}

    for word, count in words_dict.items():
        if len(word) >= 5:
            new_dict[word] = count * 2

    print(new_dict)


# -------------------------------------------------------------
def zadanie7():
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    first = []
    second = []
    third = []

    for i in m:
        for j in range(3):
            if j == 0:
                first.append(i[j])
            elif j == 1:
                second.append(i[j])
            else:
                third.append(i[j])

    new_m = [first, second, third]
    print(new_m)


# -------------------------------------------------------------
def zadanie9():
    m = [n for n in range(2, 101) if all(n % j != 0 for j in range(2, n))]
    print(m)


# -------------------------------------------------------------
def zadanie10():
    cezar = "CEZAR"
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encoded_cezar = "".join(
        [alphabet[(alphabet.index(c) + 3) % len(alphabet)] for c in cezar]
    )
    print(encoded_cezar)


# -------------------------------------------------------------


def zadanie11():
    fib = [0, 1]
    while fib[-1] < 80:
        fib.append(fib[-1] + fib[-2])

    res = [f for f in fib if f % 2 == 0]
    print(res)


# -------------------------------------------------------------
tekst = "To jest pierwsze zdanie. To jest drugie zdanie. A to jest trzecie zdanie. Tak, to jest czwarte zdanie."
zdania = tekst.split(". ")


def zadanie12(zdania):
    new_list = []
    for zdanie in zdania:
        for slowo in zdanie.split(" "):
            if len(slowo) > 3:
                new_list.append(slowo.upper())
    print(new_list)


# zadanie12(zdania)


# -------------------------------------------------------------
def zadanie13():
    kwadraty = []
    for i in range(1, 6):
        kw = []
        for j in range(i, i + 3):
            kw.append(j**2)
        kwadraty.append(kw)
    print(kwadraty)


# zadanie13()


# -------------------------------------------------------------
n = 10


def zadanie14(n):
    slownik = {i: i**2 for i in range(1, n + 1)}
    print(slownik)


# zadanie14(n)


# -------------------------------------------------------------
n = 10


def zadanie15(n):
    dict = {}
    for i in range(1, n + 1):
        if i % 2 == 0:
            dict[i] = i**2
    return dict


# zadanie15(n)


# -------------------------------------------------------------
def zadanie16(words_dict):
    new_dict = {}
    for k, v in words_dict.items():
        new_dict[v] = k
    print(new_dict)


# zadanie16(words_dict)


# -------------------------------------------------------------
def zadanie17():
    ascii_dict = {chr(i): i for i in range(97, 123)}
    print(ascii_dict)


# zadanie17()


# -------------------------------------------------------------
n = 15


def zadanie18(n):
    nested_dict = {i: {"kwadrat": i**2, "szescian": i**3} for i in range(1, n + 1)}
    print(nested_dict)


# zadanie18(n)


# -------------------------------------------------------------
def zadanie19(n):
    dict = {i: i**2 for i in range(1, n) if i ** 2 > 10}
    print(dict)


zadanie19(n)
