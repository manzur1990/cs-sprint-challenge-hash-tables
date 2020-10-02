def has_negatives(a):
    """
    YOUR CODE HERE
    1. set up a result list
    2. set up a hash table
    3. loop through list _a_
        a. set up posetive number int in the hash table
        b. if number not 0 or in dictionary
            a. append to dictionary
    """
    # Your code here
    result = []
    ht = {}

    for pn in a:
        ht[pn] = pn

        if pn != 0 and -pn in ht:
            result.append(abs(pn))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
