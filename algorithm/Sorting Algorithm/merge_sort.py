#  Time	Complexity					                                Space Complexity
#  Best:Ω(n log(n)) 	Average:Θ(n log(n)) 	Worst:O(n log(n)) 	Worst:O(n)

def merge(L1, L2):
    """ (list, list) -> list
    Merge sorted lists L1 and L2 into a new list and return that new list.
    >>> merge([1, 3, 4, 6], [1, 2, 5, 7])
    [1, 1, 2, 3, 4, 5, 6, 7]
    """
    newL = []
    i1 = 0
    i2 = 0
    # For each pair of items L1[i1] and L2[i2], copy the smaller into newL.
    while i1 != len(L1) and i2 != len(L2):
        if L1[i1] <= L2[i2]:
            newL.append(L1[i1])
            i1 += 1
        else:
            newL.append(L2[i2])
            i2 += 1
    # Gather any leftover items from the two sections.
    # Note that one of them will be empty because of the loop condition.
    newL.extend(L1[i1:])
    newL.extend(L2[i2:])
    return newL

def mergesort(L):
    """ (list) -> NoneType
    Reorder the items in L from smallest to largest.
    >>> L = [3, 4, 7, -1, 2, 5]
    >>> mergesort(L)
    >>> L
    [-1, 2, 3, 4, 5, 7]
    """
    # Make a list of 1-item lists so that we can start merging.
    workspace = []
    for i in range(len(L)):
        workspace.append([L[i]])
    # The next two lists to merge are workspace[i] and workspace[i + 1].
    i = 0
    # As long as there are at least two more lists to merge, merge them.
    while i < len(workspace) - 1:
        L1 = workspace[i]
        L2 = workspace[i + 1]
        newL = merge(L1, L2)
        workspace.append(newL)
        i += 2
    # Copy the result back into L.
    if len(workspace) != 0:
        L[:] = workspace[-1][:]
    return L

##########################  Another Example ##########################
def merge_sort(lst):
    '''
    Fastest version of merge_sort

    Takes an average of 0.6 microseconds to sort a list of length 1000 items.
    Best Case Scenario : O(n)
    Worst Case Scenario : O(n)
    '''
    start = []
    end = []
    while len(lst) > 1:
        a = min(lst)
        b = max(lst)
        start.append(a)
        end.append(b)
        lst.remove(a)
        lst.remove(b)
    if lst: 
        start.append(lst[0])
    end.reverse()
    return (start + end)

lst = [5, 4, 1, 3, -5, -1, -6, 2, 6]
print(mergesort(lst))
print(merge_sort(lst))  #  fast version