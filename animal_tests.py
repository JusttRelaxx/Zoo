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

    def test_eat_panda(self):
        animal = Animal("panda", 1, "Ivo", "male", 300)
        animal.eat()
        self.assertEqual(animal.weight, 300.1)

    def test_eat_tiger(self):
        animal = Animal("tiger", 2, "TegavTiger", "male", 300)
        animal.eat()
        self.assertEqual(animal.weight, 300.09)

    def test_eat_bear(self):
        animal = Animal("bear", 2, "MecoPug", "male", 300)
        animal.eat()
        self.assertEqual(animal.weight, 300.06)

    def test_grow_panda(self):
        animal = Animal("panda", 1, "Ivo", "male", 300)
        animal.grow()
        self.assertEqual(animal.age, 2)
        self.assertEqual(animal.weight, 304)

    def test_grow_tiger(self):
        animal = Animal("tiger", 2, "TegavTiger", "male", 300)
        animal.grow()
        self.assertEqual(animal.age, 3)
        self.assertEqual(animal.weight, 305)

    def test_grow_bear(self):
        animal = Animal("bear", 2, "MecoPug", "male", 300)
        animal.grow()
        self.assertEqual(animal.age, 3)
        self.assertEqual(animal.weight, 305)


if __name__ == '__main__':
    unittest.main()
