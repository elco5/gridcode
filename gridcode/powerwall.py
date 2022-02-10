class VoltWattSettings:

    def __init__(self, characteristic_type, category, eut) -> None:
        
        self.characteristic = characteristic_type
        self.category = category

        if characteristic_type == 1:
            self.v1 = eut.vn * 1.06
            self.p1 = eut.prated
            self.v2 = eut.vn * 1.1
            self.p2_prime = -eut.prated
            self.ol_tr = 10

        elif characteristic_type == 2:
            self.v1 = eut.vn * 1.05
            self.p1 = eut.prated
            self.v2 = eut.vn * 1.1
            self.p2_prime = -eut.prated
            self.ol_tr = 90

        elif characteristic_type == 3:
            self.v1 = eut.vn * 1.09
            self.p1 = eut.prated
            self.v2 = eut.vn * 1.1
            self.p2_prime = -eut.prated
            self.ol_tr = 0.5

class Powerwall:

    def __init__(self):
        self.vn = 240
        self.prated = 5000


pw = Powerwall()
print(pw.vn + pw.prated)
