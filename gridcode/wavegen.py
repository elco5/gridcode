#import re
#from tokenize import Name
import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

class Wavegen:

    def __init__(self) -> None:
        pass

    def time_vector(self, n_points) -> np.ndarray:
        T = np.linspace(0,1,n_points,endpoint=False)
        return T
    
    def shifted_sin_function(self,t,shift_deg) -> float:
        alpha = 2*np.pi*t
        beta = shift_deg*(180/np.pi)
        return np.sin(alpha + beta)

    def generate_wave(self,T: np.ndarray, shift_deg: float) -> np.ndarray:
        W = np.zeros(len(T))
        for count, t in enumerate(T):
            W[count] = self.shifted_sin_function(T[count],shift_deg)
        return W


# wg = Wavegen()
# n_points = 24
# shift_deg = -np.pi
# T = wg.time_vector(n_points)
# print(T)
# W = wg.generate_wave(T,shift_deg) 

# df = pd.DataFrame(np.round(W.T,4),np.round(T.T,4))
# df.to_csv('wave.csv', header=False)
# fig = df.plot()









wg = Wavegen()
T = wg.time_vector(12)
print(T)
