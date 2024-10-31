import itertools
import os
from collections import defaultdict

lst = ["a", "b", "c", "d", "e", "f"]


def zadanie1(lst):
    return list(itertools.accumulate(lst, lambda x, y: x + y))


# print(zadanie1(lst))


def zadanie2(lst):
    return list(itertools.accumulate(lst, max))


lst = [5, 3, 6, 2, 1, 9, 1]

# print(zadanie2(lst))


def zadanie3(lst):
    n = len(lst)
    for i in range(n):
        yield 1 << i


# print(list(zadanie3(lst)))


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def kwadrat(generator):
    for num in generator:
        yield num**2


def zadanie4(n):
    generator = fibonacci(n)
    return list(kwadrat(generator))


# print(zadanie4(10))


def zadanie5(generator):
    new_list = []
    for num in generator:
        if num % 2 == 0:
            new_list.append(num)
    return new_list


# print(zadanie5(zadanie4(10)))


def zadanie6(n):
    def liczby_pierwsze():
        D = {}
        q = 2

        while True:
            if q not in D:
                yield q
                D[q * q] = [q]  ## oznacza pierwszą wielokrotność
            else:
                for p in D[q]:
                    D.setdefault(p + q, []).append(p)
                del D[q]
            q += 1

    def generator(liczby_pierwsze, n):
        do_zwrocenia = [next(liczby_pierwsze) for _ in range(n)]
        return do_zwrocenia

    return generator(liczby_pierwsze(), n)


# print(zadanie6(10))


def zadanie7(n):
    count = 0
    x = 1
    while count < n:
        for y in range(x, 2 * x):
            z = (x**2 + y**2) ** 0.5
            if z.is_integer():
                yield (x, y, int(z))
                count += 1
                if count >= n:
                    break
        x += 1


# print(list(zadanie7(10)))


def zadanie8(katalog):
    def fulfilled(katalog):
        for root, _, files in os.walk(katalog):
            for file in files:
                yield os.path.join(root, file)

    return list(fulfilled(katalog))


# print(zadanie8('/Users/bartlomiejsadza/Documents/Projekty/ProjektyStudia'))


def palindrom(word):
    return word == word[::-1]


def zadanie9(slowo):
    words = slowo.split()
    return map(palindrom, words)


# print(list(zadanie9('kamilslimak')))

words = ["level", "world", "radar", "python", "madam", "java", "civic"]


def zadanie10(lista):
    filtered = list(filter(palindrom, lista))
    return list(map(lambda word: word.upper() if word in filtered else word, lista))


# print(zadanie10(words))


def zadanie11(n):
    mapped = list(map(lambda x: x if isinstance(x, (int, float)) else "", n))
    filtered = list(filter(lambda x: x != "", mapped))

    return len(filtered)


# print(zadanie11([1, 2, 3, 4, 5, 6, 7, 8, 9, 'tak', 10, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5]))


def zadanie12(n):
    def process(sublista):
        return list(filter(lambda x: x % 2 == 0, sublista))

    return [process(sublista) for sublista in n]


zagniezdzone = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# print(zadanie12(zagniezdzone))


def zadanie13(lista):
    result = defaultdict(int)
    list(map(lambda x: result.__setitem__(x[0], result[x[0]] + x[1]), lista))
    return dict(result)


klasy = [
    ("Klasa A", 11),
    ("Klasa A", 12),
    ("Klasa A", 5),
    ("Klasa B", 3),
    ("Klasa B", 15),
    ("Klasa B", 10),
    ("Klasa B", 2),
]
# print(zadanie13(klasy))


def zadanie14(lista1, lista2):
    scalone = list(zip(lista1, lista2))
    for i, v in enumerate(scalone):
        return {i: v for i, v in scalone}


numbers = [1, 2, 3, 4, 5, 6]
letters = ["a", "b", "c", "d", "e", "f"]

# print(zadanie14(numbers, letters))
