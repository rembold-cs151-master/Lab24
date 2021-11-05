# Lab09.py

""" Playing around with inheritance and class definitions in the context of different
sorts of vehicles.
"""

class Vehicle:
    """ Generic class to store information about any vehicle. """
    def __init__(self, terrain, weight):
        self.terrain = terrain
        self.weight = weight

    def __repr__(self):
        return f"Vehicle({self.terrain},{self.weight})"

    def get_terrain(self):
        """ Gets the terrain the vehicle traverses. """
        return self.terrain

    def set_terrain(self, new_terrain):
        """ Set a new terrain type for the vehicle.
        Inputs:
            new_terrain (str): The new terrain type
        """
        self.terrain = new_terrain

    def get_weight(self):
        """ Get the weight of the vehicle. """
        return self.weight

    def set_weight(self, new_weight):
        """ Set a new weight for the vehicle. 
        Inputs:
            new_weight (float): The new vehicle weight
        """
        self.weight = new_weight

# You can go ahead and insert your class definitions below!












if __name__ == '__main__':
    pass
    # You can add any tests you want to run down here! And you should absolutely do so!
