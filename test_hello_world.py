import unittest
from hello_world import print_hello_world


class TestPrintHelloWorld(unittest.TestCase):
    def test_print_hello_world(self):
        self.assertEqual(print_hello_world(), None, 'Function must return None')


if __name__ == '__main__':
    unittest.main()