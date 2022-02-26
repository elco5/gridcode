#class for working with the .CSV output of the WT3000 Power Analyzer
import re
import pandas as pd

class WT3K:
    
    def __init__(self) -> None:
        pass
        self.data = pd.DataFrame()

    
    def read_in_file(self, file):
        # read in the file to a pandas dataframe
        # INPUT: the .csv file generate by the PA
        # OUTPUT: a pandas dataframe with meaninful column names
            # index is 1-indexed observation
        self.data = pd.read_csv(file, header=21)
        self.data.set_index ("Store No.")
        self.pretty_column_names()
    
    def pretty_column_names(self):
        for col in self.data.columns:
            new_name = col.rstrip("-Total")
            self.data.rename(columns={col: new_name}, inplace=True)
            


    # metadata such as sample rate 

    # plotter
        # INPUT: x column and y column
        #C:\Users\ecountrywood\dev\gridcode\pa_data.csv
        # /c/users/ecountrywood/dev/gridcode/


