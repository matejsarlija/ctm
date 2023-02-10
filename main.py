
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

print(makeInverseIndex(lines))

def orSearch(inverseIndex, query):
    for x in query:
        if x in inverseIndex:
            return inverseIndex.get(x)
def andSearch(inverseIndex, query):
    return {inverseIndex[x] for x in query if x in inverseIndex}

print(orSearch(makeInverseIndex(lines), ['matej', 'je']))