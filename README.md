# zillow-regression-project
Regression Project: Estimating Home Value


#### Project Summary:

The Zillow Data Science Team wants to be able to predict the values of single unit properties that the tax district assesses based on their data based on property transactions during May through August 2017. Properties are all located in Los Angeles County, Orange County or Ventura County, California

Data Source: Zillow database on Codeup's data server.

All files referenced in this presentation are available in the github repository for this project:   https://github.com/barbmarques/zillow-regression-project.

#### Project Goals:
- Predict the tax value of single unit properties in the Ventura County, Los Angeles County and Orange County, California. 
- Determine the distribution of tax rates for each county. 

#### Initial Questions: 
- Does the lot size affect the value of the house?
- Does the county a home is located in affect the value of the home?
- Does the age of a home affect the value of the home?

#### Hypotheses:

- H$_{0}$: There is no relationship between the county is located in and its tax value. 

  H$_{a}$: There is a dependent relationship between county and tax value.  
  <font color = 'red'> Reject the null hypothesis that there is no relationship between county and tax value.<font color = 'black'>
    

- H$_{0}$: There is no difference between the mean tax value of a home that is over 30 years old and one that is under 30. 
  
  H$_{a}$: There is a difference in mean tax value of a home based on its age.  
  <font color = 'red'>Reject the null hypothesis that there is no difference in tax value of a home based on an age over 30 years.<font color = 'black'>

#### Recommendation & Takeaways:

- Recommend using a Polynomial Regression Model (degree of 2) to predict home values based on bathroom count, age of home, square footage and zip code.
- Note: Scatterplot visualization demonstrates that our model tends to under-value homes that exceed the median tax value of ~$408,000.
- Primary Drivers of Tax Value include: square footage, bedroom and bathroom count, age of home, and zip code in which home is located.

#### Given more Time and Resources, I would:

- Fine tune feature engineering, perhaps combining some features, to increase accuracy.
- Since there was little difference in the RMSE for mean and median, I would re-run models using median as baseline. 
- Reconfigure many of my explorations and modeling code into functions, to clean up notebook and increase reproducibility of results.





#### Progression through the Data Science Pipeline: 
``` PLAN -> ACQUIRE -> PREPARE -> EXPLORE -> MODEL -> DELIVER ```

Each step in the process is recorded and staged on a Trello board at: https://trello.com/b/l8KSm6ZM

```Plan:```
- Set up GitHub repo, readme, env.
- Use Sequel to investigate the database and compose an appropriate query
- Brainstorm a list of questions and form hypotheses about how variables might impact one another. 

```Acquire:```
- Read data from Zillow’s own database located on Codeup’s SQL Server into a Pandas dataframe to be analyzed using Python.
- Created a function, ```acquire(df)```, as a reproducible component for acquiring necessary data.

```Prepare:```
- Carefully reviewed data, identifying any missing, erroneous, or invalid values. 
- Explored value counts of the dataframe and visualized distribution of univariate data 
- Created and called a function, ```prep_zillow```, as a reproducible component that cleans/prepares data for analysis by: renames columns, handling missing values, adjusts data types, handles any data integrity
- Created and called a function, ```train_validate_test_split```, that splits the data into train, validate and test sets.
- Numeric data was scaled using MinMax scaler.
- Created a module ```wrangle_zillow.py``` which stores code for functions that acquire and prepare data.

```Explore:```
- Visualize all combination of variables to explore relationships.
- Tested for independent variables that correlate with tax value.
- Created a module, ```explore.py```, which stores code for functions to explore data.
- Developed hypotheses and ran statistical tests: t-test and correlation, to accept or reject null hypotheses.
- Summarized takeaways and conclusions.

```Model:``` 
- Developed a baseline model.
- Developed a regression model that performs better than the baseline
- Documented algorithms and hyperparameters used.
- Plotted the residuals and documented evaluation metrics (SSE, RMSE, or MSE).

```Deliver:```
- Clearly documented all code in a reproducible Jupyter notebook called Zillow_Regression_Project.
- Created a Google slide presentation that can be shared with Zillow management.

#### Instructions for Reproducing My Findings:

1.  Start by cloning the github repository on your From your terminal command line, type git clone git@github.com:barbmarques/zillow-regression-project.git

2.  Download the following files from https://github.com/barbmarques/zillow-regression-project to your working directory:  
 - Zillow_Regression Project.ipynb
 - wrangle_zillow.py
 - explore.py
  
3.  You will also need you a copy of your personal env file in your working directory:
 - This should contain your access information (host, user, password) to access Codeup's database in MySQL

4. Run the Jupyter notebook, Zillow_Regression_Project, cell by cell, to reproduce my analysis.

4. To access the property value predictions in a csv format, download ```property_value_predictions
.csv```. 


#### Data Dictionary of Variables Used in Analysis

| Attribute | Definition | Data Type |
| ----- | ----- | ----- |
| **tax_value**| The 2017 total tax assessed value of the parcel | int64 |
|parcel_id| Unique identifier for parcels (lots) | object |
|bathrooms| Number of bathrooms in home, including fractional bathrooms | int64 |
|square_feet|Calculated total finished living area of the home| int64|
|bedrooms|Number of bedrooms in home| int64 |
|lot_size|Area of the lot in square feet| int64 |
|zip_code| Zip code in which the home is located| int64 |
|fips|Federal Information Processing Standard Code. This code identifies the county in which the home is located. 6037: Los Angeles County, 6059: Orange County, 6111: Ventura County|int64 |
|age|Number of years from original construction until the home sold in 2017.| int64 | 
|taxes|The total property tax assessed for the assessment year|float64|
|tax rate| Calculated based on taxed amount and assessed value of home |float64|

