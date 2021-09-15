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
| `bathroomcnt`                  |  Number of bathrooms in home including fractional bathrooms                                                            |   float     |   Used in model    |
| `bedroomcnt`                   |  Number of bedrooms in home                                                                                            |   int     |   Used in model    |
| `calculatedfinishedsquarefeet` |  Calculated total finished living area of the home                                                                     |     int      |   Used in model    |
| `fips`                         |  Federal Information Processing Standard code -  see https://en.wikipedia.org/wiki/FIPS\_county\_code for more details |     string      |   Used in model    |
| `propertylandusetypeid`        |  Type of land use the property is zoned for                                                                            |      int     |    Used to filter properties from database   |
| `yearbuilt`                    |  The Year the principal residence was built                                                                            |       int    |    Used in model   |
| `taxamount`                    | The total property tax assessed for that assessment year                                                               |      float     |    Used to calculate tax rates by county   |

---
| Target | Definition | Data Type | Notes |
| ----- | ----- | ----- | ----- |
| `taxvaluedollarcnt` | The total tax assessed value of the parcel| float | Value being predicted |

#### Initial, Informal Hypotheses
> - Number of bathrooms, location (county), and total square footage will be most related to appraised value
> - Average assessed value will vary by county

#### Formal Hypotheses

>  **Hypotheses (Correlation Tests):**
> - alpha = .05

> Null Hypotheses:
> 1. H_0: There is no linear relationship between appraised value and bedroom_cnt
> 2. H_0: There is no linear relationship between appraised value and bathroom_cnt
> 3. H_0: There is no linear relationship between appraised value and sqft
> 4. H_0: There is no linear relationship between appraised value and year_built 

> Alternative Hypotheses:
> 1. H_a: There is a linear relationship between appraised value and bedroom_cnt
> 2. H_a: There is a linear relationship between appraised value and bathroom_cnt
> 3. H_a: There is a linear relationship between appraised value and sqft
> 4. H_a: There is a linear relationship between appraised value and year_built 

> **Conclusions:**
> 1. We reject the null hypothesis since there is a evidence of a linear relationship between appraised_value and bedroom_cnt since p < alpha
> 2. We reject the null hypothesis since there is a evidence of a linear relationship between appraised_value and bathroom_cnt since p < alpha
> 3. We reject the null hypothesis since there is a evidence of a linear relationship between appraised_value and sqft since p < alpha
> 4. We reject the null hypothesis since there is a evidence of a linear relationship between appraised_value and year_built since p < alpha


> **Hypotheses (Mann-Whitney Tests):** 
> - alpha = .05

> Null Hypotheses:
> 1. H_0: there is no difference in appraised_value for houses in LA County and Orange County
> 2. H_0: there is no difference in appraised_value for houses in LA County and Ventura County
> 3. H_0: there is no difference in appraised_value for houses in Orange County and Ventura County 

> Alternative Hypotheses:
> 1. H_a: there is a difference in appraised_value for houses in LA County and Orange County
> 2. H_a: there is a difference in appraised_value for houses in LA County and Ventura County
> 3. H_a: there is a difference in appraised_value for houses in Orange County and Ventura County

> **Conclusions:**
> 1. We reject the null, there is evidence of a difference in appraised_value for houses in LA County and Orange County since p < 0.05
> 1. We reject the null, there is evidence of a difference in appraised_value for houses in LA County and Ventura County since p < 0.05
> 1. We reject the null, there is evidence of a difference in appraised_value for houses in Orange County and Ventura County since p < 0.05

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Executive Summary - Conclusions & Next Steps

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

> **Conclusions:**
> - Best predictors discovered were county, number of bedrooms, number of bathrooms, and square footage
> - Best-peforming model outperformed baseline and increased R^2 value by 20%

> **Next Steps:**
> - Improve model performance by adding additional, more predictive features to the model
>> - ZIP code
>> - Neighborhood
>> - Garage count
>> - Pool info
>> - Etc.

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
> - Import the acquire function from the wrangle.py module and use it to acquire the data in the Final Report Notebook.
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
- [ ] Download the wrangle.py, evaluate.py, explore.py, and final_report.ipynb files into your working directory
- [ ] Add your own env file to your directory. (user, password, host)
- [ ] Run the final_report.ipynb notebook