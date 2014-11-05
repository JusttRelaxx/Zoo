import unittest

from animal import Animal


class TestAnimal(unittest.TestCase):

    def test_animal_init(self):
        animal = Animal("panda", 1, "Ivo", "male", 300, 400, 6, "bamboo", 10, 0.2, 20, True)
        self.assertEqual("panda", animal.species)
        self.assertEqual(1, animal.age)
        self.assertEqual("Ivo", animal.name)
        self.assertEqual("male", animal.gender)
        self.assertEqual(300, animal.weight)
        self.assertEqual(400, animal.average_weight)
        self.assertEqual(6, animal.life_expectancy)
        self.assertEqual("bamboo", animal.food_type)
        self.assertEqual(10, animal.weight_age_ratio)
        self.assertEqual(0.2, animal.food_weight_ratio)
        self.assertEqual(20, animal.new_born_weight)

    def test_animal_save(self):
        animal1 = Animal("panda", 1, "Ivo", "male", 300, 400, 6, "bamboo", 10, 0.2, 20, True)
        animal2 = Animal("bear", 2, "Mecho", "male", 400, 650, 3, "meat", 12, 0.4, 25, True)
        animal1.save_animals_to_json()
        animal2.save_animals_to_json()

if __name__ == '__main__':
    unittest.main()
