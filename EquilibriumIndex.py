"""
TASK
    Write a function that, given a sequence, returns its equilibrium indices
    (if any). Assume that the sequence may be very long. Feel free to Google for
    hints, but give lots of comments about what your thoughts are and your
    process for devising an algorithm.

TEST
    from EquilibriumIndex import eqindex
    d = ([-7, 1, 5, 2, -4, 3, 0],
         [2, 4, 6],
         [2, 9, 2],
         [1, -1, 1, -1, 1, -1, 1])
    for data in d:
        print("Test: %r" % data)
        print("Result: %r" % list(eqindex(data)))

DESIGN
    find the eqil index of a list that might be very long
        *linear might be too slow for large lists
        *corner cases: might be more than one eqindex, might be no eqindex, list
            might have an equilibrium but no index( ie. Happened in between
            indexes like [4,4,8]
    looks like the test scrip expects a list to be returned
    objects: list_section(lower_list, upper_list), current_index
        list_section:
            attributes: number_list
            Methods: sum
        current_index:
            attributes: current_index, data_list
            methods: split_list, comp_sides

ASSUMPTIONS
    1- When no eqindex can be found return an empty list

PSEUDO-CODE
    sum_of_list [2,6,4,6,1,8,10] = 37
    then you can iterate through the list adding and subtracting
        sum_of_left =0; sum_of_left+=current_index
        sum_of_right=sum_of_list; sum_of_right -= current_index
        if sum_of_left == sum_of_right:
            append_eqindex_list()
"""

def eqindex(data):
    r_sum = sum(data) #right side total
    l_sum = 0 #left side total
    pr_num = 0 #keep track of previous number
    eq_list = [] #list to hold the index of equilib locations

    for i,item in enumerate(data):
        try:
            assert type(item) == int #make sure we are working with integers
        except AssertionError:
            print("Must supply a list of ints")
        r_sum -= item
        l_sum += pr_num
        pr_num = item
        if r_sum == l_sum:
            if i == 0 or i == len(data)-1: #ignore the first and last index
                                           #because the numbers might total
                                           #to 0
                continue
            else:
                eq_list.append(i) #make the list of equil indexes

    return(eq_list)

