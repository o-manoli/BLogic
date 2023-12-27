"""
   Basic Testcases
"""

# imports are relatively hard :(

from pathlib import Path

import sys

sys.path.append(f"{Path(__file__).parent.parent}")

from to_rational import convert_rational

import unittest

class Test_Rational_Numbers(unittest.TestCase):
   def test_convert_rational(self):
      """
         Source: Uebungsaufgaben-DT1-Loesung A6.2
      """
      self.assertEqual(convert_rational(base= 2)("0.3"), ("0.01001","1001"))
      self.assertEqual(convert_rational(base= 2)("12.3"), ("1100.01001","1001"))
      self.assertEqual(convert_rational(base= 3)("50.5"), ("1212.1","1"))
      self.assertEqual(convert_rational(base= 4)("50.5"), ("302.2",""))
      self.assertEqual(convert_rational(base= 5)("50.4"), ("200.2",""))
      self.assertEqual(convert_rational(base= 6)("60.75"), ("140.43",""))
      self.assertEqual(convert_rational(base= 7)("37.3"), ("52.2046","2046"))
      self.assertEqual(convert_rational(base= 8)("101.75"), ("145.6",""))
      self.assertEqual(convert_rational(base= 9)("111.3"), ("133.26","26"))
      self.assertEqual(convert_rational(base=11)("151.4"), ("128.4","4"))
      self.assertEqual(convert_rational(base=12)("47.875"), ("3B.A6",""))
      self.assertEqual(convert_rational(base=13)("47.875"), ("38.B4","B4"))
      self.assertEqual(convert_rational(base=14)("47.875"), ("35.C37",""))
      self.assertEqual(convert_rational(base=15)("41.875"), ("2B.D1","D1"))
      self.assertEqual(convert_rational(base=16)("172.859375"), ("AC.DC",""))

