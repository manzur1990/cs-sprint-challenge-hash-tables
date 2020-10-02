#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    1. initate a hash table
    2. set a node like variable
    3. iterate through the ticket
    4. for each ticket
        a. location = key
        b. destination = value
    5. try to implement a link list logic. 
    """
    # Your code here

    cache = {}
    route = [None] * length

    for ticket in tickets:
        cache[ticket.source] = ticket.destination

    next = cache["NONE"]

    for i in range(length):
        route[i] = next
        next = cache[next]

    return route
