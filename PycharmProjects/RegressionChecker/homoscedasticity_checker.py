from scipy import stats

class VarianceChecker:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

    def levene_test(self):
        ci = [0.01, 0.05, 0.10]
        try:
            alpha = float(input('Enter Confidence Interval in decimal form: '))
            while alpha not in ci:
                print('Please enter a valid confidence interval (.01, .05, .10)\n')
                alpha = float(input('Enter Confidence Interval in decimal form: '))
        except Exception as e:
            print(f'Error: {e}')

        for xI in self.X:
            stat, pVal = stats.levene(xI, self.Y)

            if (pVal < alpha).any():
                print("Heteroskedasticity detected!")
            else:
                print("Homoskedasticity likely.")

