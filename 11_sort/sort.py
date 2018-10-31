"""
Bubble sort, insertion sort, and selection sort
"""


def bubble_sort(a):
    """
    Bubble sort
    :param a: a list of ints
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
                a[j] = a[j+1]
                flag = True
        if not flag:
            break