# Built on Python 3.6.5 on Linux
from pathlib import Path

import pandas as pd

def get_list(file_list):
    """ Function reads the csv.  May need more options depending on the 
        characteristics of the file."""
    
    df = pd.read_csv(file_list)
    
    return df

def clean_options(df, path_column):
    """ Creates a list from the path column in the dataframe.  
        Removes leading "'" that may occur if a line contains a leading "/" as 
        in the case of denoting a Linux file system in Excel or LibreOffice.
        May not be needed.  Is needed in hand created testing file.  More
        cleanining operations could go here.  """
        
    df = df[path_column].str.lstrip(to_strip="'")
    #print(df) # Testing
    df_list = df.tolist()
    #print(df_list) # test
    return df_list
            
def test_path(df_list):
    """ Test existance of the file and greate a list of results"""
    results = []
    for i in df_list:
        temp_result = []
        if Path(i).is_file():
            temp_result.append(i)
            temp_result.append('yes')
        else:
            temp_result.append(i)
            temp_result.append('no')
        results.append(temp_result)
        
    #print(results)  # Test
    return results   

def create_file(results):
    """ Create a file of results.  Defaults to directory where spript is run.
        Specify an alternative location if so desired."""     
    
    # Create a dataframe from the list.  Not necessary, but give a tool for 
    # further manipulation if you want to expand the functionality.
    df_results = pd.DataFrame.from_records(results, columns=['File', 'Exists'])
    # Write to file.  
    df_results.to_csv('Results.csv', index=False)
    

if __name__=='__main__':
    # Define some variables.
    file_list = Path('/home/willy/dwfiles/file_list.csv')
    path_column = 'path'
    # Read the file with the column of file paths to test.
    df = get_list(file_list)
    # Get list of file paths.
    df_list = clean_options(df, path_column)
    #Test the file paths
    results = test_path(df_list)
    # Creaye the file
    create_file(results)
    
    
    
    