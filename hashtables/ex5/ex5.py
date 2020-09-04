# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here

    # create cache
    cache = {}
    # set result
    result = []
    # loop through queries
    for q in queries:
        if q not in cache:
            # add to cache
            cache[q] = 1
    # loop through path
    for f in files:
        f_text = f.split("/")[-1]
        # if exists in query
        if f_text in cache:
            # add to list
            result.append(f)
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
