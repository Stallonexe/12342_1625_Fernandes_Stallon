class Matrix:
    def __init__(self):
        self.Row = []
        self.Rank = []
        self.Matrix = []

    def AppendMatrix(self, Matrix_dict):
        for key, value in Matrix_dict.items():
            if key not in self.Row:
                self.Row.append(key)
                self.Matrix.append(value[:len(Matrix_dict)])

    def UpdateMatrix(self, Matrix_dict):
        self.Matrix = []
        self.Row = []
        for key, value in Matrix_dict.items():
            self.Row.append(key)
            self.Matrix.append(value[:len(Matrix_dict)])

    def InitialRank(self):
        for i in range(len(self.Row)):
            rank = 1 / len(self.Row)
            self.Rank.append(rank)
        print(self.Rank)

    def MultiplyMatrix(self):
        Rank = []
        for row in self.Matrix:

            Row_Sum = []
            for i in range(0, len(row)):

                rank = (row[i] * self.Rank[i])

                Row_Sum.append(rank)

            Rank.append(sum(Row_Sum))

        self.Rank = Rank
        print(self.Rank)





A = Matrix()

A.AppendMatrix({"A": [0,1,0,2],
               "B": [2,6,7,9],
               "C": [1,3,5,4],
               "D": [0,2,4,8]})
print(f"{A.Row}, \n{A.Matrix} dslf")

A.UpdateMatrix({"A": [0,0,0.5,0.5],
                "B": [1,0,0,0.5],
                "C": [0,0.5,0,0],
                "D": [0,0.5,0.5,0]})

print(f"{A.Row}, \n{A.Matrix} ")

A.InitialRank()

for i in range(100):
    A.MultiplyMatrix()
