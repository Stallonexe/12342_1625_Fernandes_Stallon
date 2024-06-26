class Matrix:
    def __init__(self):
        self.Row = []
        self.Rank = []
        self.Matrix = []

    def MatrixProcedure(self):
        self.InitialRank()
        for i in range(3):
            self.MultiplyMatrix()





    def AppendMatrix(self, Matrix_dict):
        for key, value in Matrix_dict.items():
            if key not in self.Row:
                self.Row.append(key)
                self.Matrix.append(value[:len(Matrix_dict)])

        self.MatrixProcedure()



    def InitialRank(self):
        for i in range(len(self.Row)):
            rank = 1 / len(self.Row)
            self.Rank.append(rank)


    def MultiplyMatrix(self):
        Rank = []
        for row in self.Matrix:

            Row_Sum = []
            for i in range(0, len(row)):

                rank = (row[i] * self.Rank[i])

                Row_Sum.append(rank)

            total = 0
            for i in range(0,len(Row_Sum)-1):
                total += Row_Sum[i]

            Rank.append(total)

        self.Rank = Rank


    def ConvertToDictionary(self):
        Dictionary = {}
        size = len(self.Row)
        for i in range(size):
            Dictionary[self.Row[i]] = self.Rank[i]
        return Dictionary

    def GetRank(self):
        RankDictionary = self.ConvertToDictionary()
        Rank = sorted(self.Row, key=lambda ID: RankDictionary[ID], reverse=True)
        return Rank


#Matrix = Matrix()

#Matrix.AppendMatrix({'H1': [0.0, 0.25, 0.25, 0.5],'H2': [0.5, 0.0, 0.0, 0.5],'H3': [0.5, 0.0, 0.0, 0.5],'H4': [0.5, 0.25, 0.25, 0.0]})
