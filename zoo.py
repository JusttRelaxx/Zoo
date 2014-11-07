from animal import Animal

import json


class Zoo:

    INCOME_PER_ANIMAL = 60

    def __init__(self, animals, capacity, budget):
        self.animals = animals
        self.capacity = capacity
        self.budget = budget

    def get_daily_incomes(self):
        return len(self.animals) * Zoo.INCOME_PER_ANIMAL

    def get_daily_outcomes(self):
        daily_outcome = 0
        for animal in self.animals:
            if animal.food_type == "carnivore":
                daily_outcome += animal.daily_food_consumption * 4
            elif animal.food_type == "herbivore":
                daily_outcome += animal.daily_food_consumption * 2
        return daily_outcome

    def accommodate_an_animal(self, animal):
        if len(self.animals) < self.capacity:
            self.animals.append(animal)
        else:
            raise OverflowError("Zoo is full of animals")

    def see_animals(self):
        for animal in self.animals:
            print ("{} : {}, {}, {}, {}".format(
                animal.name,
                animal.species, animal.gender, animal.age, animal.weight))

    def move_to_habitat(self, species, name):
        for animal in self.animals:
            if (animal.species == species and animal.name == name):
                self.animals.remove(animal)

    def reproduce(self):
        pass

    def remove_dead_animals(self):
        list_of_alive_animals = []
        for animal in self.animals:
            if animal.is_alive:
                list_of_alive_animals.append(animal)
        self.animals = list_of_alive_animals
