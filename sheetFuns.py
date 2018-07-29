"""File with functions to handle weightings spreadsheet"""
import pandas as pd
def load_sheet():
    """Load weightings spreadsheet"""
    try:
        weightings = pd.read_excel('weightings.xlsx')
    except FileNotFoundError:
        weightings = None
    
    return weightings