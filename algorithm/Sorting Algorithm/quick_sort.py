#  Time	Complexity					                            Space Complexity
#  Best:Ω(n log(n))     Average:Θ(n log(n))     Worst:O(n^2)	Worst:O(log(n))

def quicksort(array):
    """
    (array) -> int

    Return sorted array.
    """
    if len(array) < 2:
        #  Base case: arrays with 0 or 1 element are already “sorted.”
        return array
    else:
        #  Recursive case
        pivot = array[0]
        #  Sub-array of all the elements less than the pivot
        less = [i for i in array[1:] if i <= pivot]
        #  Sub-array of all the elements greater than the pivot
        greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)

##########################  Another Example ##########################
def quicksort2(_list):
    """
    Author: OMKAR PATHAK
    Created On: 31st July 2017
    quick_sort algorithm
    :param _list: list of integers to sort
    :return: sorted list
    """
    if len(_list) <= 1:
        return _list
    pivot = _list[len(_list) // 2]
    left = [x for x in _list if x < pivot]
    middle = [x for x in _list if x == pivot]
    right = [x for x in _list if x > pivot]
    return quicksort2(left) + middle + quicksort2(right)

##########################  Another Example ##########################
def quick_sort(ARRAY):
    """
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    Examples:
    >>> quick_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> quick_sort([])
    []
    """
    ARRAY_LENGTH = len(ARRAY)
    if ARRAY_LENGTH <= 1:
        return ARRAY
    else:
        PIVOT = ARRAY[0]
        GREATER = [ element for element in ARRAY[1:] if element > PIVOT ]
        LESSER = [ element for element in ARRAY[1:] if element <= PIVOT ]
    return quick_sort(LESSER) + [PIVOT] + quick_sort(GREATER)

print(quicksort([10, 5, 2, 3, -1, -6, -3, 9]))
print(quicksort2([10, 5, 2, 3, -1, -6, -3, 9, -2]))
print(quick_sort([10, 5, 2, 3, -1, -6, -3, 9, -2]))
