from statsmodels.stats.stattools import durbin_watson

class AutoCorrelation:
    def __init__(self, residuals):
        self.residuals = residuals

    def autocorrelation_test(self):
        stat = durbin_watson(self.residuals)
        if stat == 2:
            print('No autocorrelation in the residuals')
        elif stat < 2 and stat >= 0:
            print('Positive autocorrelation in the residuals')
        elif stat > 2 and stat <= 4:
            print('Negative autocorrelation in the residuals')