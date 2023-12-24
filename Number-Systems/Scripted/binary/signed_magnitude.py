"""
   Negative Offset

   CLI Options:
      a number to fix bit-size and loop
"""

# the hardest part to pares will be that `-0` is not `0`

from typing import Callable

from binary import to_binary, fixed, loop as main

def parser(WIDTH: int) -> Callable[[str], int]:
   def parsed(s:str, offset:int = 2**(WIDTH-1)) -> int:
      # kind of cheating because I've programmed to_binary to ignore the sign
      # otherwise this should be 2^(WIDTH-1) + abs(n)
      n = int(s)
      if not s.strip().startswith('-'):
         return n
      if n == 0:
         return offset
      return offset - n
   return parsed

def signed_magnitude(WIDTH:int) -> Callable[[str], str]:
   def callback(
         n:str,
         to_binary:Callable[[int], str] = fixed(WIDTH)(to_binary),
         parsed: Callable[[str], int] = parser(WIDTH)
      ) -> str:
      return to_binary(parsed(n))
   return callback


def loop():
   while (In := input("Input the number of bits and a number: ")):
      bits, number = In.split()
      print(
         f"{number} signed magnitude with {bits}-bits: {signed_magnitude(int(bits))(number)}"
      )


if __name__ == '__main__':

   import sys

   if len(sys.argv) == 1:
      # variadic bit sized loop
      loop()
      exit()

   if len(sys.argv) != 2:
      print(__doc__)
      raise ValueError(f"{sys.argv} is no good ...")

   WIDTH = int(sys.argv[1])

   main(
      signed_magnitude(WIDTH),
      f"{{}} as a {WIDTH}-binary encoded with two's complement: {{}}"
   )

