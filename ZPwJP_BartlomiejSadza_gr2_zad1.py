import math
import random


def zadanie1():
    userInput = input("Wprowadź pierwszą liczbę: ")
    userInput2 = input("Wprowadź drugą liczbę: ")

    num1 = float(userInput)
    num2 = float(userInput2)

    result = math.sqrt(num1 + num2)

    return result


def zadanie2():
    number = random.randint(1, 5)
    guess = 0
    while guess != number:
        guess = int(input("Zgadnij numer od 1 do 5: "))

        if guess == number:
            print("Gratulacje! Zgadłeś numer!")
        elif guess < number:
            print("Numer jest większy")
        else:
            print("Numer jest mniejszy")


def zadanie3():
    nums = [random.randint(2, 8) for _ in range(10)]
    print("Originalna lista:", nums)

    # b
    print("Lista elementów z indeksami:")
    for index, value in enumerate(nums):
        print(f"Index {index}: {value}")

    # c
    c = [num for num in nums if num % 2 == 0]
    print("Lista po usunięciu nieparzystych wartości:", c)

    # d
    d = [num for num in nums if num not in [2, 3]]
    print("Lista po usunięciu wartości 2 i 3:", d)

    # e
    i = 0
    while i < len(nums):
        if nums[i] % 3 == 0:
            nums.insert(i + 1, 15)
            i += 1
        i += 1

    print(
        "Finalna lista po wstawieniu 15'stki po kazdej wartosci podzielnej przez 3",
        nums,
    )


def zadanie4():
    tnums = tuple(random.randint(2, 15) for _ in range(10))
    print("Originalna lista:", tnums)

    # a
    for index, value in enumerate(tnums):
        print(f"Index {index}: {value}")

    # b
    harmoniczna = len(tnums) / sum(1 / num for num in tnums)
    geometryczna = math.exp(sum(math.log(num) for num in tnums) / len(tnums))
    arytmetyczna = sum(tnums) / len(tnums)

    print(f"Średnia harmoniczna: {round(harmoniczna, 2)}")
    print(f"Średnia geometryczna: {round(geometryczna, 2)}")
    print(f"Średnia arytmetyczna: {round(arytmetyczna, 2)}")

    # c
    counter = 0
    for num in tnums:
        if num == 5 or num == 3:
            counter += 1
    print(f"Ilość 3 i 5 w tupli: {counter}")


def zadanie5():
    sub = [
        "Matematyka",
        "Fizyka",
        "Chemia",
        "Biologia",
        "Historia",
        "Geografia",
        "Informatyka",
        "Język Polski",
        "Język Angielski",
        "Wychowanie Fizyczne",
    ]
    names = [
        "Jan",
        "Anna",
        "Piotr",
        "Katarzyna",
        "Michał",
        "Karolina",
        "Tomasz",
        "Agnieszka",
        "Jakub",
        "Natalia",
    ]
    ids = [22223, 22224, 22225, 22226, 22227, 22228, 22229, 22230, 22231, 22232]

    group = list(
        zip(
            ids,
            names,
            [
                random.sample(sub, random.randint(1, len(sub)))
                for _ in range(int(len(ids) / 2))
            ],
        )
    )
    print("Grupa:", group)


def zadanie6():
    # a
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    lista = []
    podlista = []

    for letter in alphabet:
        podlista.append(letter.upper())
        if len(podlista) == 5:
            lista.append(podlista)
            podlista = []

    # print("Lista:", lista)

    # b
    lista2 = []
    podlista2 = []

    for letter in alphabet:
        podlista2.append(letter.upper())
        if len(podlista2) == random.randint(3, 7):
            lista2.append(podlista2)
            podlista2 = []

    # print("Lista2:", lista2)

    # c
    lista3 = [
        (x, y) for x in range(1, 11) if x % 2 == 0 for y in range(1, 11) if y % 2 != 0
    ]
    print(lista3)


def zadanie7():
    student_grades = [("Alice", 5), ("Bob", 4), ("Eve", 3), ("AAA", "BBB")]
    for student, grade in student_grades:
        if type(grade) == int:
            print(f"{student}: {grade}")


def zadanie8():
    smak = ["smietankowe", "pistacjowe", "truskawkowe", "jagodowe", "cytrynowe"]
    rozmiar = ["duże", "małe"]
    dodatek = [
        "polewa czekoladowa",
        "polewa karmelowa",
        "posypka czekoladowa",
        "posypka kolorowa",
    ]

    lista = []
    for i in range(100):
        random_smak = random.choice(smak)
        random_rozmiar = random.choice(rozmiar)
        random_dodatek = random.choice(dodatek)
        if (random_smak, random_rozmiar, random_dodatek) not in lista:
            lista.append((random_smak, random_rozmiar, random_dodatek))
    return lista


# print(zadanie8())
