# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# This is the base/superclass
class Vehicle:
    pass

# This is a subclass of Vehicle
class GroundVehicle(Vehicle):
    pass

# This is a subclass of Vehicle
class FlightVehicle(Vehicle):
    pass

# This is a subclass of GroundVehicle, which is a subclass of Vehicle
class Car(GroundVehicle):
    pass

# This is a subclass of GroundVehicle, which is a subclass of Vehicle
class Motorcycle(GroundVehicle):
    pass

# This is a subclass of FlightVehicle, which is a subclass of Vehicle
class Airplane(FlightVehicle):
    pass

# This is a subclass of FlightVehicle, which is a subclass of Vehicle
class Starship(FlightVehicle):
    pass
