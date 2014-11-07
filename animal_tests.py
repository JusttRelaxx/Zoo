import unittest

from animal import Animal


class TestAnimal(unittest.TestCase):

    def test_animal_init(self):
        animal = Animal("panda", 1, "Ivo", "male", 300)
        self.assertEqual("panda", animal.species)
        self.assertEqual(1, animal.age)
        self.assertEqual("Ivo", animal.name)
        self.assertEqual("male", animal.gender)
        self.assertEqual(300, animal.weight)


if __name__ == '__main__':
    unittest.main()
