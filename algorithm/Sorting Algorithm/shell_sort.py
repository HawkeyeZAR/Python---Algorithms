#  Time	Complexity						                                Space Complexity
#  Best:Ω(n log(n))   Average:Θ(n(log(n))^2)   Worst:O(n(log(n))^2) 	Worst:O(1)

def shell_sort(_list):
    """
    Author: OMKAR PATHAK
    Created On: 31st July 2017

    Shell sort algorithm
    :param _list: list of integers to sort
    :return: sorted list
    """
    gap = len(_list) // 2
    while gap > 0:
        for i in range(gap, len(_list)):
            current_item = _list[i]
            j = i
            while j >= gap and _list[j - gap] > current_item:
                _list[j] = _list[j - gap]
                j -= gap
            _list[j] = current_item
        gap //= 2
    return _list

##########################  Another Example ##########################
def shell_sort2(collection):
    """
    :param collection:  Some mutable ordered collection with heterogeneous
    comparable items inside
    :return:  the same collection ordered by ascending
    >>> shell_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    """
    # Marcin Ciura's gap sequence
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]
    for gap in gaps:
        i = gap
        while i < len(collection):
            temp = collection[i]
            j = i
            while j >= gap and collection[j - gap] > temp:
                collection[j] = collection[j - gap]
                j -= gap
            collection[j] = temp
            i += 1
    return collection

print(shell_sort([10, 5, 2, 3, -1, -6, -3, 9, -2]))
print(shell_sort2([10, 5, 2, 3, -1, -6, -3, 9, -2]))
