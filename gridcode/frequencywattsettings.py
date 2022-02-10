
class FrequencyWattSettings:

    def __init__(self, characteristic_type, category) -> None:
        
        self.characteristic = characteristic_type
        self.category = category

        if characteristic_type == 1:
            self.dbof = 0.036
            self.kof = 0.05
            self.Tr = 5
        elif characteristic_type == 2:
            if category == (1 or 2):
                self.dbof = 0.017
                self.kof = 0.03
                self.Tr = 1
            elif category == 3:
                self.dbof = 0.017
                self.kof = 0.02
                self.Tr = 0.2

class ExpectedPowerCalculator:

    def load_frequency_settings(self,frequency_watt_setting):
        pass

#fwset = FrequencyWattSettings(1, 3)
#print(fwset.kof)
