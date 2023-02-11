
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


def orSearch(inverseIndex, query):
    result_dict = set()

    for x in query:
        if x in inverseIndex:
            result_dict.update(inverseIndex.get(x))

    return result_dict


def and_search(inverseIndex, query):
    return {inverseIndex[x] for x in query if x in inverseIndex}

print(orSearch(our_index, ['matej', 'je']))