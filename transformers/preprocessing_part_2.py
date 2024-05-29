from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd


class MoreColumnsRemover(BaseEstimator,TransformerMixin):
    def __init__(self):
        self.columns_to_remove = ['name','latitude','longitude','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    def fit(self,X,y=None):
        return self
    def transform(self,X):
        X=X.drop(columns = self.columns_to_remove)
        return X
    def set_output(self, *args, **kwargs):
        return self
    
class CategoryEncoder(BaseEstimator,TransformerMixin):
    def __init__(self):
        self.type_column = ['main_category']
    def fit(self,X,y=None):
        return self
    def transform(self,X):
        X=pd.get_dummies(X, columns=self.type_column).astype(int)
        return X
