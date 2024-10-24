import numpy as np
import pandas as pd

def simulate_data():
    """
    Re-create pandas df from the first lecture.
    """
    household_id_vals = [37,37,37,241,242,155789,155789,155789]
    person_vals = [1,2,3,1,1,1,2,3]
    age_vals = [20,19,19,50,29,58,61,15]
    income_vals = [10000,5300,4700,90000,20000,5000,11000,np.nan]
    female_vals = [False,True,False,True,False,False,True,False]
    df = pd.DataFrame({'household_id':household_id_vals,
                       'person':person_vals,
                       'age':age_vals,
                       'income':income_vals,
                       'female':female_vals})
    return df


def generate_household_data(df):
    """
    Group data at household (hh) level and create
    additional columns for data analysis.
    """
    df_hh = df.groupby('household_id').agg({
        'person':'count',
        'age':'mean',
        'age':'min',
        'age':'max',
        'female':'sum',
        'income':'mean',
        'income':'sum'
    })
    
    df_hh.columns = ['size_hh',
                     'mean_age',
                     'min_age',
                     'max_age',
                     'nr_female',
                     'mean_income',
                     'total_income']
    
    
    df_hh = df_hh.reset_index()
    return df_hh