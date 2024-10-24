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
     
    df_hh = df.groupby('household_id').agg(
        size_hh=('person','count'),
        mean_age=('age','mean'),
        min_age=('age','min'),
        max_age=('age','max'),
        nr_female=('female','sum'),
        mean_income=('income','mean'),
        total_income=('income','sum')
    )
    
    df_hh = add_no_children(df_hh,df)
    df_hh = add_female_earner(df_hh,df)
    
    df_hh = df_hh.reset_index()
    return df_hh


def add_no_children(df_hh,df):
    """
    Add number of children as new column.
    """
    df_hh['no_children'] = df.groupby('household_id')['age'].apply(lambda x: (x<18).sum())
    return df_hh


def add_female_earner(df_hh,df):
    """
    Add column indicating if highest earner is female.
    """
    df_hh['highest_earner_female'] = df.groupby('household_id').apply(highest_earner_female)
    return df_hh


def highest_earner_female(group):
    """
    Indicate if highest earner in group is female.
    """
    max_income_row = group.loc[group['income'].idxmax()]
    return max_income_row['female']