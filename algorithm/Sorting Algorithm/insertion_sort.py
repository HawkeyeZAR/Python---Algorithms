#  Time	Complexity						        Space Complexity
#  Best:Ω(n) 	Average:Θ(n^2) 	Worst:O(n^2) 	Worst:O(1)

def insert(L, b):
    """ (list, int) -> NoneType

    Precondition: L[0:b] is already sorted.
    Insert L[b] where it belongs in L[0:b + 1].

    >>> L = [3, 4, -1, 7, 2, 5]
    >>> insert(L, 2)
    >>> L
    [-1, 3, 4, 7, 2, 5]
    """
    # Find where to insert L[b] by searching backwards from L[b]
    # for a smaller item.
    i = b
    while i != 0 and L[i - 1] >= L[b]:
        i = i - 1

    value = L[b]  # Move L[b] to index i, shifting following values to the right.
    del L[b]
    L.insert(i, value)

def insertion_sort(L):
    """ (list) -> NoneType

    Reorder the items in L from smallest to largest.

    >>> L = [3, 4, 7, -1, 2, 5]
    >>> insertion_sort(L)
    >>> L
    [-1, 2, 3, 4, 5, 7]
    """
    i = 0 # The index of the first unknown item in lst; L[:i] is sorted
    
    while i != len(L):
        # Insert L[i] where it belongs in L[0:i+1].
        insert(L, i)
        i = i + 1
    return L

##########################  Another Example ##########################
def insertion_sort2(lst):
    """ 
    (list) -> NoneType

    Reorder the items in L from smallest to largest.
    """
    n = len(lst)
    # Starts with the first item as the only sorted entry.
    for i in range(1, n) :
        # Save the value to be positioned.
        value = lst[i]
        # Find the position where value fits in the ordered part of the list.
        pos = i
        while pos > 0 and value < lst[pos - 1] :
            # Shift the items to the right during the search.
            lst[pos] = lst[pos - 1]
            pos -= 1    
    # Put the saved value into the open slot.
    lst[pos] = value
    return lst

lst = [5, 4, 1, 3, -5, -1, -6, 2, 6]
print(insertion_sort(lst))
print(insertion_sort2(lst))