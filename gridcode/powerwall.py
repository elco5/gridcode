
class Powerwall:

    def __init__(self):
        
        self.vn = 240
        self.vh = self.vn * 1.15
        self.vl = self.vn * 0.85
        
        self.pmin = -5000
        self.prated = 5000
        self.pmax = 5000

