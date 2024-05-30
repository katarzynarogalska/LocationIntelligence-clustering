from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder


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
        self.encoder = OneHotEncoder(sparse=False)
    def fit(self,X,y=None):
        self.encoder.fit(X[self.type_column])
        return self
    def transform(self,X):
        types_encoded = self.encoder.transform(X[self.type_column])
        df_encoded = pd.DataFrame(types_encoded, columns=self.encoder.get_feature_names_out(self.type_column))
        X = pd.concat([X, df_encoded], axis=1).drop(columns=self.type_column)
        return X
    def set_output(self, *args, **kwargs):
        return self
    
class BooleanToNumericEncoder(BaseEstimator,TransformerMixin):
    def __init__(self):
        self.boolean_column = 'verified'
    def fit(self,X,y=None):
        return self
    def transform(self,X):
        X[self.boolean_column] = X[self.boolean_column].apply(lambda x: 1 if x else 0)
        return X
    def set_output(self, *args, **kwargs):
        return self
    
class SecondStandardizer(BaseEstimator,TransformerMixin):
    def __init__(self):
        self.scaler = StandardScaler()

    def fit(self, X, y=None):
        self.scaler.fit(X)
        return self

    def transform(self, X):
        scaled_data = self.scaler.transform(X)
        return scaled_data
    def set_output(self, *args, **kwargs):
        return self

    



