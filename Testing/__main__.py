import unittest

loader = unittest.TestLoader()
testSuite = loader.discover(f'./{__package__}')
testRunner = unittest.TextTestRunner(verbosity=2)
testRunner.run(testSuite)

