class Matrix:
    def __init__(self, matrix_string):
        self.mtx = []
        for i in matrix_string.splitlines():
            self.mtx.append([int(j) for j in i.split()])

    def row(self, index):
        return self.mtx[index - 1]

    def column(self, index):
        return [i[index - 1] for i in self.mtx]
