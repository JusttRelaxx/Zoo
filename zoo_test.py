import unittest
from zoo import Zoo
from animal import Animal


class TestZoo(unittest.TestCase):

    def setUp(self):
        self.bear = Animal("bear", 12, "Pesho", "male", 60)
        self.panda = Animal("panda", 12, "Ivo", "male", 60)
        animals = [self.bear, self.panda]
        self.zoo = Zoo(animals, 10, 200)

    def test_init(self):
        self.assertEqual(self.zoo.animals, [self.bear, self.panda])
        self.assertEqual(self.zoo.budget, 200)
        self.assertEqual(self.zoo.capacity, 10)

    def test_get_info(self):
        self.assertEqual(self.bear.get_info("gestation_period"), 3)

    def test_move_to_habitat(self):
        self.zoo.move_to_habitat("bear", "Pesho")
        self.assertEqual(self.zoo.animals, [self.panda])

    def test_daily_incomes(self):
        self.assertEqual(self.zoo.get_daily_incomes(), 120)

    def test_accommodate_an_animal(self):
        bear2 = Animal("bear", 12, "Pesho2", "male", 60)
        self.zoo.accommodate_an_animal(bear2)
        self.assertEqual(self.zoo.animals, [self.bear, self.panda, bear2])

    def test_remove_dead_animals(self):
        bear2 = Animal("bear", 12, "Pesho2", "male", 60)
        self.zoo.accommodate_an_animal(bear2)
        bear2.is_alive = False
        self.zoo.remove_dead_animals()
        self.assertEqual(self.zoo.animals, [self.bear, self.panda])

if __name__ == '__main__':
    unittest.main()
