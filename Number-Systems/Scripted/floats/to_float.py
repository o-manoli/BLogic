"""
   Wrapper Madness
"""

from typing import Callable, Iterator
from functools import wraps

Symbols:dict[int, str] = {
   i:c for i, c in enumerate("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
}

def as_integer(f:Callable[[int], str]) -> Callable[[str], str]:
   @wraps(f)
   def wrapper(N:str) -> str:
      return f(int(N))
   return wrapper

def positive_input(f:Callable[[int], str]) -> Callable[[int], str]:
   @wraps(f)
   def wrapper(n:int) -> str:
      return f(-n if n < 0 else n)
   return wrapper

def zero_output(f:Callable[[int], str]) -> Callable[[int], str]:
   @wraps(f)
   def wrapper(n:int):
      return f(n) or "0"
   return wrapper

def to_base(base:int) -> Callable[[str], str]:
   @as_integer
   @zero_output
   @positive_input
   def convert(n:int, base:int = base) -> str:
      n_b = ""
      while n:
         n, r = divmod(n, base)
         n_b = f"{Symbols[r]}{n_b}"
      return n_b
   return convert


def base_float(base:int):
   def left_overflow(n:int) -> tuple[int, str]:
      n_ = f"{base * int(n)}"
      return int(n_[:(d := len(n_) - len(str(n)))] or "0"), n_[d:]
   return left_overflow


def to_float(base:int, number:str) -> str:
   def yielder() -> Iterator[str]:
      f = base_float(base)
      cycle:list[int] = list()
      m, n = number.split('.')
      while (n := int(n)) not in cycle and n:
         cycle.append(n)
         m, n = f(n)
         yield Symbols[int(m)]
   return "".join(yielder())

def parse_comma(n:str) -> str:
   return n.replace(',', ".")

def main(base:int, number:str):
   hole, decimal = parse_comma(number).split('.')
   print(
      f"({to_base(base)(hole)}.{to_float(base, f'0.{decimal}')})_{base}"
   )

def loop():
   while (In := input("Input a base and a number: ")):
      base, number = In.split()
      main(int(base), number)

if __name__ == '__main__':

   import sys

   if len(sys.argv) == 1:
      loop()
      exit()

   if len(sys.argv) != 3:
      print(__doc__)
      raise ValueError(f"\n\t{sys.argv} is no good\n\n")

   main(int(sys.argv[1]), sys.argv[2])


