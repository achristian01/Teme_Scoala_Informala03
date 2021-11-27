
class Fractie():
    def __init__(self, numarator, numitor):
        self.numarator = numarator
        self.numitor = numitor
        if not isinstance(numarator, int):
            raise TypeError
        if not isinstance(numitor, int):
            raise TypeError
        if numitor != 0:
            return numarator / numitor
        else:
            print("You cannot perform this operation.")

    def __str__(self):
        return str(self.numarator) + "/" + str(self.numitor)

    def __add__(self, numarator, numitor):





