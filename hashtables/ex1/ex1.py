def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    
    # create cache
    cache = {}
    # loop through list
    for i in range(length):
        # set key
        w = weights[i]
        # compare limit and w
        value = (limit - w)
        # if value exists in table
        if value in cache:
            result = cache[value]
            # return tuple
            return (i, result)
        else:
            # set key to index
            cache[w] = i
    return None
