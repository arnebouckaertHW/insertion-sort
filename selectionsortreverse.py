def sort (data, last: int):
    """Sorts a list of integers from smallest to largest bypassing the elements to the right of last.

    Args:
        data (int): list of integers
        last (int): the list index at which the sort will end
    """
    # initialize loop counter variables named i, j
    i = 0
    j = 0

    # initialize variable named small used to store index of smallest value
    small = 0

    # initialize variable named temp used to swap list values
    temp = 0
    
    while (i < last):
        # set small equal to last
        small = last

        # set j equal to last - 1
        j = last - 1

        while (j >= i):
            # if value in data[small] is more than value in data[j], set small equal to j
            if (data[j] < data[small]):
                small = j

            # decrement j
            j -= 1
        
        # set temp to value in data[i]
        temp = data[i]

        # set data[i] to value in data[small]
        data[i] = data[small]

        # set data[small] to value in temp
        data[small] = temp

        # increment i
        i += 1