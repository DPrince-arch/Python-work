import unittest
from jar import Jar

instance = Jar

instance.capacity
instance.deposit
instance.size
instance.withdraw
#instance.mro

class TestJar(unittest.TestCase):

    def test_init(self):
        jar = Jar(10)
        self.assertEqual(jar.capacity, 10)
        self.assertEqual(jar.size, 0)

        with self.assertRaises(ValueError):
            jar.Jar(-5)

    def test_str(self):
        jar = Jar(5)
        jar.deposit(3)
        self.assertEqual(str(jar), "🍪🍪🍪")

    def test_deposit(self):
        jar = Jar(5)
        jar.deposit(2)
        self.assertEqual(jar.size, 2)

        jar.deposit(3)
        self.assertEqual(jar.size, 5)

        with self.assertRaises(ValueError):
            jar.deposit(1)

    def test_withdraw(self):
        jar = Jar(5)
        jar.deposit(4)

        jar.withdraw(1)
        self.assertEqual(jar.size, 3)

        jar.withdraw(3)
        self.assertEqual(jar.size, 0)

        with self.assertRaises(ValueError):
            jar.withdraw(1)

    def test_capacity_property(self):
        jar = Jar(8)
        self.assertEqual(jar.capacity, 8)

    def test_size_property(self):
        jar = Jar(5)
        jar.deposit(4)
        self.assertEqual(jar.size, 4)


if __name__ == "__main__":
    unittest.main()
