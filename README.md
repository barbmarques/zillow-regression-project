# zillow-regression-project
Regression Project: Estimating Home Value


#### Project Summary:

The Zestimate’s accuracy depends on location and the availability of data in an area. Some areas have more detailed home information available — such as square footage and number of bedrooms or bathrooms — and other areas do not. The more data available, the more accurate the Zestimate value will be.  The Zillow Data Science Team wants to be able to predict the values of single unit properties that the taxdistrict assesses using the property data from transactions during May and June 2017. 

Data Source: Zillow database on Codeup's data server.

#### Project Goals:
- Predict the values of single unit properties that that the tax district assess based on data of property transaction in May through June 2017. 
- Find the states and counties the properties are located in.
- Calculate the distribution of tax rates for each county. 


### Factors contributing to tax value include:
- 

#### Recommendation:


To view the requested information: download ```predicted_values.csv```. 

All files referenced in this presentation are available in the github repository for this project:   https://github.com/barbmarques/zillow-regression-project.


#### Progression through the Data Science Pipeline: 
Each step in the our process is recorded and staged on a Trello board at: https://trello.com/b/vOXbVcbl

Plan:
- Set up GitHub repo, readme, env.
- Use Sequel to investigate the database and compose an appropriate query
- Brainstorm a list of questions and form hypotheses about how variables might impact one another. 

Acquire: 
- Read data from Zillow’s own database located on Codeup’s SQL Server into a Pandas dataframe to be analyzed using Python.
- Created a function, acquire.py, as a reproducible component for acquiring necessary data

Prepare:
- Carefully reviewed data, identifying any missing, erroneous, or invalid values. 
- Explored value counts of the dataframe and visualized univariate data 
- Data was scaled as necessary.
- Data was split into train, validate and test sets, and ready for analysis/modeling.
- Created a function, prep.py, as a reproducible component that cleans/prepares data for analysis and modeling by: handling missing values, adjusts data types, handles any data integrity and scales data, as necessary.

Explore:
- Visualize all combination of variables to explore relationships.
- Developed hypotheses and ran statistical tests: t-test and correlation, to accept or reject null hypotheses.
- Tested for independent variables that correlate with tax value.
- Summarized takeaways and conclusions.

Model: 
- Developed a model that established baseline.
- Developed a regression model that performs better than the baseline
- Documented algorithms and hyperparameters used.
- Plotted the residuals and documented evaluation metrics (SSE, RMSE, or MSE).
- Plotted y by y-hat
- Created model.py as a reproducible component, containing functions to fit, predict and evaluate the final model on the test data set. 


#### Instructions for Reproducing Our Findings:

1.  Download the following files from https://github.com/barbmarques/zillow-regression-project to your working directory:  
 - Zillow.ipynb
 

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



