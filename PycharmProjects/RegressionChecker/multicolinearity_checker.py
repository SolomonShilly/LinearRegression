import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor

class VIF:
    def __init__(self, xConst):
        self.xConst = xConst

    def vif(self):
        data = pd.DataFrame()
        data['VIF'] = [variance_inflation_factor(self.xConst, i) for i in range(len(self.xConst[0,:]))]
        print(data)
        return data