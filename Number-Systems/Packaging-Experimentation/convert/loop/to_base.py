from typing import Callable

from ..to_base import callback as loop

def main(loop: Callable[[int, int], str]):
   while (In := input("\tinput a number and a base: ")):
      loop(*map(int, In.split()))

if __name__ == '__main__':
   main(loop)

