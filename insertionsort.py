def sort (data, first: int):
    """Sorts a list of integers from smallest to largest bypassing the elements to the left of first.

    Args:
        data (int): list of integers
        first (int): the list index at which the sort will begin
    """
    # initialize loop counter variable i to 1
    i = 1

    # initialize loop counter variable j to 0
    j = 0

    # declare variable for next value
    nextVal = 0

    # loop as many times through the list as specified by the length of the list and first
    # this loop reperesents the blue arrow
    while(i < len(data) - first):
        # store a copy of the value at data[first + i] in nextVal
        nextVal = data[first + i]

        # loop through the list starting at the same index as next value and
        # iterate back toward first as long as the element to the left of next value
        # is greater than next value and we're not the whole way back to first
        j = first + i
        while(j > first and data[j - 1] > nextVal):
            # shift the element to the left of next value one position to the right
            data[j] = data[j - 1]

            # insert next value into the element that was just shifted
            data[j - 1] = nextVal

            # decrement j by 1
            j -= 1
        
        # increment i by 1
        i += 1