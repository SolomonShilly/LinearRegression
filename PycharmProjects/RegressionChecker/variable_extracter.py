import numpy as np

class VariableExtracter:
    def __init__(self, data):
        self.data = data

    def assign_variables(self):
        X = []
        Y = []

        while True:
            try:
                col = int(input('What column number would you like to predict? (Start at 1): ')) - 1
                if col < 0:
                    raise ValueError
                break
            except ValueError:
                print('Please enter a valid column index (integer greater than 0).')

        lines = self.data.strip().split('\n')

        for line in lines:
            try:
                values = [float(v.strip()) for v in line.split(',')]

                if col >= len(values):
                    raise IndexError("Selected column index is out of range.")

                Y.append(values[col])

                xI = []
                for index, value in enumerate(values):
                    if index != col:
                        xI.append(value)
                X.append(xI)

            except (ValueError, IndexError) as e:
                print(f'Unable to parse line: "{line}". Error: {e}')

        X = np.transpose(X)
        return X, Y
