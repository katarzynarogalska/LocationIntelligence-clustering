from sklearn.base import BaseEstimator, TransformerMixin
import re
from sklearn.preprocessing import Normalizer

#transformer to delete rows with missing latitude and longitude
class MissingGeographRemover(BaseEstimator,TransformerMixin ): 
    def __init__(self):
        self.columns=['latitude','longitude']

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        return X.dropna(subset=self.columns)
    

#transformer to create new binary columns from Phone and website   
class ContactKnownAdder(BaseEstimator, TransformerMixin): 
    def __init__(self):
        pass
    def fit(self,X,y=None):
        return self
    def transform(self,X):
        X['Website_known'] = X['website'].apply(lambda x: 0 if x.lower()=='uknown' else 1)
        X['Phone_known'] = X['phone_number'].apply(lambda x: 0 if x.lower()=='uknown' else 1)
        return X
    def set_output(self, *args, **kwargs):
        return self

#transformer to classify types 
class ClassifyType(BaseEstimator, TransformerMixin): 
    def __init__(self):
        self.main_categories = ["Hotel","Restaurant","Shop","Service","Agency","Dealer","Repair","Car","Travel","Fitness","Health","Dental","RealEstate",
    "Office","Tourist","Attraction","Park","Attorney","Bank","Pharmacy","Supermarket","Bakery","Barbershop","Hospital","Library","Museum","Cinema",
    "Store","Jeweler","Beauty"]
    def fit(self, X, y=None):
        return self
    def transform(self,X):
        def classify(text):
            for category in self.main_categories:
                if re.search(category, text, re.IGNORECASE):
                    return category
            return 'Other'
        X['main_category'] = X['types'].apply(classify)
        return X
    def set_output(self, *args, **kwargs):
        return self
    
#transformer to delete irrelevant columns
class IrrelevantColumnRemover(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.irrelevant_columns = ['business_id','phone_number','full_address','website','country','city','place_id','place_link', 'types', 'timezone','state', 'geo_cluster' ]
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        X = X.drop(columns = self.irrelevant_columns)
        return X
    def set_output(self, *args, **kwargs):
        return self
    

#transformer to Normalize numerical columns
class NumericalNormalizer(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.numerical_cols= ['review_count','rating']
        self.scaler = Normalizer()

    def fit(self,X, y=None):
        self.scaler.fit(X[self.numerical_cols])
        return self
    def transform(self,X):
        X[self.numerical_cols] = self.scaler.transform(X[self.numerical_cols])
        return X
    def set_output(self, *args, **kwargs):
        return self
