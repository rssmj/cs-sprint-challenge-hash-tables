#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    # create ticket cache
    ticket_cache = {}
    # set route length
    route = [None] * length
    # loop to initiate cache
    for t in tickets:
        ticket_cache[t.source] = t.destination
    next = ticket_cache['NONE']
    # # loop through length to set route to next
    for i in range(length):
        route[i] = next
        next = ticket_cache[next]
    return route

    # next = 'NONE'
    # for i in range(length):
    #     if i == 0:
    #         route[i] = ticket_cache[next]
    #         next = ticket_cache[route[i]]
    #         continue
    #     route[i] = next
    #     next = ticket_cache[route[i]]
