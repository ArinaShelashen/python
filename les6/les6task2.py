class Road:
    def __init__(self, _length, _width):
        _length = _length
        _width = _width
        self.square = _length * _width

    def asphalt(self):
        asph_mass_sqm_kg = 25
        depth_cm = 5
        tot_mass = int(self.square * asph_mass_sqm_kg * (depth_cm / 100))
        print(f'Необходимая масса асфальта - {tot_mass} т')


a = Road(20, 500)
a.asphalt()
