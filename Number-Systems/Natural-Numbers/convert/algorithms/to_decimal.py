
from typing import Iterator

def base_multiplier(base:int) -> Iterator[int]:
   b = 1
   while True:
      yield b
      b *= base

def to_decimal_implemented(
   n: str, base: int,
   symbols: dict[str, int] = {
      s:i for i, s in enumerate("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
       }
   ) -> int:

   return sum(
      map(
         lambda digit, p: symbols[digit]*p, n[::-1], base_multiplier(base)
      )
   )

to_decimal = int # really that simple ;)


