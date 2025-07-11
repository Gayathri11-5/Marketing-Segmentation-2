from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
import pandas as pd
def preprocess_data(data):
    data=data.copy()
    for col in data.columns:
        if 'ID' in col:
            data.drop(col,axis=1,inplace=True)

    if 'Dt_Customer' in data.columns:
        data['Dt_Customer']=pd.to_datetime(data['Dt_Customer'],errors='coerce')
        data['Customer_Since_now']=(pd.Timestamp('today')-data['Dt_Customer']).dt.days
        data.drop('Dt_Customer',axis=1,inplace=True)

    if 'Year_Birth' in data.columns:
        data["age"]=2025-data["Year_Birth"]
        data.drop(["Year_Birth"],axis=1,inplace=True)

    spent_products=['MntWines',	'MntFruits',	'MntMeatProducts',	'MntFishProducts',	'MntSweetProducts'	,'MntGoldProds']
    if all(col in data.columns for col in spent_products):
        data["spent"]=data[spent_products].sum(axis=1)
    numeric_cols=data.select_dtypes(include=['int64','float64']).columns
    if len(numeric_cols)>0:
        imputer=SimpleImputer(strategy='median')
        data[numeric_cols]=imputer.fit_transform(data[numeric_cols])
    else:
        raise ValueError("No numeric columns found")
    categorical_cols=data.select_dtypes(include=['object']).columns
    data=pd.get_dummies(data,columns=categorical_cols,drop_first=True)
    scaler=StandardScaler()
    scaled_array=scaler.fit_transform(data[numeric_cols])
    return data,scaled_array
