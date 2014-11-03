import unittest

from animal import Animal


class TestAnimal(unittest.TestCase):

    def test_animal_init(self):
        animal = Animal("panda", 1, "Ivo", "male", 300, 6, "bamboo", 10, 0.2)
        self.assertEqual("panda", animal.species)
        self.assertEqual(1, animal.age)
        self.assertEqual("Ivo", animal.name)
        self.assertEqual("male", animal.gender)
        self.assertEqual(300, animal.weight)
        self.assertEqual(6, animal.life_expectancy)
        self.assertEqual("bamboo", animal.food_type)
        self.assertEqual(10, animal.weight_age_ratio)
        self.assertEqual(0.2, animal.food_weight_ratio)
if __name__ == '__main__':
    unittest.main()
