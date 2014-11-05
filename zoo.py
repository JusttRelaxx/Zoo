from animal import Animal

import json


class Zoo:

    def __init__(self, animals, capacity, budget):
        self.animals = animals
        self.capacity = capacity
        self.budget = budget

    def get_dailty_incomes(self):
        return len(self.animals) * 60

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


bear = Animal("bear", 12, "Pesho", "male", 60)
bear.get_info("gestation_period")
print (bear.daily_food_consumption)
