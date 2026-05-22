import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.employee1 = Employee("John", "Doe", 5000)
        self.employee2 = Employee("Foo", "Bar", 7000)
        self.employee3 = Employee("Baz", "Shar", 10000)

    def test_attributes(self):
        self.assertTrue(self.employee1.first)
        self.assertTrue(self.employee2.last)
        self.assertEqual(10000, self.employee3.pay)

    def test_email(self):
        self.assertEqual("John.Doe@email.com", self.employee1.email)
        self.assertEqual("Foo.Bar@email.com", self.employee2.email)
        self.assertEqual("Baz.Shar@email.com", self.employee3.email)

    def test_fullname(self):
        self.assertEqual("John Doe", self.employee1.fullname)
        self.assertEqual("Foo Bar", self.employee2.fullname)

    def test_raise(self):
        self.employee1.apply_raise()
        self.assertEqual(5250, self.employee1.pay)
        self.employee2.apply_raise()
        self.assertEqual(7350, self.employee2.pay)
        self.employee3.apply_cut()
        self.assertEqual(9500, self.employee3.pay)


if __name__ == "__main__":
    unittest.main()
