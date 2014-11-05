import json

animals = {}


class Animal:
    # weight/age ratio - how much does the species grow for a month
    # till average weight (when the species gets to average weight,
    # it stops growing)

    def __init__(
            self, species, age, name, gender,
            weight):

        self.species = species
        self.age = age
        self.name = name
        self.gender = gender
        self.weight = weight
        self.is_alive = True
        self.daily_food_consumption = self.get_info("food_weight_ratio") * self.weight
    """def save_animals_to_json(self):

        animals[self.name] = {'species': self.species,
                              'live_expectancy': self.life_expectancy,
                              'food_type': self.food_type,
                              'gestation_period': self.gestation_period,
                              'weight_age_ratio': self.weight_age_ratio,
                              'food_weight_ratio': self.food_weight_ratio,
                              'new_born_weight': self.new_born_weight}

        file = open('database.json', 'w+')
        file.write(json.dumps(animals))
        file.close()"""

    def grow(self, age):
        expected_weight = self.weight_age_ratio * age
        if self.weight + expected_weight <= self.average_weight:
            self.weight += expected_weight
            self.age += age

    def get_database(self):
        with open("database.json", 'r') as load_file:
            content = json.load(load_file)
        return content

    def get_info(self, info):
        for animal in self.get_database()['Animals']:
            if animal['species'] == self.species:
                return animal[info]
