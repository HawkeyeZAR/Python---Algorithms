#  Time	Complexity						                            Space Complexity
#  Best:Ω(n log(n)) 	Average:Θ(n log(n)) 	Worst:O(n log(n)) 	Worst:O(1)

def sort(_list):
    """
    Author: OMKAR PATHAK
    Created On: 31st July 2017

    heap sort algorithm
    Create the heap using heapify().
    This is an implementation of max-heap, so after bullding the heap, the max element is at the top (_list[0]).
    We move it to the end of the list (_list[end]), which will later become the sorted list.
    After moving this element to the end, we take the element in the end to the top and shift it down to its right location in the heap.
    We proceed to do the same for all elements in the heap, such that in the end we're left with the sorted list.

    :param _list: list of values to sort
    :return: sorted values
    """
    # create the heap
    heapify(_list)              
    end = len(_list) - 1
    while end > 0:
        _list[end], _list[0] = _list[0], _list[end]
        shift_down(_list, 0, end - 1)
        end -= 1
    return _list

def heapify(_list):
    """
    function helps to maintain the heap property
    
    :param _list: list of values to sort
    :return: sorted values
    """
    start = len(_list) // 2
    while start >= 0:
        shift_down(_list, start, len(_list) - 1)
        start -= 1

def shift_down(_list, start, end):
    root = start
    while root * 2 + 1 <= end:
        child = root * 2 + 1
        # right child exists and is greater than left child
        if child + 1 <= end and _list[child] < _list[child + 1]:
            child += 1
        # if child is greater than root(parent), then swap their positions
        if child <= end and _list[root] < _list[child]:
            _list[root], _list[child] = _list[child], _list[root]
            root = child
        else:
            return

##########################  Another Example ##########################
def max_heapify(seq, i, n):
    """
    Heap Sort
    Psuedo Code: CLRS. Introduction to Algorithms. 3rd ed.

    The function of max_heapify is to let the value at seq[i] "float down" in
    the max-heap so that the subtree rooted at index i becomes a max-heap.
    :param seq: A list of integers
    :param i: An integer that is an index in to the list that represents the
              root of a subtree that max heapify is called on.
    :param n: length of the list
    """
    l = 2 * i + 1
    r = 2 * i + 2
    if l <= n and seq[l] > seq[i]:
        largest = l
    else:
        largest = i
    if r <= n and seq[r] > seq[largest]:
        largest = r
    if largest != i:
        seq[i], seq[largest] = seq[largest], seq[i]
        max_heapify(seq, largest, n)

def build_heap(seq):
    """
    Continously calls max_heapify on the list for each subtree.
    :param seq: A list of integers
    """
    n = len(seq) - 1
    for i in range(n//2, -1, -1):
        max_heapify(seq, i, n)

def sort2(seq):
    """
    Takes a list of integers and sorts them in ascending order. This sorted
    list is then returned.
    :param seq: A list of integers
    :rtype: A list of sorted integers
    """
    build_heap(seq)
    heap_size = len(seq) - 1
    for x in range(heap_size, 0, -1):
        seq[0], seq[x] = seq[x], seq[0]
        heap_size = heap_size - 1
        max_heapify(seq, 0, heap_size)
    return seq

my_list = ['c', 'h', 'i', 'j', 'k', 'l', 'm', 'd', 'e', 'f', 'g', 'a', 'b']
my_list2 = [-1, 2, 5, -3, 3, -4, 9, -2]
print(sort(my_list))
print(sort(my_list2))
########### Second Example Print Statements###############
print(sort2(my_list))
print(sort2(my_list2))