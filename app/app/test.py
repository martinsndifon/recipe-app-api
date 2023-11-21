"""
Sample test
"""
from django.test import SimpleTestCase
from app.calc import add, subtract

class CalcTest(SimpleTestCase):
	"""Test the calc module"""

	def test_add_numbers(self):
		"""Test addition of two numbers"""
		res = add(5, 6)
		self.assertEqual(res, 11)

	def test_subtract_numbers(self):
		"""Test substracting numbers"""

		res = subtract(15, 10)
		self.assertEqual(res, 5)