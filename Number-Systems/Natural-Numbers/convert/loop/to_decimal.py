
from typing import Callable

from ..to_decimal import callback as loop

def main(loop: Callable[[str, int], int]):
   while (In := input("\tinput a number and a base: ")):
      number, base = In.split()
      loop(number, int(base))

if __name__ == '__main__':
   main(loop)

