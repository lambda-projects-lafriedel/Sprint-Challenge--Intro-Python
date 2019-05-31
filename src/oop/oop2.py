# Superclass that defaults wheel number to 4 if not specified in instance
class GroundVehicle():
    def __init__(self, num_wheels = 4):
        self.num_wheels = num_wheels

    def drive(self):
        return "vroooom"


# Subclass Motorcycle from GroundVehicle, specify wheel number as 2 and override drive().
class Motorcycle(GroundVehicle):
    def __init__(self, num_wheels = 2):
        super().__init__(num_wheels)

    def drive(self):
        return "BRAAAP!!"

vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and print the result of calling drive() on each.
vehicle_noise = [v.drive() for v in vehicles]
print(vehicle_noise)