# zillow-regression-project
Regression Project: Estimating Home Value


#### Project Summary:

The Zillow Data Science Team wants to be able to predict the values of single unit properties that the taxdistrict assesses using the property data from transactions during May and June 2017. 

Data Source: Zillow database on Codeup's data server.

#### Project Goals:
- Predict the values of single unit properties that that the tax district assess based on data of property transaction in May through June 2017. 
- Find the states and counties the properties are located in.
- Calculate the distribution of tax rates for each county. 

#### Using a ____ Model, :
-

####Factors are contributing to tax value include:
- 

#### Recommendation:


To view the requested information: download ```predicted_values.csv```. 

All files referenced in this presentation are available in the github repository for this project:   https://github.com/barbmarques/zillow-regression-project.


#### Process/Data Science Pipeline:
Each step in the our process is recorded and staged on a Trello board at: https://trello.com/b/vOXbVcbl


#### Instructions for Reproducing Our Findings:

1.  Download the following files from https://github.com/barbmarques/zillow-regression-project to your working directory:  
 - 
 

2.  You will also need you a copy of your personal env file in your working directory:
 - This should contain your access information (host, user, password) to access Codeup's database in MySQL

3. Run the Jupyter notebook, cell by cell, allowing time for visualizations to generate.

4. To access the property value predictions in a csv format, download ```property_value_predictions
.csv```. 


#### Data Dictionary of Variables Used in Analysis

| Attribute | Definition | Data Type |
| ----- | ----- | ----- |
| **tax_value**| The total tax assessed value of the parcel | int64 |
|parcel_id| Unique identifier for parcels (lots) | object |
|bathrooms| Number of bathrooms in home, including fractional bathrooms | int64 |
|square_feet|Calculated total finished living area of the home||
|bedrooms|Number of bedrooms in home| int64 |
|lot_size|Area of the lot in square feet| int64 |
|zip_code| Zip code in which the home is located| float64 |
|county| County in which the home is located | |
|yearbuilt|The year the principal residence was built| float64 | 
|taxes|The total property tax assessed for the assessment year||
|assessmentyear|The year of the property tax assessment||
|building_quality|Overall assessment of condition of the building from best (lowest) to worst (highest)||



