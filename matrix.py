
class Matrix(object):

    def __init__(self, p, q, init=True):
            if init:
                self.rows = [[0] * q for x in range(p)]
            else:
                self.rows = []
            self.p = p
            self.q = q

    def __str__(self):
        s = '\n'.join([' '.join([str(item) for item in row]) for row in self.rows])
        return s + '\n'

    def __getitem__(self, idx):
        return self.rows[idx]

    def __setitem__(self, idx, item):
        self.rows[idx] = item

    def transpose(self):
        p = self.q
        q = self.p
        matrix = Matrix(p,q)
        for x in range(p):
            for y in range(q):
                matrix.rows[x][y]=self.rows[y][x]
        return matrix

    def mult(self, targetMatrix):
        if self.p == targetMatrix.q:
            matrix_t=targetMatrix.transpose()
            resultMatrix = Matrix(self.p, targetMatrix.q)
            for x in range(self.p):
                for y in range(matrix_t.p):
                    resultMatrix[x][y] = sum([int(item[0])*int(item[1]) for item in zip(self.rows[x], matrix_t[y])])
            return resultMatrix


    @classmethod
    def readMatrix(self, file):
        file_object = open(file, "r")
        rows = [];
        for line in file_object.readlines():
            line = line.rstrip("\n")
            if "x" in line:
                p = int(line[:line.find("x")])
                q = int(line[line.find("x") + 1:])
            else:
                rows += [line.split(',')]
        file_object.close()
        newMatrix = Matrix(p,q)
        newMatrix.rows=rows
        return newMatrix














