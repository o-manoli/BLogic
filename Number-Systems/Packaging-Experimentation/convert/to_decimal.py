"""
	TODO
"""

from typing import Callable

from .algorithms.to_decimal import to_decimal


def callback(number: str, base: int) -> int:

   converted = to_decimal(number, base)

   print(f"\n\t{number} in base {base}: {converted} in decimal\n")

   return converted


def main(callback: Callable[[str, int], int]):
   import sys

   if len(sys.argv) != 3:
      print(__doc__)
      raise ValueError("Not enough args ... or perhaps too much")

   number, base = sys.argv[1:]
   callback(number, int(base))

if __name__ == '__main__':
   main(callback)

