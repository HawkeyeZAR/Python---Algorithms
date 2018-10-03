def built_in_sort(v, lst):
    """
    Python's built in list sort function
    """
    lst.sort() # sort list in place
    index = lst.index(v) # find item v and return its index
    result = 'Index no: {0} Value is: {1}'.format(index,lst[index])
    return result

my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
new_list = [str(n) for n in range(1000000)]

print(built_in_sort('m', my_list))
print(built_in_sort('99', new_list))


