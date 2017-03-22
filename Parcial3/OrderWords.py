#!/usr/bin/env python3


def comp(thiss, other):
    """Returns: thiss < other"""
    smallWordSize = min(len(thiss), len(other))
    thiss = list(thiss)
    other = list(other)
    for i in range(smallWordSize):
        paso1 = False
        paso2 = False
        this1 = 0.0
        other1 = 0.0
        if ord(thiss[i]) == 241 or ord(thiss[i]) == 209:
            this1 = 110.5
            paso1 = True
        if ord(other[i]) == 241 or ord(other[i]) == 209:
            other1 = 110.5
            paso2 = True
        if not paso1:
            this1 = float(ord(thiss[i]))
        if not paso2:
            other1 = float(ord(other[i]))

        if this1 > other1:
            return False
        if other1 > this1:
            return True
    if len(thiss) > smallWordSize:
        return False
    return True


def partition(lista, start, end):
    pivot = lista[end]
    bottom = start - 1
    top = end

    done = 0
    while not done:

        while not done:
            bottom = bottom + 1

            if bottom == top:
                done = 1
                break

            if comp(pivot, lista[bottom]):
                lista[top] = lista[bottom]
                break
        while not done:
            top = top - 1

            if top == bottom:
                done = 1
                break

            if comp(lista[top], pivot):
                lista[bottom] = lista[top]
                break
    lista[top] = pivot
    return top


def quicksort(lista, start, end):
    if start < end:
        splited = partition(lista, start, end)
        quicksort(lista, start, splited - 1)
        quicksort(lista, splited + 1, end)
    else:
        return


if __name__ == "__main__":
    print("Ingrese una listaa de palabras a ordenar.")
    print("Una linea vacia indicara el fin de la listaa")
    listaa = []
    while True:
        word = str(input()).replace(" ", "").lower()
        if word == "":
            break
        listaa.append(word)
    start = 0
    end = len(listaa) - 1
    quicksort(listaa, start, end)
    print(str.join('\n', listaa))
