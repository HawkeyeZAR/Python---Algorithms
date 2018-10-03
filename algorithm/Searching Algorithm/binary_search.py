def binary_search(v, lst):
    """
    (object, list) -> int

    v must exist in lst for this function to work correctly

    Return the mid of the first occurrence of value in lst, 
    if value not in list, infinate loop occurs.
    """
    left = 0 # Determines the starting index of the list we have to search in
    right = len(lst) - 1 # Determines the last index of the list we have to search in
    mid = (right + left) // 2
    
    while lst[mid] != v: # If this is not our search element
        # If the current middle element is less than v then move the left next to mid
        # Else we move right next to mid
        if  lst[mid] < v:
            left = mid + 1
        else:
            right = mid - 1
        mid = (right + left) // 2 
    return mid

##########################  Another Example ##########################
def binary_search2(v, lst):
    """
    (object, list) -> int

    Return the index of the first occurrence of value in lst, 
    or return -1 if value is not in lst.
    """
    left = 0  # Determines the starting index of the list we have to search in
    right = len(lst) -1  # Determines the last index of the list we have to search in

    while left != right + 1:
        middle = (left + right) // 2
        # If the current middle element is less than v then move the left next to mid
        # Else we move right next to mid
        if lst[middle] < v:
            left = middle + 1
        else:
            right = middle - 1
    if 0 <= left < len(lst) and lst[left] == v:
        return left
    else:
        return -1

##########################  Another Example ##########################
def binary_search3(lst, v):
    """
    (list, object) -> int

    Return the index of the first occurrence of value in lst, 
    or return -1 if value is not in lst.
    """
    index = 0  # Mark the left and right indices of the unknown section.
    right = len(lst) - 1

    while index != right + 1:
        middle = (index + right) // 2
        if lst[middle] < v:
            index = middle + 1
        else:
            right = middle - 1
    if 0 <= index < len(lst) and lst[index] == v:
        return index
    else:
        return -1

##########################  Another Example ##########################
def binary_search4(lst, item):
    """
    (lst, object) -> int

    Return the index of the first occurrence of value in lst, 
    or return None if value is not in lst.
    """
    low = 0  # low and high keep track of which part of the list you’ll search in.
    high = len(lst) - 1

    # Repeatedly subdivide the sequence in half until the target is found.
    while low <= high:
        mid = (low + high)
        guess = lst[mid]
        # Does the midpoint contain the item?
        if guess == item:
            return mid
        # Or does the item precede the midpoint?
        if guess > item:
            high = mid - 1
        # Or does the item follow the midpoint?       
        else:
            low = mid + 1
        # If item not found, return None
    return None

my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
print(binary_search('c', my_list))
print(binary_search2('c', my_list))
print(binary_search3(my_list, 'e'))
print(binary_search4(my_list, 'm'))

