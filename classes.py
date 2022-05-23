from abc import ABC, abstractmethod



class Device(ABC):
    voltage = 0
    resistance = 0
    price = 0.0
    name = ""


    def __init__(self, voltage, resistance, price, name) -> None:
        self.voltage = voltage
        self.resistance = resistance
        self.price = price
        self.name = name
    

    @abstractmethod
    def make_noise(self):
        pass

class DigitalDevice(Device):
    invention_year = 2022
    def __init__(self, voltage, resistance, price, name, invention_year) -> None:
        super().__init__(voltage, resistance, price, name)
        self.invention_year = invention_year
    
    def make_noise(self):
        print("Dzz")

class AnalogDevice(Device):
    signal_frequency = 0.0

    def __init__(self, voltage, resistance, price, name, signal_frequency) -> None:
        super().__init__(voltage, resistance, price, name)
        self.signal_frequency = signal_frequency

    def make_noise(self):
        print("Vzh")

class ImpulseDevice(Device):
    impulse = 0.0
    
    def __init__(self, voltage, resistance, price, name, impulse) -> None:
        super().__init__(voltage, resistance, price, name)
        self.impulse = impulse

    def make_noise(self):
        print("hmm")


class Source(Device):
    directions = ["direct", "reversive"]
    direction = enumerate(directions)

    def __init__(self, voltage, resistance, price, name, direction = 0) -> None:
        super().__init__(voltage, resistance, price, name)
        self.direction = direction
        
    def make_noise(self):
        print("weef")

class PowerSource(Source):
    power = 0
    def __init__(self, voltage, resistance, price, name, power, direction=0, ) -> None:
        super().__init__(voltage, resistance, price, name, direction)
        self.power = power


    def make_noise(self):
        return super().make_noise()    


class CurrentSource(Source):
    current = 0
    def __init__(self, voltage, resistance, price, name, current, direction=0, ) -> None:
        super().__init__(voltage, resistance, price, name, direction)
        self.current = current


    def make_noise(self):
        return super().make_noise()

class OperativeAmplifier(AnalogDevice):
    amplify_rate = 1.0
    def __init__(self, voltage, resistance, price, name, signal_frequency, amplify_rate) -> None:
        super().__init__(voltage, resistance, price, name, signal_frequency)
        self.amplify_rate = amplify_rate

class Decoder(DigitalDevice):
    efficiency_in_chars_per_second = 0.0
    
    def __init__(self, voltage, resistance, price, name, invention_year, efficiency_in_chars_per_second) -> None:
        super().__init__(voltage, resistance, price, name, invention_year)
        self.efficiency_in_chars_per_second = efficiency_in_chars_per_second

class Adder(ImpulseDevice):
    is_binary = True

    def __init__(self, voltage, resistance, price, name, impulse, is_binary = True) -> None:
        super().__init__(voltage, resistance, price, name, impulse)
        self.is_binary = is_binary
        


crr_src = CurrentSource(10, 5, 100, "Crr_Source1", 1, 0)
pwr_src = PowerSource(14, 0.5, 125, "Pwr_Source1", 22, 1)
amplifier= OperativeAmplifier(5, 1, 15, "Amplifier1", 4, 1.5)
decoder = Decoder(10, 2, 2, "Decoder1", 2001, 100)
adder = Adder(100, 23, 400, "Adder1", 1, 0)
     
crr_src.make_noise()
pwr_src.make_noise()
amplifier.make_noise()


## in
