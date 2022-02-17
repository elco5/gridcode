import pandas as pd
import numpy as np

class ReportDriver:
    
    #class data
        #test profile values table
        #plots

    def __init__(self) -> None:
        self.table = pd.DataFrame()

    def test_profile_to_csv(self,vw_test):pass
    #input n voltWattTests
    #output table of test values 

    def calc_ideal_power_data_frame(self,vw_test):
        #input voltWattTest
        data_length = 100

        v = np.linspace(vw_test.eut.vl, vw_test.eut.vh, data_length)
        power = np.zeros(data_length)

        for count, voltage in enumerate(v):
            power[count] = vw_test.watts_from_volts(v[count])
        
        ideal_df = pd.DataFrame({'volts': v.T , 'watts': power.T})

        #ideal tolerance
        watt_tolerance = vw_test.eut.prated * 0.05
        ideal_df['w-hi'] = ideal_df['watts'] + watt_tolerance
        ideal_df['w-lo'] = ideal_df['watts'] - watt_tolerance

        return ideal_df
        
    def test_steps_power_data_frame(self,vw_test):
        P = np.zeros(len(vw_test.steps))
        for count, voltage in enumerate(vw_test.steps):
            P[count] = vw_test.watts_from_volts(vw_test.steps[count])
        
        test_steps_df = {'volts': vw_test.steps.T , 'watts': P.T}
        
        return test_steps_df

    def vw_plotter(self,VoltWattTest,):pass

