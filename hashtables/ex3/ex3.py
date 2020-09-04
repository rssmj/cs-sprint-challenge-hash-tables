def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    # create cache
    cache = {}
    # set result
    result = []
    # loop through arrays
    for arr in arrays:
        # loop through array values
        for value in arr:
            # check if in cache and not result
            if value in cache and value not in result:
                # add to result
                result.append(value)
            else:
                cache[value] = 1
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
