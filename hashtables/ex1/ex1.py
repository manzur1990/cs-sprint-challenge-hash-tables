def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE

    1. find a way to iterate through the length of the list
    2. create a hash table that will take indices related to the weight of item
    3. reference the index in weights list
    4. if the index in weight is in the cache then assign a value 
    5. calculate wieght difference

    """
    # Your code here

    cache = {}

    # Go through items in weights & add to the dictionary.
    for item in range(length):
        weight = weights[item]

        if weight in cache:
            value = cache[weight]
            return (item, value)

        weight_differece = limit - weight
        cache[weight_differece] = item

    return None
