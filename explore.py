import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_selection import SelectKBest, f_regression, RFE
from sklearn.linear_model import LinearRegression

def plot_variable_pairs(df):
    '''
    Takes in df and returns reg pairplot
    '''
    sns.pairplot(data=df, kind='reg', plot_kws={'line_kws':{'color':'black'}});
    
def plot_variable_pairs_cat_hue(df):
    '''
    Takes in df and returns pairplot with hue for each categorical variable with dtype of string
    '''
    cat_cols = df.select_dtypes('string').columns.tolist()
    for cat in cat_cols:
        sns.pairplot(data=df, hue=cat);
        
def plot_categorical_and_continuous_vars(df):
    '''
    Takes in df and returns barplot, swarmplot, stripplot, boxplot, boxenplot, and violin plot for each combination of categorical
    and numerical variables
    '''
    num_cols = df.select_dtypes('number').columns.tolist()
    cat_cols = df.select_dtypes('string').columns.tolist()
    for cat_col in cat_cols:
        
        print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(cat_col)
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        
        for num_col in num_cols:
            
            print('\n----------------------------------------------------------------------------------------------------------')
            print(num_col)
            print('----------------------------------------------------------------------------------------------------------\n')
           
            fig = plt.figure(figsize = (12,6))
            fig.suptitle(f'{cat_col} vs. {num_col}')
            
            gs = plt.GridSpec(2,3)
            
            ax1 = fig.add_subplot(gs[0,0])
            sns.barplot(x=cat_col, y=num_col, data=df, color='green')
            plt.xticks(rotation = 90)
            
            ax2 = fig.add_subplot(gs[0,1])
            sns.swarmplot(x=cat_col, y=num_col, data=df, color='green')
            plt.xticks(rotation = 90)
            
            ax3 = fig.add_subplot(gs[0,2])
            sns.stripplot(x=cat_col, y=num_col, data=df, color='green')
            plt.xticks(rotation = 90)
            
            ax4 = fig.add_subplot(gs[1,0])
            sns.boxplot(x=cat_col, y=num_col, data=df, color='green')
            plt.xticks(rotation = 90)
            
            ax5 = fig.add_subplot(gs[1,1])
            sns.boxenplot(x=cat_col, y=num_col, data=df, color='green')
            plt.xticks(rotation = 90)
            
            ax6 = fig.add_subplot(gs[1,2])
            sns.violinplot(x=cat_col, y=num_col, data=df, color='green')
            plt.xticks(rotation = 90)
            
            plt.tight_layout()
            plt.show();
            
def select_kbest(X, y, k):
    '''
    Takes in predictors, target, and number of features to select and returns that number of best features based on SelectKBest function
    '''
    kbest = SelectKBest(f_regression, k=k)
    kbest.fit(X, y)
    return X.columns[kbest.get_support()].tolist()

def rfe(X, y, n):
    '''
    Takes in predictors, target, and number of features to select and returns that number of best features based on RFE function
    '''
    rfe = RFE(estimator=LinearRegression(), n_features_to_select=n)
    rfe.fit(X, y)
    return X.columns[rfe.get_support()].tolist()

def show_rfe_feature_ranking(X, y):
    '''
    Takes in predictors and target and returns feature ranking based on RFE function
    '''
    rfe = RFE(estimator=LinearRegression(), n_features_to_select=1)
    rfe.fit(X, y)
    rankings = pd.Series(rfe.ranking_, index=X.columns)
    return rankings.sort_values()