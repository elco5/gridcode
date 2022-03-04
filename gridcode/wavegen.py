
import numpy as np
import pandas as pd


class Wavegen:

    
    def __init__(self) -> None:
        self.n_points = 1024
        self.decimal_places = 6    

    def time_vector(self) -> np.ndarray:
        T = np.linspace(0,1,self.n_points,endpoint=False)
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
    
    def batch_create_waveforms(self):

        min_shift_deg = -90
        max_shift_deg = 90
        iterval_deg = 5

        index = np.arange(self.n_points)
        T = self.time_vector()

        for shift in range(min_shift_deg,max_shift_deg+1,iterval_deg):
            W = self.generate_wave(T,shift)
            df = pd.DataFrame(np.round(W.T,self.decimal_places),index.T)
            file_name = './waveforms/' + str(shift) + '.abw'
            df.to_csv(file_name, header=False)



#     def run_app(self):
#         print("app has run")
        
# if __name__ == "__main__":
#     with Wavegen() as app:
#         app.run_app()