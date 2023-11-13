import unittest

from BLogic import P, InputSpace

class HayThere(unittest.TestCase):

	def test_load_class(self):
		S = InputSpace(2)
		a, b = S(1), S(0)
		print()
		P(a, b)

	def test_and_overloading(self):
		S = InputSpace(2)
		a, b = S(1), S(0)
		print()
		P(a, b, a & b)

	def test_or_overloading(self):
		S = InputSpace(2)
		a, b = S(1), S(0)
		print()
		P(a, b, a | b)

	def test_identity(self):
		S = InputSpace(3)

		a = S(0)

		print(f"""

			{type(a) = }
			{type(S) = }
			{type(InputSpace) = }

		""")

