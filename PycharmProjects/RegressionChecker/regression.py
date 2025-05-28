import statsmodels.api as sm
import numpy as np

class Regression:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

    def linear_regression(self):
        self.X = np.transpose(self.X)
        xConst = sm.add_constant(self.X)
        model = sm.OLS(self.Y, xConst).fit()
        print(model.summary())
        residuals = model.resid
        return model, residuals, xConst
