
class VoltWattTest:

    def __init__(self, characteristic_type,  eut):
        # todo: add percent_power
        self.characteristic = characteristic_type
        self.eut = eut

        self.vh = eut.vn * 1.15
        self.vl = eut.vn * 0.85
        self.av = eut.vn * 0.015

        if characteristic_type == 1:
            self.v1 = eut.vn * 1.06
            self.p1 = eut.prated
            self.v2 = eut.vn * 1.1
            self.p2_prime = 0
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

        self.steps = [
            self.vl + self.av,
            self.v1 - self.av,
            self.v1 + self.av,
            (self.v1 + self.v2)/2,
            self.v2 - self.av,
            self.v2 + self.av,
            self.vh - self.av,
            self.v2 + self.av,
            self.v2 - self.av,
            (self.v1 + self.v2)/2,
            self.v1 + self.av,
            self.v1 - self.av,
            self.vl + self.av
        ]

    def vw_slope(self):
        dy = self.p2_prime - self.p1
        dx = self.v2 - self.v1
        return dy/dx

    def watts_from_volts(self, volts):

        if volts <= self.v1:
            return self.p1

        elif volts <= self.v2:
            m = self.vw_slope()
            return m * (volts - self.v1) + self.p1

        else:
            return self.p2_prime
        #     # some tests of function
        # print(vw1.vw_slope())
        # print(vw1.watts_from_volts(200))
        # print(vw1.watts_from_volts(vw1.v2))


# Step AC to V_L + a_v
# Step AC to V_1 - a_v
# Step AC to V_1 + a_v
# Step AC to (V_1+V_2)/2
# Step AC to V_2 - a_v
# Step AC to V_2 + a_v
# Step AC to V_H - a_v
# Step AC to V_2 + a_v
# Step AC to V_2 - a_v
# Step AC to (V_1+V_2)/2
# Step AC to V_1 - a_v
# Step AC to V_1 + a_v
# Step AC to V_L + a_v
