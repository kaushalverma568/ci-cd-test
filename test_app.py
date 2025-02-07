import unittest
from app import hello_world  # Import the function from app.py

class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), "Hello, World")

if __name__ == "__main__":
    unittest.main()
