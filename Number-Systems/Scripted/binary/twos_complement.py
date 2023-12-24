"""
   wrappers all the way down

"""

from typing import Callable

from binary import to_binary, fixed, integer_feeder, loop as main

def complement(WIDTH:int) -> Callable[[int], str]:
   def callback(
         n:int, offset:int = 2**WIDTH,
         to_binary:Callable[[int], str] = fixed(WIDTH)(to_binary)
      ) -> str:
      return to_binary(offset + n if n < 0 else n)
   return callback


def loop():
   while (In := input("Input the number of bits and a number: ")):
      bits, number = *map(int, In.split()),
      print(
         f"{number} as binary complement with {bits}-bits: {complement(bits)(number)}"
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
      integer_feeder(complement)(WIDTH),
      f"{{}} as a {WIDTH}-binary encoded with two's complement: {{}}"
   )


# Another Implementation

def inverted(
      n:str,
      Map:dict[str, str]={zero:one for zero, one in zip("01", "10")}
   ) -> str:
   return "1" + ''.join(Map[c] for c in n)

def one_liner_ish(n:int) -> str:
   return inverted(to_binary(-1-n)) if n < 0 else to_binary(n)


