import matplotlib.pyplot as plt

class LinearityChecker:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

    def grapher(self):
        for xI in self.X:
            plt.scatter(xI, self.Y)
            plt.xlabel(f'xI{0}')
            plt.ylabel(f'Y{0}')
            plt.title('Linearity Check: X vs Y')
            plt.show()