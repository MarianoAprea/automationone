import unittest


class MiClase(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(2 + 2, 4)

    def test_multiplicacion(self):
        self.assertEqual(5 * 5, 25)


if __name__ == '__main__':
    unittest.main()
