import unittest
from pathlib import Path

loader = unittest.TestLoader()
testSuite = loader.discover(f"{Path(__file__).parent}")

testRunner = unittest.TextTestRunner(verbosity=2)

testRunner.run(testSuite)

