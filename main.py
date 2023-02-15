
f = open("input2.txt")
lines = list(f)

def makeInverseIndex(strlist):
    ourDict = {x:set(y.split()) for x,y in enumerate(strlist)}
    inverseIndexDict = {}

    for x in ourDict.items():
        for y in x[1]:
            if y in inverseIndexDict:
                inverseIndexDict[y].add(x[0])
            else:
                inverseIndexDict[y] = {x[0]}

    return inverseIndexDict

our_index = makeInverseIndex(lines)
print(our_index)


def or_search(inverse_index, query):
    result_set = set()

    for x in query:
        if x in inverse_index:
            result_set.update(inverse_index.get(x))

    return result_set


# Write a procedure andSearch(inverseIndex, query) which takes an inverse
# index and a list of words query, and returns the set of document numbers specifying
# all documents that contain all the words in query.
def and_search(inverse_index, query):
    result_set = set()

    for x in query:
        if x in inverse_index:
            if result_set:
                result_set.intersection_update(inverse_index.get(x))
            else:
                result_set.update(inverse_index.get(x))

    return result_set


print(and_search(our_index, ['matej', 'ok']))

