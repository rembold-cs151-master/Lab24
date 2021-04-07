#############################################
# Name: 
#############################################


class Vehicle:
    """ Generic class to store information about any vehicle. """
    def __init__(self, terrain, weight):
        self.terrain = terrain
        self.weight = weight

    def __repr__(self):
        return f"Vehicle({self.terrain},{self.weight})"

    def get_terrain(self):
        return self.terrain

    def set_terrain(self, new_terrain):
        self.terrain = new_terrain

    def get_weight(self):
        return self.weight

    def set_weight(self, new_weight):
        self.weight = new_weight

# You can go ahead and insert your class definitions below!












if __name__ == '__main__':
    pass
    # You can add any tests you want to run down here!
