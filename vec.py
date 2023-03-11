class Vec:
    def __init__(self, labels, function):
        self.D = labels
        self.f = function

    def setitem(self, d, val):
        self.f[d] = val

    def getitem(self, d):
        return self.f[d] if d in self.f else 0


