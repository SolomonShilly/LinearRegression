import matplotlib.pyplot as plt
import seaborn as sns

class Residuals:
    def __init__(self, residuals):
        self.residuals = residuals

    def visualize_residuals(self):
        sns.histplot(self.residuals, kde=True)
        plt.title('Histogram and KDE of Residuals')
        plt.xlabel('Residuals')
        plt.show()

