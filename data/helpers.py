import pandas as pd

states = pd.read_csv('join_tables/state_abbrevs.csv')


def name_to_code(state_name):
    try:
        return states[states['State'] == state_name]['Code'].values[0]
    except:
        print(f"Error Processing {state_name}")

def code_to_name(state_code):
    try:
        return states[states['Code'] == state_code]['State'].values[0]
    except:
        print(f"Error Processing {state_name}")