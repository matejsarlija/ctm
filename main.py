
f = open("input2.txt")
lines = list(f)
#print(lines)
#print([x.split() for x in lines])
def makeInverseIndex(strlist):
    ourDict = {x:set(y.split()) for x,y in enumerate(strlist)}
    inverseIndexDict = {}

    for x in ourDict.items():
        for y in x[1]:
            inverseIndexDict[y] = x[0]

    return inverseIndexDict

print(makeInverseIndex(lines))

def orSearch(inverseIndex, query):
    return {inverseIndex[x] for x in query if x in inverseIndex}

print(orSearch(makeInverseIndex(lines), ['ali', 'matej']))