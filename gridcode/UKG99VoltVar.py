import numpy as np

class UKG99VoltVar:
    

    def __init__(self, characteristic_type, eut) -> None:
        
        self.characteristic = characteristic_type
        self.eut = eut

        if characteristic_type == 1:
            self.Q = np.array([1, 0, 0, -1]) *eut.qmax
            self.V = np.array([0.95, 1, 1, 1.05]) * eut.vn

        elif characteristic_type == 2:
            self.Q = np.array([0.5, 0, 0, -0.5]) *eut.qmax
            self.V = np.array([0.9, 0.98, 1.02, 1.1]) * eut.vn

        elif characteristic_type == 3:
            self.Q = np.array([0.05, 0, 0, -0.05]) *eut.qmax
            self.V = np.array([0.82, 0.95, 1.05, 1.18]) * eut.vn

    def vars_from_volts(self, volts):

        if volts <= self.V[1]:
            dy = self.Q[1] - self.Q[0]
            dx = self.V[1] - self.V[0]
            return (dy/dx) * (volts - self.V[1])
        elif (volts > self.V[1] and volts < self.V[2]):        
            return 0
        elif volts >= self.V[2]:
            dy = self.Q[3] - self.Q[2]
            dx = self.V[3] - self.V[2]
            return (dy/dx) * (self.V[3] - volts)