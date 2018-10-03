"""
Author: SHARAD BHAT
Created On: 22nd August 2017

 - Best O(1)
 - Average O(log(logn))
 - Worst O(n)
"""

def search(_list, target):
    """
    This function performs an interpolation search
    on a sorted list and returns the index
    of item if successful else returns False

    :param _list: list to search
    :param target: item to search for
    :return: index of item if successful else returns False
    """
    if type(_list) is not list:
        raise TypeError("interpolation search only accepts lists, not {}".format(str(type(_list))))
    # First element
    low = 0
    # Last element
    high = len(_list) - 1
    # List is assumed to be sorted
    while low <= high and target >= _list[low] and target <= _list[high]:
        position = low + int(((float(high - low) / (_list[high] - _list[low])) * (target - _list[low])))
        if _list[position] == target:
            return position
        # If target is greater, search in right half
        if _list[position] < target:
            low = position + 1
        # If target is smaller, search in left half
        else:
            high = position - 1
    return False

##########################  Another Example ##########################
def search2(sorted_collection, item):
    """
    Be careful collection must be sorted, otherwise result will be
    unpredictable
    :param sorted_collection: some sorted collection with comparable items
    :param item: item value to search
    :return: index of found item or None if item is not found
    """
    left = 0
    right = len(sorted_collection) - 1
    while left <= right:
        point = left + ((item - sorted_collection[left]) * (right - left)) // (sorted_collection[right] - sorted_collection[left])
        #out of range check
        if point<0 or point>=len(sorted_collection):
            return None
        current_item = sorted_collection[point]
        if current_item == item:
            return point
        else:
            if item < current_item:
                right = point - 1
            else:
                left = point + 1
    return None

my_list = [i for i in range(20)]
print(search(my_list, 4))
print(search2(my_list, 19))