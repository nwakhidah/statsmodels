class PLSReg(object):
    def __init__(self, endog, exog, ncomp=None, standardize=True):
        pass

    def fit(self, method='nipals'):
        pass


class PCAReg(object):
    def __init__(self, endog, exog, ncomp=None, standardize=True):
        pass

    def fit(self, method='svd'):
        pass


class RegularizedReducedRankReg(object):
    def __init__(self, endog, exog, ncomp=None, method='svd',
                 standardize=True):
        pass

    def fit(self, regularization='spectral'):
        pass


class ThreePassReg(object):
    def __init__(self, endog, exog, instr, ncomp=None, ninstr=None,
                 standardize=True):
        pass

    def fit(self):
        pass
