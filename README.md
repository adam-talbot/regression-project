# Zillow Regression Project

<img src="https://1000logos.net/wp-content/uploads/2017/12/Zillow_logo_PNG2.png" alt="Zillow" title="Zillow Logo" width="400" height="200" />

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Project Summary

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

#### Project Objectives
> - Document code, process (data acquistion, preparation, exploratory data analysis and statistical testing, modeling, and model evaluation), findings, and key takeaways in a Jupyter Notebook report
> - Create modules (acquire.py, prepare.py) that make my process repeateable
> - Construct a model to predict tax assessed home values using regression techniques
> - Deliver a 5-minute, audience-appropriate presentation consisting of a high-level walkthrough using slides
> - Answer panel questions about your code, process, findings and key takeaways, and model

#### Business Goals
> - Find drivers of tax assessed home values
> - Construct a ML regression model that accurately predicts tax assessed home values
> - Document process well enough to be presented or read like a report

#### Audience
> - The Zillow Data Science team

#### Project Deliverables
> - A verbal report in the form of a presentation, supported by slides (5 minutes max)
> - A Jupyter Notebook Report showing process and analysis with the goal of finding drivers for tax assessed home values
> - A README.md file containing the project description with goals, initial hypotheses, a data dictionary, project planning, instructions or an explanation of how someone else can recreate your project and findings, answers to your hypotheses, key findings, recommendations, and takeaways from your project 
> - Individual modules, .py files, that hold your functions to acquire and prepare your data

#### Project Context
> - The Zillow dataset I'm using came from the Codeup database.


#### Data Dictionary

---
| Feature                        | Description                                                                                                            | Data Type | Notes |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------- | --------- | ----- |
| 'airconditioningtypeid'        |  Type of cooling system present in the home (if any)                                                                   |           |       |
| 'architecturalstyletypeid'     |  Architectural style of the home (i.e. ranch, colonial, split-level, etc…)                                             |           |       |
| 'basementsqft'                 |  Finished living area below or partially below ground level                                                            |           |       |
| 'bathroomcnt'                  |  Number of bathrooms in home including fractional bathrooms                                                            |           |       |
| 'bedroomcnt'                   |  Number of bedrooms in home                                                                                            |           |       |
| 'buildingqualitytypeid'        |  Overall assessment of condition of the building from best (lowest) to worst (highest)                                 |           |       |
| 'buildingclasstypeid'          | The building framing type (steel frame, wood frame, concrete/brick)                                                    |           |       |
| 'calculatedbathnbr'            |  Number of bathrooms in home including fractional bathroom                                                             |           |       |
| 'decktypeid'                   | Type of deck (if any) present on parcel                                                                                |           |       |
| 'threequarterbathnbr'          |  Number of 3/4 bathrooms in house (shower + sink + toilet)                                                             |           |       |
| 'finishedfloor1squarefeet'     |  Size of the finished living area on the first (entry) floor of the home                                               |           |       |
| 'calculatedfinishedsquarefeet' |  Calculated total finished living area of the home                                                                     |           |       |
| 'finishedsquarefeet6'          | Base unfinished and finished area                                                                                      |           |       |
| 'finishedsquarefeet12'         | Finished living area                                                                                                   |           |       |
| 'finishedsquarefeet13'         | Perimeter  living area                                                                                                 |           |       |
| 'finishedsquarefeet15'         | Total area                                                                                                             |           |       |
| 'finishedsquarefeet50'         |  Size of the finished living area on the first (entry) floor of the home                                               |           |       |
| 'fips'                         |  Federal Information Processing Standard code -  see https://en.wikipedia.org/wiki/FIPS\_county\_code for more details |           |       |
| 'fireplacecnt'                 |  Number of fireplaces in a home (if any)                                                                               |           |       |
| 'fireplaceflag'                |  Is a fireplace present in this home                                                                                   |           |       |
| 'fullbathcnt'                  |  Number of full bathrooms (sink, shower + bathtub, and toilet) present in home                                         |           |       |
| 'garagecarcnt'                 |  Total number of garages on the lot including an attached garage                                                       |           |       |
| 'garagetotalsqft'              |  Total number of square feet of all garages on lot including an attached garage                                        |           |       |
| 'hashottuborspa'               |  Does the home have a hot tub or spa                                                                                   |           |       |
| 'heatingorsystemtypeid'        |  Type of home heating system                                                                                           |           |       |
| 'latitude'                     |  Latitude of the middle of the parcel multiplied by 10e6                                                               |           |       |
| 'longitude'                    |  Longitude of the middle of the parcel multiplied by 10e6                                                              |           |       |
| 'lotsizesquarefeet'            |  Area of the lot in square feet                                                                                        |           |       |
| 'numberofstories'              |  Number of stories or levels the home has                                                                              |           |       |
| 'parcelid'                     |  Unique identifier for parcels (lots)                                                                                  |           |       |
| 'poolcnt'                      |  Number of pools on the lot (if any)                                                                                   |           |       |
| 'poolsizesum'                  |  Total square footage of all pools on property                                                                         |           |       |
| 'pooltypeid10'                 |  Spa or Hot Tub                                                                                                        |           |       |
| 'pooltypeid2'                  |  Pool with Spa/Hot Tub                                                                                                 |           |       |
| 'pooltypeid7'                  |  Pool without hot tub                                                                                                  |           |       |
| 'propertycountylandusecode'    |  County land use code i.e. it's zoning at the county level                                                             |           |       |
| 'propertylandusetypeid'        |  Type of land use the property is zoned for                                                                            |           |       |
| 'propertyzoningdesc'           |  Description of the allowed land uses (zoning) for that property                                                       |           |       |
| 'rawcensustractandblock'       |  Census tract and block ID combined - also contains blockgroup assignment by extension                                 |           |       |
| 'censustractandblock'          |  Census tract and block ID combined - also contains blockgroup assignment by extension                                 |           |       |
| 'regionidcounty'               | County in which the property is located                                                                                |           |       |
| 'regionidcity'                 |  City in which the property is located (if any)                                                                        |           |       |
| 'regionidzip'                  |  Zip code in which the property is located                                                                             |           |       |
| 'regionidneighborhood'         | Neighborhood in which the property is located                                                                          |           |       |
| 'roomcnt'                      |  Total number of rooms in the principal residence                                                                      |           |       |
| 'storytypeid'                  |  Type of floors in a multi-story house (i.e. basement and main level, split-level, attic, etc.).  See tab for details. |           |       |
| 'typeconstructiontypeid'       |  What type of construction material was used to construct the home                                                     |           |       |
| 'unitcnt'                      |  Number of units the structure is built into (i.e. 2 = duplex, 3 = triplex, etc...)                                    |           |       |
| 'yardbuildingsqft17'           | Patio in  yard                                                                                                         |           |       |
| 'yardbuildingsqft26'           | Storage shed/building in yard                                                                                          |           |       |
| 'yearbuilt'                    |  The Year the principal residence was built                                                                            |           |       |
| 'taxvaluedollarcnt'            | The total tax assessed value of the parcel                                                                             |           |       |
| 'structuretaxvaluedollarcnt'   | The assessed value of the built structure on the parcel                                                                |           |       |
| 'landtaxvaluedollarcnt'        | The assessed value of the land area of the parcel                                                                      |           |       |
| 'taxamount'                    | The total property tax assessed for that assessment year                                                               |           |       |
| 'assessmentyear'               | The year of the property tax assessment                                                                                |           |       |
| 'taxdelinquencyflag'           | Property taxes for this parcel are past due as of 2015                                                                 |           |       |
| 'taxdelinquencyyear'           | Year for which the unpaid propert taxes were due                                                                       |           |       |

---
| Target | Definition | Data Type | Notes |
| ----- | ----- | ----- | ----- |
| 'taxvaluedollarcnt' | The total tax assessed value of the parcel| float |  |

#### Initial, Informal Hypotheses
> - Some categorical variables will be related to the target (I can test this with the Chi-Square Test)
>> - Those that are related should be used in model, those that aren't, shouldn't be used
> - 

#### Formal Hypotheses

>  **Hypotheses (Categorical Variables):**
> - alpha = .05

> Null Hypotheses:
> 1. H_0: 

> Alternative Hypotheses:
> 1. H_a: 

> **Conclusions:**
> 1. 


>  **Hypotheses (Quantitative Variables):** 
> - alpha = .05

> Null Hypotheses:
> 1. H_0: 

> Alternative Hypotheses:
> 1. H_a: 

> **Conclusions:**
> 1. 

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Executive Summary - Conclusions & Next Steps

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

> **Conclusions:**
> - 

> **Next Steps:**
> - 

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Pipeline Stages Breakdown

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

##### ***Plan***
- [x] Create README.md with data dictionary, project and business goals, come up with initial hypotheses.
- [x] Acquire data from the Codeup Database and create a function to automate this process. Save the function in an acquire.py file to import into the Final Report Notebook.
- [x] Clean and prepare data for the first iteration through the pipeline, MVP preparation. Create a function to automate the process, store the function in a prepare.py module, and prepare data in Final Report Notebook by importing and using the funtion.
- [x] Clearly define at least two hypotheses, set an alpha, run the statistical tests needed, reject or fail to reject the Null Hypothesis, and document findings and takeaways.
- [x] Establish a baseline accuracy and document well.
- [x] Train various different regression models.
- [x] Evaluate models on train and validate datasets.
- [x] Choose the model with that performs the best and evaluate that single model on the test dataset.
- [x] Document conclusions, takeaways, and next steps in the Final Report Notebook.

___

##### Plan -> ***Acquire***
> - Store functions that are needed to acquire data from the database on the Codeup data science database server; make sure the acquire.py module contains the necessary imports to run my code.
> - The final function will return a pandas DataFrame.
> - Import the acquire function from the acquire.py module and use it to acquire the data in the Final Report Notebook.
> - Complete some initial data summarization (`.info()`, `.describe()`, `.value_counts()`, ...).
___

##### Plan -> Acquire -> ***Prepare***
> - Store functions needed to prepare the data; make sure the module contains the necessary imports to run the code. The final function should do the following:
>> - Split the data into train/validate/test.
>> - Handle any missing values.
>> - Handle erroneous data and/or outliers that need addressing.
>> - Encode variables as needed.
> - Import the prepare function from the prepare.py module and use it to prepare the data in the Final Report Notebook.
> - Plot distributions of individual variables.
> - Add data dictionary to notebook that defines fields that will be used in your model and analysis
> - Identify unit measures and decide how to best scale any numeric data
___

##### Plan -> Acquire -> Prepare -> ***Explore***
> - Answer key questions, my hypotheses, and figure out the features that can be used in a regression model to best predict the target variable. 
> - Run at least 2 statistical tests in data exploration. Document my hypotheses, set an alpha before running the tests, and document the findings well.
> - Create visualizations and run statistical tests that work toward discovering variable relationships (independent with independent and independent with dependent). 
> - Summarize my conclusions, provide clear answers to my specific questions, and summarize any takeaways/action plan from the work above.
___

##### Plan -> Acquire -> Prepare -> Explore -> ***Model***
> - Establish a baseline accuracy to determine if having a model is better than no model and train and compare at least 3 different models. Document these steps well.
> - Train (fit, transform, evaluate) multiple models, varying the algorithm and/or hyperparameters you use.
> - Compare evaluation metrics across all the models you train and select the ones you want to evaluate using your validate dataframe.
> - Feature Selection (after initial iteration through pipeline): Are there any variables that seem to provide limited to no additional information? If so, remove them.
> - Based on the evaluation of the models using the train and validate datasets, choose the best model to try with the test data, once.
> - Test the final model on the out-of-sample data (the testing dataset), summarize the performance, interpret and document the results.
___

##### Plan -> Acquire -> Prepare -> Explore -> Model -> ***Deliver***
> - Introduce myself and my project goals at the very beginning of my presentation.
> - Summarize my findings at the beginning like I would for an Executive Summary.
> - Walk Zillow Data Science Team through the analysis I did to answer my questions and that lead to my findings. (Visualize relationships and Document takeaways.) 
> - Clearly call out the questions and answers I am analyzing as well as offer insights and recommendations based on my findings.
> - Finish with key takeaways, recommendations, and next steps and be prepared to answer questions from the data science team about your project.

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Reproduce My Project

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

You will need your own env file with database credentials along with all the necessary files listed below to run my final project notebook. 
- [x] Read this README.md
- [ ] Download the aquire.py, prepare.py, explore.py, and final_report.ipynb files into your working directory
- [ ] Add your own env file to your directory. (user, password, host)
- [ ] Run the final_report.ipynb notebook