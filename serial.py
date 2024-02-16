"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)
    

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        self.start = start
        self.count = start
    
    def generate(self):
        serial_number = self.count
        self.count += 1
        return serial_number
    
    def reset(self):
        serial.count = self.start
    

serial = SerialGenerator(start=100)

print(serial.generate())
print(serial.generate())
print(serial.generate())
print(serial.generate())
print(serial.generate())
print(serial.generate())
print(serial.generate())
print(serial.reset())