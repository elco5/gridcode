#class for working with the .CSV output of the WT3000 Power Analyzer
import pandas as pd
import numpy as np
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
        # self.data.set_index ("Store No.")
        self.pretty_column_names()
    
    def pretty_column_names(self):
        for col in self.data.columns:
            new_name = col.rstrip("-Total")
            self.data.rename(columns={col: new_name}, inplace=True)
            


    def get_step_average(self, data_series, bin_start_index, bin_width):
        sum = 0
        n_samples = 5
        bin_middle_index = np.floor((bin_start_index + bin_width)/2)
        sample_start_index = bin_middle_index - np.floor(n_samples / 2)
        sample_end_index = sample_start_index + n_samples
        loop_counter = 0
        for index in range(sample_start_index,sample_end_index):
            sum = sum + data_series.loc[index]
            loop_counter += 1

        # start index
        # every nth sample (bin_width)
        # sample size for average




    # metadata such as sample rate 

    # plotter
        # INPUT: x column and y column
        #C:\Users\ecountrywood\dev\gridcode\pa_data.csv
        # /c/users/ecountrywood/dev/gridcode/


