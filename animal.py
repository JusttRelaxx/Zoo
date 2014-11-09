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

    def grow(self):
        if self.is_alive:
            self.age += 1
            weight_age_ratio = self.get_info("weight_age_ratio")
            self.weight += weight_age_ratio

    def eat(self):
        food_weight_ratio = self.get_info("food_weight_ratio")
        self.weight += food_weight_ratio

    def get_database(self):
        with open("database.json", 'r') as load_file:
            content = json.load(load_file)
        return content

    def get_info(self, info):
        for animal in self.get_database()['Animals']:
            if animal['species'] == self.species:
                return animal[info]
