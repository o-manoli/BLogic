"""
   wrappers all the way down

"""

from typing import Callable

from binary import to_binary, fixed, integer_feeder, loop

def offset(WIDTH:int) -> Callable[[int], str]:
   def callback(
         n:int, offset:int = 2**(WIDTH-1),
         to_binary:Callable[[int], str] = fixed(WIDTH)(to_binary)
   ) -> str:
      return to_binary(offset+n)
   return callback

if __name__ == '__main__':

   import sys

   if len(sys.argv) != 2:
      print(__doc__)
      raise ValueError(f"{sys.argv} is no good ...")

   WIDTH = int(sys.argv[1])

   loop(
      integer_feeder(offset)(WIDTH),
      f"{{}} as a {WIDTH}-binary with positive offset: {{}}"
   )



