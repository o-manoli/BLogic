"""
	TODO
"""


from typing import Callable
from .algorithms.to_base import to_base

def callback(number: int, base: int) -> str:

   converted = to_base(number, base)

   print(f"\n\t{number} in base {base} is: {converted}\n")

   return converted


def main(callback: Callable[[int, int], str]):
   import sys

   if len(sys.argv) != 3:
      print(__doc__)
      raise ValueError("Not enough args ... or perhaps too much")

   callback(*map(int, sys.argv[1:]))

if __name__ == '__main__':
   main(callback)


