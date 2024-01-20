
import unittest
from pathlib import Path
from sys import path


Loader = unittest.TestLoader()
Runner = unittest.TextTestRunner(verbosity= 2)

TestCasesPath = Path(__file__).parent
path.append(f"{TestCasesPath.parent}")

TestSuit = Loader.discover(f"{TestCasesPath}")
Runner.run(TestSuit)

