import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.preprocessing
from sklearn.preprocessing import StandardScaler, LabelEncoder, QuantileTransformer
from sklearn.model_selection import train_test_split
import numpy as np
from scipy import stats
import env

# connection function for accessing mysql 
def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def acquire(df):
    '''
    This function connects to Codeup's SQL Server using given parameters in the user's
    env file.  It then acquires data from Zillow's database using a SQL query that
    selects ten specific features from the 2017 properties and predictions tables. 
    The query limits transaction dates to May - August, 2017. It specific property 
    use types to represent single unit properties and controls for outliers on
    square footage, bathroom and bedroom counts, and zip codes. Observations 
    with null values in key columns are not pulled in.    
    '''
    
    def get_connection(db, user=env.user, host=env.host, password=env.password):
         return f'mysql+pymysql://{user}:{password}@{host}/{db}'
    query = '''
            SELECT bathroomcnt, 
                    bedroomcnt, 
                    yearbuilt, 
                    calculatedfinishedsquarefeet, 
                    lotsizesquarefeet, 
                    parcelid, 
                    fips, 
                    regionidzip, 
                    taxvaluedollarcnt, 
                    taxamount
            FROM properties_2017
            JOIN predictions_2017 using(parcelid)
            WHERE (transactiondate between "2017-05-01" and "2017-08-31")
            AND ((propertylandusetypeid IN (261, 262, 264, 273, 274, 276, 279)) or (unitcnt = 1))
            AND (calculatedfinishedsquarefeet >= 700)
            AND (calculatedfinishedsquarefeet <= 5500)
            AND (taxvaluedollarcnt <= 3100000)
            AND (taxvaluedollarcnt >= 90000)
            AND (bedroomcnt > 0)
            AND (bedroomcnt < 8)
            AND (bathroomcnt > 0)
            AND (bathroomcnt < 7)
            AND (regionidzip <= 99999)
            AND (yearbuilt IS NOT NULL)
            AND (calculatedfinishedsquarefeet IS NOT NULL)
            AND (lotsizesquarefeet IS NOT NULL)
            AND (taxvaluedollarcnt IS NOT NULL)
            AND (taxamount IS NOT NULL)
            AND (regionidzip IS NOT NULL)
           
            '''

    df = pd.read_sql(query, get_connection('zillow'))
    return df


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def prep_zillow(df):
    '''
    This function will take in the acquired zillow database and clean data by: renaming columns, 
    reseting the index to parcel_id, converting the year built feature to age in years, convert
    data types as needed.
    
    '''
    # rename columns
    df = df.rename(columns={"bedroomcnt": "bedrooms", 
                             "bathroomcnt": "bathrooms", 
                             "calculatedfinishedsquarefeet":"square_feet", 
                             "lotsizesquarefeet":"lot_size",
                             "taxamount": "taxes",
                             "taxvaluedollarcnt": "tax_value", 
                             "parcelid":"parcel_id",
                             "buildingqualitytypeid":"building_quality",
                             "regionidcounty":"county",
                             "regionidzip":"zip_code",
                             "yearbuilt":"age"})
                        
    #reset index to parcel_id
    df = df.set_index('parcel_id')
          
    #convert year built to age in years
    df.age = 2017 - df.age

    # Change datatypes
    df.bathrooms = df.bathrooms.astype('int64')
    df.bedrooms = df.bedrooms.astype('int64')
    df.age = df.age.astype('int64')
    df.square_feet = df.square_feet.astype('int64')
    df.fips = df.fips.astype('int64') 
    df.zip_code = df.zip_code.astype('int64')
    return df
     

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   
def train_validate_test_split(df, target, seed=123):
    
    '''
    This function takes in (df, target, seed = 123) and splits the data into separate
    X_ and y_ train, validate and test data sets 
    
    '''
    train_and_validate, test = train_test_split(
        df, test_size=0.2, random_state=seed)
    train, validate = train_test_split(
        train_and_validate,
        test_size=0.3,
        random_state=seed)
    
    # split train into X (dataframe, drop target) & y (series, keep target only)
    X_train = train.drop(columns=[target])
    y_train = train[target]
    
    # split validate into X (dataframe, drop target) & y (series, keep target only)
    X_validate = validate.drop(columns=[target])
    y_validate = validate[target]
    
    # split test into X (dataframe, drop target) & y (series, keep target only)
    X_test = test.drop(columns=[target])
    y_test = test[target]

    return X_train, X_validate, X_test, y_train, y_validate, y_test


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def min_max_scale(X_train, X_validate, X_test, numeric_cols):
    '''
    this function takes in 3 dataframes with the same columns, 
    a list of numeric column names (because the scaler can only work with numeric columns),
    and fits a min-max scaler to the first dataframe and transforms all
    3 dataframes using that scaler. 
    it returns 3 dataframes with the same column names and scaled values. 
    '''
    # create the scaler object and fit it to X_train (i.e. identify min and max)
    # if copy = false, inplace row normalization happens and avoids a copy (if the input is already a numpy array).


    scaler = sklearn.preprocessing.MinMaxScaler(copy=True).fit(X_train[numeric_cols])

    #scale X_train, X_validate, X_test using the mins and maxes stored in the scaler derived from X_train. 
    # 
    X_train_scaled_array = scaler.transform(X_train[numeric_cols])
    X_validate_scaled_array = scaler.transform(X_validate[numeric_cols])
    X_test_scaled_array = scaler.transform(X_test[numeric_cols])

    # convert arrays to dataframes
    X_train_scaled = pd.DataFrame(X_train_scaled_array, 
                                  columns=numeric_cols).\
                                  set_index([X_train.index.values])

    X_validate_scaled = pd.DataFrame(X_validate_scaled_array, 
                                     columns=numeric_cols).\
                                     set_index([X_validate.index.values])

    X_test_scaled = pd.DataFrame(X_test_scaled_array, 
                                 columns=numeric_cols).\
                                 set_index([X_test.index.values])

    
    return X_train_scaled, X_validate_scaled, X_test_scaled

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def remove_tax_value_outliers(df):
    '''
    This function removes outliers in tax values in the Zillow data to prepare the data to 
    for calculating the distribution of tax rates in Orange County, Ventura County, and Los
    Angeles County, California.
    '''
    
    # Calculate the interquartile range for your column

    q1, q3 = df.tax_value.quantile([.25, .75])
    
    iqr = q3 - q1
    
    # Create variables holding upper and lower cutoff values using common formula. Tweak as you like.
    
    tax_upperbound = q3 + 3.5 * iqr
    
    #tax_lowerbound = q1 - 3 * iqr ==> The lowerbound is negative and since there are no negative values, 
    # there are no lowerbound outliers
    
    # Filter the column using variables and reassign to your dataframe.
    tax_dist_a = tax_dist[tax_dist.tax_value < tax_upperbound]
    return tax_dist_a