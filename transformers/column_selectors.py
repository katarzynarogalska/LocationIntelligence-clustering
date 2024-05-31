from sklearn.base import BaseEstimator,TransformerMixin

class FirstColumnSelector(BaseEstimator,TransformerMixin):
    def __init__(self):
        self.columns = ['geo_cluster','rating','review_count','main_category']
    def fit(self,X,y=None):
        return self
    def transform(self,X):
        return X[self.columns]
    def set_output(self, *args, **kwargs):
        return self
    
class SecondColumnSelector(BaseEstimator,TransformerMixin):
    def __init__(self):
        pass
    def fit(self,X,y=None):
        return self
    def transform(self,X):
        high_cols = treshold_columns(X,0.15)
        return X[high_cols]
    def set_output(self, *args, **kwargs):
        return self
    
class ThirdColumnSelector(BaseEstimator,TransformerMixin):
    def __init__(self):
        pass
    def fit(self,X,y=None):
        return self
    def transform(self,X):
        high_cols = treshold_columns(X,0)
        return X[high_cols]
    def set_output(self, *args, **kwargs):
        return self
    
def treshold_columns(X,t):
    variances = X.var()
    high_variance_cols = variances[variances>t].index
    return high_variance_cols
