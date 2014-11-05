import unittest
from zoo import Zoo


class TestZoo(unittest.TestCase):

    def setUp(self):
        self.zoo = Zoo([], 10, 200)

    def test_init(self):
        self.assertEqual(self.zoo.budget, 200)
        self.assertEqual(self.zoo.capacity, 10)
        
if __name__ == '__main__':
    unittest.main()
