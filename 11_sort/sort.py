"""
Bubble sort, insertion sort, and selection sort
"""


def bubble_sort(a):
    """
    Bubble sort
    :param a: a list
    :return:
    """
    if len(a) <= 1:
        return
    for i in range(len(a)):
        flag = False  # flag for making swap or not
        for j in range(len(a) - i - 1):
            if a[j] > a[j+1]:
                tmp = a[j+1]
                a[j+1] = a[j]
                a[j] = tmp
                flag = True
        if not flag:
            break


def insertion_sort(a):
    """
    Insertion sort
    :param a: a list of ints
    :return:
    """
    if len(a) <= 1:
        return
    for i in range(1, len(a)):
        value = a[i]
        j = i - 1
        while j >= 0 and a[j] > value:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = value


def selection_sort(a):
    """
    Selection sort
    :param a: a list of ints
    :return:
    """
    if len(a) <= 1:
        return
    for i in range(len(a)):
        min_value = a[i]
        min_index = i
        for j in range(i, len(a)):
            if a[j] < min_value:
                min_value = a[j]
                min_index = j
        if min_index == i:
            continue
        tmp = a[i]
        a[i] = a[min_index]
        a[min_index] = tmp


if __name__ == "__main__":
    array = [1, 1, 1, 1]
    bubble_sort(array)
    print(array)

    array = [1, 2, 3, 4]
    bubble_sort(array)
    print(array)

    array = [4, 3, 2, 1]
    bubble_sort(array)
    print(array)

    array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
    bubble_sort(array)
    print(array)

    array = [1, 1, 1, 1]
    insertion_sort(array)
    print(array)

    array = [1, 2, 3, 4]
    insertion_sort(array)
    print(array)

    array = [4, 3, 2, 1]
    insertion_sort(array)
    print(array)

    array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
    insertion_sort(array)
    print(array)

    array = [1, 1, 1, 1]
    selection_sort(array)
    print(array)

    array = [1, 2, 3, 4]
    selection_sort(array)
    print(array)

    array = [4, 3, 2, 1]
    selection_sort(array)
    print(array)

    array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
    selection_sort(array)
    print(array)