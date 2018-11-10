"""
Quick sort
"""


def quick_sort(a):
    """
    Quick sort
    :param a: a list
    :return: 
    """
    _quick_sort_internal(a, 0, len(a) - 1)


def _quick_sort_internal(a, p, r):
    if p >= r:
        return

    q = _partition(a, p, r)
    _quick_sort_internal(a, p, q - 1)
    _quick_sort_internal(a, q + 1, r)


def _partition(a, p, r):
    pivot = a[r]
    i = p
    for j in range(p, r):
        if a[j] < pivot:
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp
            i += 1
    tmp = a[i]
    a[i] = pivot
    a[r] = tmp
    return i


if __name__ == "__main__":
    a1 = [3, 5, 6, 7, 8]
    a2 = [2, 2, 2, 2]
    a3 = [4, 3, 2, 1]
    a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
    quick_sort(a1)
    print(a1)
    quick_sort(a2)
    print(a2)
    quick_sort(a3)
    print(a3)
    quick_sort(a4)
    print(a4)