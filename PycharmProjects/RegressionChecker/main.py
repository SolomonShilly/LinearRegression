from autocorrelation_test import AutoCorrelation
from file_handler import FileHandler
from homoscedasticity_checker import VarianceChecker
from linearity_checker import LinearityChecker
from regression import Regression
from residual_normality import Residuals
from variable_extracter import VariableExtracter
from multicolinearity_checker import VIF

class Main:
    def main(self):
        vars = VariableExtracter(FileHandler().open_file())
        X, Y = vars.assign_variables()
        LinearityChecker(X, Y).grapher()
        check = VarianceChecker(X, Y)
        check.levene_test()
        lr = Regression(X, Y)
        model, residuals, xConst = lr.linear_regression()
        Residuals(residuals).visualize_residuals()
        AutoCorrelation(residuals).autocorrelation_test()
        vifData = VIF(xConst).vif()

Main().main()