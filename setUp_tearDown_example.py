import unittest
from student import Student


class ExampleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    def setUp(self):
        self.student = Student("Alan", "Sample")
        print("\tsetUp")

    def tearDown(self):
        print("\ttearDown")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def test_full_name(self):
        self.assertEqual(self.student.full_name, "Alan Sample")
        print("\t\tRunning Test 1")

    def test_email(self):
        self.assertEqual(self.student.email, "alan.sample@email.com")
        print("\t\tRunning Test 2")


if __name__ == "__main__":
    unittest.main()
